

"""
reference
# https://stackoverflow.com/questions/23151246/iterrows-pandas-get-next-rows-value
"""

import pandas as pd

from datetime import datetime as dt


# 1st test : iterrows
def using_iterrows(df):

    res = []

    for ind, row in df.iterrows():
        res.append(row)

    return res


# 2nd test : indexing
def using_indexing(df):

    res = []

    for i in range(len(df)):
        res.append(df[df.index == i])

    return res


if __name__ == '__main__':

    df = pd.read_csv(
        'sample.txt',
        sep='\t',
    )

    _start = dt.now()

    res = using_iterrows(df)

    _end = dt.now()

    print('Total Time : {0}'.format(_end-_start))



    _start = dt.now()

    res = using_indexing(df)

    _end = dt.now()

    print('Total Time : {0}'.format(_end - _start))


"""
result :
>>>
using_iterrows : 0:00:00.534812
using_indexing : 0:00:02.428798
>>>
"""
