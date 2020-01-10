from pymongo import MongoClient
from src import mongo_config
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import json 

# Access collection into twitterdb
collection = mongo_config.db['twitter_search']

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

# b question #######################################################################################
####################################################################################################
####################################################################################################

find_aggregate_by_hour = collection.aggregate([
{ "$addFields": {
        "tweet_created_at": {
            "$toDate": "$tweet_created_at"
        }
    } }, { "$project": {
      "h":{"$hour":"$tweet_created_at"} }
 }])

convert_aggregate_in_list = list(find_aggregate_by_hour)

encoder_aggregate_list = JSONEncoder().encode(convert_aggregate_in_list)

load_json_aggregate_list = json.loads(encoder_aggregate_list)

split_hrs = []   

for x in load_json_aggregate_list:
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
    
    
# c question #######################################################################################
####################################################################################################
####################################################################################################

find_aggr_by_flag = collection.aggregate([
    { "$project": 
        {
            "hashtag": "$hashtag",
            "language": "$language"
        },
    }])



convert_agrr_to_list = list(find_aggr_by_flag)

encoder_aggr_list = JSONEncoder().encode(convert_agrr_to_list)

load_json_aggr_list = json.loads(encoder_aggr_list)


split_lang = [] 
split_hashtags = [] 

for x in load_json_aggr_list:
    split_lang.append(x['language'])
    

for y in load_json_aggr_list:
    split_hashtags.append(y['hashtag'])

#print(split_hashtags)
  
lang = []
twe_flag = list(set(split_lang))
twe_hash = list(set(split_hashtags))

for x in twe_flag:
    lang.append(split_lang.count(x))
    
group_list_by_flag = []   
     
for x,y,z in zip(twe_hash, lang, twe_flag):   
    c_question = {
        'hashtag': x,
        'language': z,
        'total': y
    }   
    
    group_list_by_flag.append(c_question)

    
"""    
    {
        'hashtag': #devops
        'language': it
        'total': 20
    }
 """   