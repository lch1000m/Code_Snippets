
"""
reference
# https://stackoverflow.com/questions/23151246/iterrows-pandas-get-next-rows-value
"""

import pandas as pd


df = pd.read_csv(
    'sample.txt',
    sep='\t',
)


for ind, row in df.iterrows():
    print(ind)
    print(row.to_dict())
