try:
    import json
except ImportError:
    import simplejson as json
import sys
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
import csv
import time
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
ACCESS_KEY = '940193737237413888-7P7F949i64HhvPA5uAqpnMNnZIhpvhY'
ACCESS_SECRET = '8QKpo2sB67UMMPfr3yn0VXu4n1WMMoxvw7meiMJjqzt35'
CONSUMER_KEY = 'Za02taiQpxuOkpUvyBfPyeQBZ'
CONSUMER_SECRET = '6UHavBCROhBNFPmkhvbskck8y3kybDjTQkqTnNgwoyBeC3fxBt'
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search,
                           q="#sarcasm",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    if tweet.text[0:2] != 'RT':
		print tweet
		print "\nprojectnewline\n"
		with open("a.csv",'a') as f:
			txt=tweet.text
			txt=txt.encode('utf-8')
			s=str(txt)
			f.write(txt)
			f.write("\n\nprojectnewline\n\n")