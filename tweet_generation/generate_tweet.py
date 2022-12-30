import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random
from tweet_generation.query_generation import get_random_element_of_list, generate_astrology_gpt_list_of_query

def initialize_client_astrology():
    consumer_key = os.environ.get("api_key_astrology")
    consumer_secret = os.environ.get("api_secret_astrology")

    access_token = os.environ.get("access_token_astrology")
    access_secret = os.environ.get("access_secret_astrology")


    openai.api_key = os.environ.get("open_ai_secret")

    return tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_secret)

def generate_astrolgy_tweet():
    emojis = ["🌌", "🌠",'🌟','🌃','✨', '🪐','🌍', '🪬','🔭','🚀']

    queries = generate_astrology_gpt_list_of_query()
    querie_to_tweet = get_random_element_of_list(queries)[0]

    gpt_response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=querie_to_tweet,
                    temperature=0.5,
                    max_tokens=256,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                    )['choices'][0]['text'].replace('\n','')

    random_emoji = get_random_element_of_list(emojis)[0]
    tweet_content = random_emoji+gpt_response+random_emoji
    
    twitter_client = initialize_client_astrology()
    tweet_response = twitter_client.create_tweet(text=tweet_content)
    print("Successfully tweeted")

def main():
    openai.api_key = os.environ.get("open_ai_secret")
    generate_astrolgy_tweet()
