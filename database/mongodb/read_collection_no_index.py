# make mongo collection

import threading
import pandas as pd

from pymongo import MongoClient
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


def main(i):

    mongo = MongoClient('localhost',27017)['test_db']['big_data_no_index']  # no index

    query = {
        '$and': [
            {'Time': {'$gte': '2017-09-01 00:00:00'}},
            {'Time': {'$lte': '2017-09-30 00:00:00'}},
            # {'No': {'$gte': 2500000}},
            # {'No': {'$lte': 5000000}},
        ]
    }

    usecols = {
        '_id':0,
        'Time':1,
        'No':1,
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

    num_of_thread = 1

    threads = []

    for i in range(num_of_thread):
        threads.append(threading.Thread(target=main, args=(i,)))

    for th in threads:
        th.start()

    for th in threads:
        th.join()
