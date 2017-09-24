# test dealing with datetime

"""
reference
#
"""

import pandas as pd

from datetime import datetime as dt


df = pd.DataFrame(
    {
        'A':[1,2,3],
        'B':['2017-07-01','2017-07-02','2017-07-03'],
        'C':[dt(2017,7,1),dt(2017,7,2),dt(2017,7,3)],
    }
)


print(df.info())


df['B'] = df['B'].astype('datetime64[ns]')

print(df.info())
