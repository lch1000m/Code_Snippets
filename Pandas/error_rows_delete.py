# remove error rows

"""
reference
#
"""

import pandas as pd
import numpy as np

from datetime import datetime as dt


df = pd.DataFrame(
    {
        'A':[1,2,3],
        'B':['a',2.2,3.3],
        'C':['2016-07-01','2016-07-02','2016-07-03'],
        'D':['a',1,'b'],
        'E':[1,dt(2017,7,2),'3'],
    }
)


def int_col_test():

    np_int = [
        np.int8,
        np.int16,
        np.int32,
        np.int64,
    ]

    type_assign = int
    column_to_assign_int = 'D'

    remove = []

    try:
        df[column_to_assign_int] = df[column_to_assign_int].astype(type_assign)
    except:
        for i, val in df[column_to_assign_int].iteritems():
            try:
                temp = type_assign(val)
            except:
                remove.append(i)

        print(remove)


def float_col_test():

    np_float = [
        np.float16,
        np.float32,
        np.float64,
    ]

    type_assign = float
    column_to_assign_int = 'B'

    remove = []

    try:
        df[column_to_assign_int] = df[column_to_assign_int].astype(type_assign)
    except:
        for i, val in df[column_to_assign_int].iteritems():
            try:
                temp = type_assign(val)
            except:
                remove.append(i)

        print(remove)


def str_col_test():
    """
    str field converted no matter input value is
    no need to correction
    """

    str_type = [
        np.object,
    ]

    type_assign = str
    column_to_assign = 'E'

    remove = []

    try:
        df[column_to_assign] = df[column_to_assign].astype(type_assign)
    except:
        for i, val in df[column_to_assign].iteritems():
            try:
                temp = type_assign(val)
            except:
                remove.append(i)

    print(remove)



def time_col_test():
    """
    time field converted no matter input value is
    no need to correction
    """

    str_type = [
        'datetime64[ns]',
    ]

    type_assign = 'datetime64[ns]'
    column_to_assign = 'E'

    remove = []

    try:
        df[column_to_assign] = df[column_to_assign].astype(type_assign)
        print(df[column_to_assign].dtypes)

        print(df)

    except:
        for i, val in df[column_to_assign].iteritems():
            try:
                temp = type_assign(val)
            except:
                remove.append(i)

            print(remove)





if __name__ == '__main__':

    # int_col_test()
    # float_col_test()
    # str_col_test()
    time_col_test()
