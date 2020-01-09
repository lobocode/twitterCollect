from pymongo import MongoClient

# Assuming you have mongoDB installed locally
mongo_host = ('mongodb://admin:admin@localhost/twitterdb?authSource=admin')

client = MongoClient(mongo_host)

# Use twitterdb database. If it doesn't exist, it will be created.
db = client.twitterdb

