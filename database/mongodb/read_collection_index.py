# make mongo collection

import pandas as pd

from pymongo import MongoClient
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


def main():
    start = dt.now()

    mongo = MongoClient('localhost',27017)['test_db']['big_data_index']     # w/ index
    # mongo = MongoClient('localhost',27017)['test_db']['big_data_no_index']  # no index

    query = {
        '$and':[
            {'Time':{'$gte':'2017-07-01 00:00:00'}},
            {'Time':{'$lte':'2017-09-30 00:00:00'}},
            # {'Col_0':{'$gte':0.8}},
        ]
    }

    usecols = {
        '_id':0,
        'Time':1,
        'No':1,
    }

    cursor = mongo.find(query)

    print(cursor.count())

    for cur in cursor:
        pass

    # df = pd.DataFrame(list(cursor))

    total_time = (dt.now() - start).total_seconds()

    print('Total Time : {0}'.format(total_time))



if __name__ == '__main__':

    for i in range(3):
        main()
