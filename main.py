from tweet_generation.generate_tweet import main
import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random
from apscheduler.schedulers.blocking import BlockingScheduler
load_dotenv()


scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', seconds=20)
scheduler.start()
