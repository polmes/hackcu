import tweepy

class MentionListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
