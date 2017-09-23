# make sparse df for memory efficiency

"""
reference
#
"""

import pandas as pd
import numpy as np


df = pd.read_table(
    'sample.txt',
    sep='\t'
)

for i in range(10):
    df['column_'+str(i+100)] = np.nan


print(df.info())


df_sparse = pd.SparseDataFrame(df)

print(df_sparse.info())

pivot = pd.pivot_table(
    df_sparse,
    index=['Name'],
    columns=['Sub'],
    values='Col1'
)

print(pivot.head())

import pdb; pdb.set_trace()
