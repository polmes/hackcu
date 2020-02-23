import tweepy
import requests

class MentionListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
		img = status.extended_entities['media'][0]['media_url_https']

		headers = {
		    'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K',
		}

		files = {
		    'image': img,
		}

		response = requests.post('https://api.deepai.org/api/densecap', headers=headers, files=files).json()

		caption = response['output']['captions'][0]['caption']

		# print(response)
		print(caption)
