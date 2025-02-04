import base64
import dataclasses
from typing import Any, List, Sequence, Union

from chalk._gen.chalk.common.v1.online_query_pb2 import FeatureExpression
from chalk.features import Feature, FeatureWrapper, Resolver
from chalk.features.feature_set import is_features_cls
from chalk.features.underscore_features import NamedUnderscoreExpr


@dataclasses.dataclass
class EncodedOutputs:
    string_outputs: List[str]
    feature_expressions: List[str]  # B64 encoded


def encode_feature_expression(expr: NamedUnderscoreExpr) -> str:
    proto = FeatureExpression(
        namespace=expr.fqn.split(".")[0],
        output_column_name=expr.fqn,
        expr=expr.expr._to_proto(),  # pyright: ignore[reportPrivateUsage]
    )
    b = proto.SerializeToString(deterministic=True)
    return base64.b64encode(b).decode("utf-8")


def encode_outputs(output: Sequence[Union[str, NamedUnderscoreExpr, Any]]) -> EncodedOutputs:
    """Returns a list of encoded outputs and warnings"""
    string_outputs: List[str] = []
    feature_expressions: List[str] = []
    for o in output:
        if isinstance(o, (Feature, FeatureWrapper)):
            string_outputs.append(str(o))
        elif is_features_cls(o):
            string_outputs.append(o.namespace)
        elif isinstance(o, Resolver):
            string_outputs.append(o.fqn.split(".")[-1])
        elif isinstance(o, NamedUnderscoreExpr):
            feature_expressions.append(encode_feature_expression(o))
        else:
            string_outputs.append(str(o))
    return EncodedOutputs(string_outputs=string_outputs, feature_expressions=feature_expressions)
