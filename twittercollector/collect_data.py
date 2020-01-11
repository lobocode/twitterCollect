import os
import sys
import json

import oauth
from mongo_config import *


class CollectData():
    
    def __init__(self, number_of_tweets, last_id, hashtags):
        
        # Number of tweets
        self.number_of_tweets = number_of_tweets
        # Latests ids
        self.last_id = last_id
        # Hashtags
        self.hashtags = hashtags
        
    # Function for collect tweets
    def get_tweets(self): 
            
            # Search only new tweets with api.search
            api_search = oauth.api.search(q=self.hashtags, count=self.number_of_tweets, show_user=True, include_rts=False,tweet_mode='extended', include_entities=True, max_id=str(self.last_id), since='2019-01-01')

            for info in api_search:

                if info.full_text.startswith("RT @") == True:
                    pass
                else:
                    dict_ = {'hashtag': self.hashtags,
                            'screen_name': info.user.screen_name,
                            'user_name': info.user.name,
                            'tweet': info.full_text,
                            'tweet_created_at': (str(info.created_at)),
                            'language': info.metadata['iso_language_code'],
                            'followers_count': info.user.followers_count
                    
                    }

                    # Convert dict_ in json 
                    mongo_data_json = json.dumps(dict_, ensure_ascii=False)

                    # Decode the JSON from Twitter
                    datajson = json.loads(mongo_data_json)

                    # Insert json into mongo
                    db.twitter_search.insert_one(datajson)

# Call code 
# collect data 
tags=['#openbanking','#apifirst','#devops','#cloudfirst','#microservices','#apigateway','#oauth', '#swagger','#raml','#openapis']

print('\nCollecting twitter data...\n')

for hashtags in tags:
    pdatabase = CollectData(100, -1, hashtags)
    pdatabase.get_tweets() 
