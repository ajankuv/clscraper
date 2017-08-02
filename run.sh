docker build -t localhost/cl_scraper . && \
docker run --env SLACKBOT_API_KEY='{your bot api key goes here}' localhost/cl_scraper
