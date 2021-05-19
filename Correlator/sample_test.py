# sample test

import pandas as pd


df = pd.DataFrame(
    {
        'lot':['A','B','C'],
        'wf':[1.0,2,13],
    }
)

df['wf'] = df['wf'].astype(int)

df.loc[df['wf']< 10, 'temp'] = '0' + df['wf'].astype(str)
df.loc[df['temp'].isnull(), 'temp'] = df['wf'].astype(str)

df['lot_wf'] = df['lot'] + '_' + df['temp']

print(df)

print('end')
