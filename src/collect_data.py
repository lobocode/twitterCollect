import os
import sys
import json
from oauth import *
from mongo_config import *

# Function for collect tweets
def get_tweets(hashtags): 
          
        # Number of tweets 
        number_of_tweets=100

        # latest ids
        last_id = -1

        # Search only new tweets with api.search
        api_search = api.search(q=hashtags, count=number_of_tweets, show_user=True, include_rts=False,tweet_mode='extended', include_entities=True, max_id=str(last_id - 1), since='2019-01-01')

        for info in api_search:

            if info.full_text.startswith("RT @") == True:
                pass
            else:
                dict_ = {'hashtag': hashtags,
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
if __name__ == '__main__': 
  

    # collect data 
    tags=['#openbanking','#apifirst','#devops','#cloudfirst','#microservices','#apigateway','#oauth', '#swagger','#raml','#openapis']
    for x in tags:
        get_tweets(x)  

# Test post one tweet 
#api.update_status("OI!")

