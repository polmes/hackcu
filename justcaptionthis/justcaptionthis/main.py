import tweepy
import os
import configparser
from listener import MentionListener

def main():
	filepath = 'config/private.cnf'
	if os.path.isfile(filepath):
		# Read access keys
		config = configparser.ConfigParser()
		cwd = os.path.dirname(os.path.abspath(__file__))
		config.read(os.path.join(cwd, filepath))

		# Setup key variables
		api = config['api']
		token = config['token']
		deepai = config['deepai']
	else:
		# Use environment variables
		api = {
			'key': os.environ['API_KEY'],
			'secret': os.environ['API_SECRET']
		}
		token = {
			'key': os.environ['TOKEN_KEY'],
			'secret': os.environ['TOKEN_SECRET']
		}
		deepai = {
			'key': os.environ['DEEPAI_KEY'],
		}

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
