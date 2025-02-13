from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Callable, Dict, Iterable, Mapping, Optional, Sequence, cast

import pyarrow as pa

from chalk.features import Feature
from chalk.integrations.named import load_integration_variable
from chalk.sql._internal.query_execution_parameters import QueryExecutionParameters
from chalk.sql._internal.sql_source import BaseSQLSource, SQLSourceKind
from chalk.sql.finalized_query import FinalizedChalkQuery
from chalk.utils.log_with_context import get_logger
from chalk.utils.missing_dependency import missing_dependency_exception
from chalk.utils.tracing import safe_trace

if TYPE_CHECKING:
    from sqlalchemy.engine import Connection
    from sqlalchemy.engine.url import URL

    try:
        from pyathena.connection import Connection as AthenaConnection
    except ImportError:
        pass
_logger = get_logger(__name__)


class AthenaSourceImpl(BaseSQLSource):
    kind = SQLSourceKind.athena

    def __init__(
        self,
        *,
        name: str | None = None,
        aws_region: str | None = None,
        aws_access_key_id: str | None = None,
        aws_access_key_secret: str | None = None,
        s3_staging_dir: str | None = None,
        schema_name: str | None = None,
        catalog_name: str | None = None,
        role_arn: str | None = None,
        engine_args: Dict[str, Any] | None = None,
    ):
        try:
            import pyathena
        except ModuleNotFoundError:
            raise missing_dependency_exception("chalkpy[athena]")
        else:
            del pyathena  # unused here

        self.aws_region = aws_region or load_integration_variable(integration_name=name, name="ATHENA_AWS_REGION")
        self.aws_access_key_id = aws_access_key_id or load_integration_variable(
            integration_name=name, name="ATHENA_AWS_ACCESS_KEY_ID"
        )
        self.aws_access_key_secret = aws_access_key_secret or load_integration_variable(
            integration_name=name, name="ATHENA_AWS_ACCESS_KEY_SECRET"
        )
        self.s3_staging_dir = s3_staging_dir or load_integration_variable(
            integration_name=name, name="ATHENA_S3_STAGING_DIR"
        )
        self.role_arn = role_arn or load_integration_variable(integration_name=name, name="ATHENA_ROLE_ARN")
        self.schema_name = schema_name or load_integration_variable(integration_name=name, name="ATHENA_SCHEMA_NAME")
        self.catalog_name = catalog_name or load_integration_variable(integration_name=name, name="ATHENA_CATALOG_NAME")

        if engine_args is None:
            engine_args = {}
        engine_args.setdefault("pool_size", 20)
        engine_args.setdefault("max_overflow", 60)
        engine_args.setdefault("connect_args", {"s3_staging_dir": s3_staging_dir})

        BaseSQLSource.__init__(self, name=name, engine_args=engine_args, async_engine_args={})

    @functools.cached_property
    def _pyathena_connection(self) -> AthenaConnection:
        try:
            from pyathena.arrow.async_cursor import AsyncArrowCursor
            from pyathena.connection import Connection as AthenaConnection
        except ModuleNotFoundError:
            raise missing_dependency_exception("chalkpy[athena]")
        return AthenaConnection(
            s3_staging_dir=self.s3_staging_dir,
            role_arn=self.role_arn,
            schema_name=self.schema_name,
            catalog_name=self.catalog_name,
            region_name=self.aws_region,
            access_key=self.aws_access_key_id,
            secret_key=self.aws_access_key_secret,
            cursor_class=AsyncArrowCursor,
        )

    def supports_inefficient_fallback(self) -> bool:
        return True

    def get_sqlglot_dialect(self) -> str | None:
        return "athena"

    def local_engine_url(self) -> URL:
        from sqlalchemy.engine.url import URL

        query = {
            k: v
            for k, v in {
                "s3_staging_dir": self.s3_staging_dir,
            }.items()
            if v is not None
        }
        # https://laughingman7743.github.io/PyAthena/sqlalchemy.html
        return URL.create(
            drivername="awsathena+arrow",
            username=self.aws_access_key_id,
            password=self.aws_access_key_secret,
            host=f"athena.{self.aws_region}.amazonaws.com",
            port=443,
            database=self.schema_name,
            query=query,
        )

    def _execute_query_efficient(
        self,
        finalized_query: FinalizedChalkQuery,
        columns_to_features: Callable[[Sequence[str]], Mapping[str, Feature]],
        connection: Optional[Connection],
        query_execution_parameters: QueryExecutionParameters,
    ) -> Iterable[pa.RecordBatch]:
        with safe_trace("athena.execute_query_efficient"):
            try:
                from pyathena.arrow.async_cursor import AsyncArrowCursor
                from pyathena.arrow.result_set import AthenaArrowResultSet
            except ModuleNotFoundError:
                raise missing_dependency_exception("chalkpy[athena]")

            assert len(finalized_query.temp_tables) == 0, "Should not create temp tables with athena source"

            formatted_op, positional_params, named_params = self.compile_query(finalized_query)
            assert (
                len(positional_params) == 0 or len(named_params) == 0
            ), "Should not mix positional and named parameters"
            execution_params = None
            paramstyle = None
            if len(positional_params) > 0:
                execution_params = list(positional_params)
                if not all(isinstance(x, str) for x in positional_params):
                    raise ValueError("Only strings are allowed as positional parameters in Athena client")
            elif len(named_params) > 0:
                execution_params = named_params
                paramstyle = "named"
            with self._pyathena_connection as conn:
                cursor = conn.cursor()
                assert isinstance(cursor, AsyncArrowCursor)
                _, query_fut = cursor.execute(
                    operation=formatted_op,
                    parameters=execution_params,
                    paramstyle=paramstyle,
                )
                query_result = cast(AthenaArrowResultSet, query_fut.result())
                parsed_table = query_result.as_arrow()
                features = columns_to_features(parsed_table.column_names)

                restricted_schema = pa.schema([pa.field(k, v.converter.pyarrow_dtype) for (k, v) in features.items()])
                parsed_table = parsed_table.select(list(features.keys()))
                parsed_table = parsed_table.cast(restricted_schema)
                parsed_table = parsed_table.rename_columns([x.root_fqn for x in features.values()])
                if len(parsed_table) > 0:
                    yield parsed_table.combine_chunks().to_batches()[0]
                if len(parsed_table) == 0 and query_execution_parameters.yield_empty_batches:
                    yield pa.RecordBatch.from_pydict({k: [] for k in parsed_table.schema.names}, parsed_table.schema)
                return
