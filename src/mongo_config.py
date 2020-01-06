from pymongo import MongoClient


# Assuming you have mongoDB installed locally
mongo_host= ('mongodb://localhost/twitterdb')

client = MongoClient(mongo_host)

# Use twitterdb database. If it doesn't exist, it will be created.
db = client.twitterdb

