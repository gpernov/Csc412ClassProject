#!/usr/bin/python

import tweepy

consumer_key = 'sOM5YsT8LQQJD9Zs86nncVxsf'
consumer_key_secret = 'BmcecnFTPjCdHcY8cMRsLuPFTUCS6zJujjtelrS0YHQBeJvVcs'

access_token = '979808154-HooZvSj9F2uyuNHXb8oKsLiwMjpjeC3MLiwpdFBH'
access_token_secret = 'nzqTdXiZZM7RZoqNYDveWHPvob1pPTNHVg0IzioCGWGxz'

class TweetListener(tweepy.StreamListener):
	def on_status(self, status):
		print('Tweet text: ' + status.text)
		return True

	def on_errorf(self, status_code):
		print('Got an error with status code: ' + str(status_code))
		return True

	def on_timeout(self):
		print('Timeout...')
		return True

if __name__ == '__main__':
	listener = TweetListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
	auth.set_access_token(access_token, access_token_secret)

	stream = tweepy.Stream(auth, listener)
	stream.filter(follow = [], track = ['#SFGiants', '#Athletics'])
 
