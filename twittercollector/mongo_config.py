from pymongo import MongoClient

# Assuming you have mongoDB installed locally
mongo_host= ('mongodb://localhost/twitterdb')

client = MongoClient(mongo_host)

# check if collection already exist
appdb = client['twitterdb']
app_collection = appdb['twitter_search']

collection_name = 'twitter_search'
if collection_name in appdb.list_collection_names():
    print('\nThis collection already exists in db.\n')
else:
    # Use twitterdb database. If it doesn't exist, it will be created.
    db = client.twitterdb

