# make mongo collection

import pandas as pd
from multiprocessing import Process

from pymongo import MongoClient
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


def main(i):

    mongo = MongoClient('localhost',27017)['test_db']['big_data_index']  # no index

    query = {
        '$and': [
            {'Time': {'$gte': '2017-09-01 00:00:00'}},  # 15638401
            {'Time': {'$lte': '2017-09-30 00:00:00'}},  # 23500801
            # {'No': {'$gte': 15638401}},
            # {'No': {'$lte': 23500801}},
            # {'col_0': {'$gte': 0.1}},
            # {'col_0': {'$lte': 0.9}},
        ]
    }

    usecols = {
        '_id':1,
        'Time':1,
        'No':1,
        'col_0':1,
        'col_1':1,

        'col_2':1,
        'col_3':1,
        'col_4':1,
        'col_5':1,
        'col_6':1,

        'col_7': 1,
        'col_8': 1,
        'col_9': 1,
        'col_10': 1,
        'col_11': 1,

        'col_12': 1,
        'col_13': 1,
        'col_14': 1,
        'col_15': 1,
        'col_16': 1,

        'col_17': 1,
        'col_18': 1,
        'col_19': 1,
        'col_20': 1,
        'col_21': 1,

        'col_22': 1,
        'col_23': 1,
        'col_24': 1,
        'col_25': 1,
        'col_26': 1,
        #
        # 'col_27': 1,
        # 'col_28': 1,
        # 'col_29': 1,
        # 'col_30': 1,
        # 'col_31': 1,
        #
        # 'col_32': 1,
        # 'col_33': 1,
        # 'col_34': 1,
        # 'col_35': 1,
        # 'col_36': 1,
    }

    start = dt.now()

    cursor = mongo.find(query)

    print(cursor.count())

    total_time = (dt.now() - start).total_seconds()
    print('{0} : Indexing Time : {1}'.format(i, total_time))


    start = dt.now()

    for cur in cursor:
        pass

    # df = pd.DataFrame(list(cursor))

    total_time = (dt.now() - start).total_seconds()

    print('{0} : Query Time : {1}'.format(i, total_time))


if __name__ == '__main__':

    num_of_thread = 3

    procs = []

    for i in range(num_of_thread):
        procs.append(Process(target=main, args=(i,)))

    for proc in procs:
        proc.start()

    for proc in procs:
        proc.join()
