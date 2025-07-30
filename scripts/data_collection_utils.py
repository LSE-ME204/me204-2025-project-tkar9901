## Imports
import pandas as pd
import numpy as np

## Set nulls based on custom values from EES
def set_nulls(x):
    if x in ["z", "x", "c"]:
        return np.nan
    else:
        try:
            return pd.to_numeric(x)
        except (ValueError, TypeError):
            return x

## Adjust time periods to a more readable format
def adjust_time_periods(col):
    return str(col)[:4] + " to " + str(col)[4:]