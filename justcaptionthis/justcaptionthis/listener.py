import tweepy
import requests

class MentionListener(tweepy.StreamListener):

	def __init__(self, api, deepai):
		self.api = api
		self.key = deepai['key']

	def on_status(self, status):
		if hasattr(status, 'extended_entities'):
			print(status.text)

			# Get first image url in tweet
			img = status.extended_entities['media'][0]['media_url_https']

			# Call DenseCap API
			headers = {
				'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K',
			}

			files = {
				'image': img,
			}

			response = requests.post('https://api.deepai.org/api/densecap', headers=headers, files=files).json()

			# Take first caption provided
			caption = response['output']['captions'][0]['caption']
			# caption = f"@{status.author.screen_name} {response['output']['captions'][0]['caption']}"

			# print(response)
			print(caption)

			# Tweet (reply) the response
			self.api.update_status(caption, in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)
