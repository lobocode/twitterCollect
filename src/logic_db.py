from pymongo import MongoClient
from .mongo_config import *
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

