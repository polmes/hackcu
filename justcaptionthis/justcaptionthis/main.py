import tweepy
import configparser

# Read access keys
config = configparser.ConfigParser()
config.read('./justcaptionthis/justcaptionthis/config/private.cnf')
api = config['api']
token = config['token']

# Authenticate
auth = tweepy.OAuthHandler(api['key'], api['secret'])
auth.set_access_token(token['key'], token['secret'])

# Start Tweepy
api = tweepy.API(auth)

# Test: read
public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)

# Test: write
api.update_status('This is still not a bot 🤖')
