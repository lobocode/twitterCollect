from pymongo import MongoClient
from mongo_config import *
from bson.objectid import ObjectId

# Access collection into twitterdb
collection = db['twitter_search']



# The five users with the most followers
five_most_followers = collection.find({}, {"followers_count": 1, "user_name": 1}).limit(5).sort("followers_count", -1)

list_five_most_followers = list(five_most_followers)

print(list_five_most_followers)

# Total posts grouped by time of day
#total_grouped_time = collection.find({}, {"tweet": 1}).limit(2)

#x = list(total_grouped_time)

#print(x)

# Total posts for each of the tags by language / country.