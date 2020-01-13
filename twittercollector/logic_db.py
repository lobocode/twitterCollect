from pymongo import MongoClient
from mongo_config import *
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json

"""
This module contains all queries and logic applied to the database.
"""


# Access collection into twitterdb
collection = db['twitter_search']

# pymongo query to mongodb
find_fl = collection.aggregate([
    {'$group': {'_id': {"user_name": "$user_name", "followers_count": "$followers_count"}}},
    {'$sort': {"_id.followers_count": -1}},
    {'$limit': 5}
])

# json_format_fl var convert cursor query in list, serialization bson, convert bson in json and deserialize
json_format_fl = json.loads(dumps(list(find_fl)))

# b question #######################################################################################

# pymongo query to mongodb
find_aggregate_by_hour = collection.aggregate([
    {
        "$addFields": {
            "tweet_created_at": {
                "$toDate": "$tweet_created_at"
            }
        }
    },
    {
        "$project": {
            "hours": {
                "$hour": "$tweet_created_at"
            }
        }
    },
    { "$group" : {
        "_id" : "$hours",
        "count" : { "$sum" : 1
                }
    }
    },
    { "$match" : {
        "_id" : { "$gt" : 1
              }
    }
    }
])

# json_format_fl var convert cursor query in list, serialization bson, convert bson in json and deserialize
aggr_by_hr = json.loads(dumps(list(find_aggregate_by_hour)))
print(aggr_by_hr)


# c question #######################################################################################
