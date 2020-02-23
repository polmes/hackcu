import tweepy
import os
import configparser
from listener import MentionListener

def main():
	# Read access keys
	config = configparser.ConfigParser()
	cwd = os.path.dirname(os.path.abspath(__file__))
	config.read(os.path.join(cwd, 'config/private.cnf'))

	# Setup key variables
	api = config['api']
	token = config['token']
	deepai = config['deepai']

	# Authenticate
	auth = tweepy.OAuthHandler(api['key'], api['secret'])
	auth.set_access_token(token['key'], token['secret'])

	# Start Tweepy
	api = tweepy.API(auth)

	# Twitter Streaming API
	listener = MentionListener(api, deepai)
	stream = tweepy.Stream(auth=api.auth, listener=listener)
	stream.filter(track=['@JustCaptionThis']) # is_async=true?

if __name__ == '__main__':
	main()
