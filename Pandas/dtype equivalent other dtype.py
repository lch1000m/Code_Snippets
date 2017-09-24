# dtype equivalent test

"""
reference
#
"""

import pandas as pd
import numpy as np

from datetime import datetime as dt


df = pd.DataFrame(
    {
        'A':[1,2,3.3],
        'B':[1.1,2.2,3.3],
        'C':['2016-07-01','2016-07-02',1.235],
        'D':['a',1,'b'],
        'E':[dt(2017,7,1),dt(2017,7,2),'2016-07-03'],
    }
)


def int_col_test():

    np_int = [
        np.int8,
        np.int16,
        np.int32,
        np.int64,
    ]

    df['A'] = df['A'].astype(np.int8)

    print(df['A'].dtypes)   # force assign df['A'] as np.int8

    res = df['A'].dtypes in np_int  # df['A'] dtype is np.int64

    print(res)  # result is True


def float_col_test():

    np_float = [
        np.float16,
        np.float32,
        np.float64,
    ]

    df['B'] = df['B'].astype(np.float16)

    res = df['B'].dtypes in np_float

    print(res)


def str_col_test():

    str_type = [
        np.object,
    ]

    res = df['D'].dtypes in str_type

    print(res)


def time_col_test():

    time_type = [
        'datetime64[ns]',
    ]

    res = df['E'].dtypes in time_type

    # print(res)



if __name__ == '__main__':

    # int_col_test()
    # float_col_test()
    # str_col_test()
    # time_col_test()
    other_test()
