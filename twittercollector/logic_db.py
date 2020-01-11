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
{ '$group': {'_id': {"user_name": "$user_name", "followers_count":"$followers_count"}}},
{ '$sort' : { "_id.followers_count": -1 } },
{ '$limit': 5}
])

# json_format_fl var convert cursor query in list, serialization bson, convert bson in json and deserialize
json_format_fl = json.loads(dumps(list(find_fl)))

# b question #######################################################################################

# pymongo query to mongodb
find_aggregate_by_hour = collection.aggregate([
{ "$addFields": {
        "tweet_created_at": {
            "$toDate": "$tweet_created_at"
        }
    } }, { "$project": {
      "h":{"$hour":"$tweet_created_at"} }
 }])

# json_format_fl var convert cursor query in list, serialization bson, convert bson in json and deserialize
aggr_by_hr = json.loads(dumps(list(find_aggregate_by_hour)))

split_hrs = []   

for x in aggr_by_hr:
    split_hrs.append(x['h'])
     
hrs = []
twe = list(set(split_hrs))

for x in twe:
    hrs.append(split_hrs.count(x))
    
group_list_by_hours = []    
    
for z,y in zip(twe, hrs):   
    b_question = {
        'hours': z,
        'tweets': y
    }
    group_list_by_hours.append(b_question)

