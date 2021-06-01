from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import Boolean, Numeric
from featuretools.utils.gen_utils import Library


class NumFalse(AggregationPrimitive):
    name = "num_false"
    input_types = [Boolean]
    return_type = Numeric
    default_value = 0

    def get_function(self, agg_type=Library.PANDAS):
        def num_false(x):
            return (x == 0).sum()

        return num_false
