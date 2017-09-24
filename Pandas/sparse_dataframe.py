# make sparse df for memory efficiency

"""
reference
#
"""

import pandas as pd
import numpy as np


dic = pd.DataFrame(
    {
        'ITEM':['A','B'],
        'VALUES':[1.23, 'asdsd'],
    }
)


df = pd.SparseDataFrame(
    pd.read_csv(
        'sample.txt',
        sep='\t'
    )
)

for i in range(10):
    df['column_'+str(i+100)] = np.nan


print(df.info())


df_sparse = pd.SparseDataFrame(df)

print(df_sparse.info())


df_sparse['kkk'] = 111

print(df_sparse.info())


df_sparse = pd.merge(df_sparse, dic, on=['ITEM'])

print(df_sparse.info())
