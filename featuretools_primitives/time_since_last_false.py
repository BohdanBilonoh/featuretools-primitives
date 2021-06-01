import numpy as np
import pandas as pd

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import DatetimeTimeIndex, Boolean, Numeric
from featuretools.utils import convert_time_units
from featuretools.utils.gen_utils import Library
from datetime import datetime


class TimeSinceLastFalse(AggregationPrimitive):
    name = "time_since_last_false"
    input_types = [DatetimeTimeIndex, Boolean]
    return_type = Numeric
    uses_calc_time = True

    def get_function(self):
        def time_since_last_false(times, booleans, time=None):
            if (booleans == 0).sum() > 0:
                time_since = time - times.loc[booleans == 0].iloc[-1]
                return convert_time_units(time_since.total_seconds(), 'seconds')
            return np.nan

        return time_since_last_false
