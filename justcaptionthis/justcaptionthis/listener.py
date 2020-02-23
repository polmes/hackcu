import tweepy
import requests
from utils import ocr, tweetsplitter

class MentionListener(tweepy.StreamListener):

	def __init__(self, api, deepai):
		self.api = api
		self.key = deepai['key']

	def on_status(self, status, firstcall=True):
		# Save ID of first tweet with @mention to reply to
		if firstcall:
			self.id = status.id

			# One or multiple captions?
			opts = ['tell me more']
			if any(substr in status.text.lower() for substr in opts):
				self.more = True
			else:
				self.more = False

		# If tweet has an image, tag this one
		if hasattr(status, 'extended_entities'):
			print(status.text)

			# Setup DenseCap
			headers = {
				'api-key': self.key,
			}

			# Iterate through each image in tweet
			caption = []
			for each in status.extended_entities['media']:
				# Get image URL
				img = each['media_url_https']
				files = {
					'image': img,
				}

				# Call DenseCap API
				response = requests.post('https://api.deepai.org/api/densecap', headers=headers, files=files).json()

				# Call tesseract for OCR
				text = ocr(img)

				# Construct caption
				if 'output' in response:
					if not self.more:
						# Take first caption provided
						cap = response['output']['captions'][0]['caption']
					else:
						# Take next 3 captions
						cap = '; '.join([response['output']['captions'][i]['caption'] for i in range(1, 4)])

					# Add OCR text if detected
					if text is not None:
						cap = 'The image shows ' + cap + ' and it says ' + text

					caption.append(cap)

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
				if len(tweet) <= 280:
					self.api.update_status(tweet, in_reply_to_status_id=self.id, auto_populate_reply_metadata=True)
				else:
					tweets = tweetsplitter(tweet)
					prev = self.id
					for t in tweets:
						latest = self.api.update_status(t, in_reply_to_status_id=prev, auto_populate_reply_metadata=True)
						prev = latest.id

		# If tweet has no image, try and find parent tweet with image
		else:
			if status.in_reply_to_status_id is not None:
				parent = self.api.get_status(status.in_reply_to_status_id)

				# Recursive call
				self.on_status(parent, False)
