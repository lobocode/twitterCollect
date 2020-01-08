from pymongo import MongoClient
from mongo_config import *
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json 

# Access collection into twitterdb
collection = db['twitter_search']

# The five users with the most followers
find_fl = collection.find({}, {"followers_count": 1, "user_name": 1}).limit(5).sort("followers_count", -1)

# mongodata into list
five_most_list = list(find_fl)

# define encode and convert BSON to JSON
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
five_most_followers = JSONEncoder().encode(five_most_list)

json_format_fl = json.loads(five_most_followers)


# Total posts grouped by time of day
#total_grouped_time = collection.aggregate({$group: { "_id": {"tweet": 1, "tweet_created_at" : 1 })

total_grouped_time_date = collection.aggregate([
    { "$group": {
        "_id": {
            "tweet": "$tweet",
            "tweet_created_at": "$tweet_created_at"
        }
    }}
])

total_grouped_list = list(total_grouped_time_date)

total_grouped = len(total_grouped_list)

#total_encoder_json = JSONEncoder().encode(total_grouped_list)

#json_format_grouped = json.loads(total_encoder_json)

#x = list(total_grouped_time)

#print(x)

# Total posts for each of the tags by language / country.
"""
db.twitter_search.aggregate([
{ $group: {
    _id : {
        tweet: "$tweet",
        tweet_created_at : "$tweet_created_at"
        }}}]).toArray().length
        
"""