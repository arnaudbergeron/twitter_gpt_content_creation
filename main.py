from tweet_generation.generate_tweet import main
import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random



openai.api_key = os.environ.get("open_ai_secret")

main()