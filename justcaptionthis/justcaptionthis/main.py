import tweepy
import configparser
from listener import MentionListener

# Read access keys
config = configparser.ConfigParser()
config.read('./justcaptionthis/justcaptionthis/config/private.cnf')
api = config['api']
token = config['token']
deepai = config['deepai']

# Authenticate
auth = tweepy.OAuthHandler(api['key'], api['secret'])
auth.set_access_token(token['key'], token['secret'])

# Start Tweepy
api = tweepy.API(auth)

# # Test: read
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
# 	print(tweet.text)

# # Test: write
# api.update_status('This is still not a bot 🤖')

# Test: streaming
listener = MentionListener(api, deepai)
stream = tweepy.Stream(auth=api.auth, listener=listener)
stream.filter(track=['@JustCaptionThis']) # is_async=true?
