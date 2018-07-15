
import pandas as pd, numpy as np

from datetime import datetime as dt


df = pd.DataFrame({
    'A':[1,2,3],
    'B':[1.1,2.2,3.3],
    'C':['a','b','c'],
    'D':[dt(2017,3,20),dt(2017,3,21),dt(2017,3,22)],
})


print(df)

for col in df.columns:
    res = pd.core.dtypes.common._get_dtype_type(df[col])
    print(res)

res = df['D'].dtype == pd.datetime64[ns]

print(res)
