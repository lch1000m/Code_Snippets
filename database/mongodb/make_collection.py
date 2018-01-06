# make mongo collection

import pandas as pd, numpy as np

from pymongo import MongoClient
from dateutil.relativedelta import relativedelta
from datetime import datetime as dt


df = pd.DataFrame()


start = dt(2017,1,1)
end   = dt(2018,1,1)

res = []

while True:
    if start >= end:
        break
    else:
        value = str(start)
        res.append(value)
        print('{0} added!'.format(value))

        start += relativedelta(seconds=1)


df['Time'] = res
df['No'] = [i+1 for i in range(len(res))]

for i in range(40):   # addtional columns
    df['col_'+str(i)] = np.random.rand(len(res))


mongo = MongoClient('localhost',27017)['test_db']['big_data']

print('Save to MongoDB start!')

for i, row in df.iterrows():
    print('{0}th'.format(i+1))
    _dic = row.to_dict()

    mongo.insert(_dic)
