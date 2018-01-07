import pymongo

from pymongo import MongoClient
from pprint import pprint

mongo = MongoClient('localhost',27017)['test_db']['big_data_index']  # no index

enum = 1

start = 0

step = 5

end = step

for i in range(enum):
    cursor = mongo.find({},{'_id':0}).sort('No', pymongo.DESCENDING)[start:end]

    for cur in cursor:
        pprint(cur)

    start += step
    end += step
