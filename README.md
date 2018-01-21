# clscraper - Craigslist scraper for RSS
================================

Scrapes CL posts for terms and reports them to slack via api key.

I use it to find deals on gpu's and other things.



## build details

`docker build -t cl_scraper .

docker run --env SLACKBOT_API_KEY='{your bot api key goes here}' cl_scraper`
