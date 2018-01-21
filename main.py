#! /bin/env python

import feedparser, time, datetime, os
from slacker import Slacker

ln = [
	'https://raleigh.craigslist.org/search/sya?format=rss',
	'https://raleigh.craigslist.org/search/syp?format=rss',
	'https://raleigh.craigslist.org/search/sys?format=rss',
	'https://raleigh.craigslist.org/search/ela?format=rss']

ids = {}

slackKey = os.environ['SLACKBOT_API_KEY']
slack = Slacker(slackKey)

while True:
	for link in ln:
		feed = feedparser.parse( link )

		for item in feed['items']:
			if item.id not in ids:
				ids[item.id] = True

				if 'gtx' in item.summary.lower() or 'gtx' in item.title.lower():
					msg = "{0}: {1}".format(item.title, item.link)
					m = msg.decode('ascii', 'ignore')
					slack.chat.post_message('#general', msg, as_user=True)

		time.sleep(1)

	time.sleep(10)
