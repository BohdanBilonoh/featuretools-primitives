import numpy as np
import pandas as pd

from featuretools.primitives import AggregationPrimitive
from featuretools.variable_types import DatetimeTimeIndex, Boolean, Numeric
from featuretools.utils import convert_time_units
from featuretools.utils.gen_utils import Library
from datetime import datetime


class AvgTimeBetweenTrue(AggregationPrimitive):
    name = "avg_time_between_true"
    input_types = [DatetimeTimeIndex, Boolean]
    return_type = Numeric
    description_template = "the average time between each of {}"

    def __init__(self, unit="seconds"):
        self.unit = unit.lower()


    def get_function(self, agg_type=Library.PANDAS):
        def pd_avg_time_between_true(x, booleans):
            x = x.dropna()

            if booleans.sum() < 2:
                return np.nan
            if isinstance(x.iloc[0], (pd.Timestamp, datetime)):
                x = x.astype('int64')

            x = x.loc[booleans == 1]
            avg = (x.max() - x.min()) / (len(x) - 1)
            avg = avg * 1e-9
            return convert_time_units(avg, self.unit)

        return pd_avg_time_between_true
