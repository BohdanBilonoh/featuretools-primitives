import numpy as np
import pandas as pd

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import DatetimeTimeIndex, Boolean, Numeric
from featuretools.utils import convert_time_units
from featuretools.utils.gen_utils import Library
from datetime import datetime


class TimeSinceLastTrue(AggregationPrimitive):
    name = "time_since_last_true"
    input_types = [DatetimeTimeIndex, Boolean]
    return_type = Numeric
    uses_calc_time = True

    def get_function(self):
        def time_since_last_true(times, booleans, time=None):
            if booleans.sum() > 0:
                time_since = time - times.loc[booleans == 1].iloc[-1]
                return convert_time_units(time_since.total_seconds(), 'seconds')
            return np.nan

        return time_since_last_true
