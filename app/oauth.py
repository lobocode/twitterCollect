# Import tweepy lib and keys
import tweepy as twe
from keys import *

# OAuth tweepy Twitter API
auth = twe.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = twe.API(auth, wait_on_rate_limit=True)

# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

