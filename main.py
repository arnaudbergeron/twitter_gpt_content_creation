from tweet_generation.generate_tweet import hourly_tweet, daily_tweet
import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random
from apscheduler.schedulers.blocking import BlockingScheduler
load_dotenv()

openai.api_key = os.environ.get("open_ai_secret")
scheduler = BlockingScheduler()
scheduler.add_job(hourly_tweet, 'interval', minutes=60)
scheduler.add_job(daily_tweet, 'cron', hour=7)
scheduler.start()
