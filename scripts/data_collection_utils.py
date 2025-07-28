## Imports
import pandas as pd
import numpy as np

from pandas.api.types import CategoricalDtype


## Set nulls based on custom values from EES
def set_nulls(x):
    if x in ["z", "x", "c"]:
        return np.nan
    else:
        try:
            return pd.to_numeric(x)
        except (ValueError, TypeError):
            return x

## Setup categorical type for grade columns to use numerical agg funcs
def setup_categorical_type(df, col):
    df[col] = df[col].fillna('N/A')
    
    grade_order = CategoricalDtype(categories=['A*', 'A*-', 'A+', 'A', 'A-',
                                               'B+', 'B', 'B-', 'C+', 'C',
                                               'C-', 'D+', 'D', 'D-', 'E+',
                                               'E', 'E-', 'U' , 'N/A'], ordered=True)
    
    df[col] = df[col].astype(grade_order)
    return df
