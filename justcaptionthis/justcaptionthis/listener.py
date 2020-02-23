import tweepy
import requests

class MentionListener(tweepy.StreamListener):

	def __init__(self, api, deepai):
		self.api = api
		self.key = deepai['key']

	def on_status(self, status, firstcall=True):
		# Save ID of first tweet with @mention to reply to
		if firstcall:
			self.id = status.id

		# If tweet has an image, tag this one
		if hasattr(status, 'extended_entities'):
			print(status.text)

			# Check number of images on tweet
			# multiple = True if len(status.extended_entities['media']) > 1 else False
			# img = status.extended_entities['media'][0]['media_url_https']

			# Setup DenseCap
			headers = {
				'api-key': self.key,
			}

			caption = []
			for each in status.extended_entities['media']:
				# Get image URL
				img = each['media_url_https']
				files = {
					'image': img,
				}

				# Call DenseCap API
				response = requests.post('https://api.deepai.org/api/densecap', headers=headers, files=files).json()

				# Take first caption provided
				if 'output' in response:
					caption.append(response['output']['captions'][0]['caption'])


			if caption:
				# Build tweet
				if len(caption) == 1:
					tweet = caption[0]
				else:
					tweet = ''
					for i, c in enumerate(caption):
						tweet += f'[{i+1}] {c}\n'
				print(tweet)

				# Tweet (reply) the response
				self.api.update_status(tweet, in_reply_to_status_id=self.id, auto_populate_reply_metadata=True)

		# If tweet has no image, try and find parent tweet with image
		else:
			if status.in_reply_to_status_id is not None:
				parent = self.api.get_status(status.in_reply_to_status_id)

				# Recursive call
				self.on_status(parent, False)
