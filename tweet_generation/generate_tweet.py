import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random
import time
import datetime
from tweet_generation.query_generation import get_random_element_of_list, generate_astrology_gpt_list_of_query, generate_horoscope_thread

def initialize_client_astrology():
    consumer_key = os.environ.get("api_key_astrology")
    consumer_secret = os.environ.get("api_secret_astrology")

    access_token = os.environ.get("access_token_astrology")
    access_secret = os.environ.get("access_secret_astrology")

    return tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_secret)

def tweet_thread(thread):
    twitter_client = initialize_client_astrology()
    prev_tweet = twitter_client.create_tweet(text=thread[0])
    for i in thread[1:]:
        new_tweet = twitter_client.create_tweet(text=i[:280], in_reply_to_tweet_id=prev_tweet[0]['id'])
        prev_tweet = new_tweet
    print("Successfully generated thread")

def generate_gpt_response(query):
    gpt_response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=query,
                    temperature=0.5,
                    max_tokens=256,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                    )['choices'][0]['text'].replace('\n','')
    return gpt_response

def generate_astrolgy_hourly_tweet():
    emojis = ["🌌", "🌠",'🌟','🌃','✨', '🪐','🌍', '🪬','🔭','🚀']

    queries = generate_astrology_gpt_list_of_query()
    querie_to_tweet = get_random_element_of_list(queries)[0]

    gpt_response = generate_gpt_response(querie_to_tweet)

    random_emoji = get_random_element_of_list(emojis)[0]
    tweet_content = random_emoji+gpt_response+random_emoji
    
    twitter_client = initialize_client_astrology()
    tweet_response = twitter_client.create_tweet(text=tweet_content[:256])
    print("Successfully tweeted")

def generate_astrology_horoscope(thread_queries):
    _thread = ["✨ Daily Horoscope ✨\n"+datetime.date.today().strftime("%d/%m/%Y")+"\nTake a look at what the stars have in mind for you today"]
    for query in thread_queries:
        time.sleep(2)
        _thread.append(generate_gpt_response(query))
    return _thread

def hourly_tweet():
    openai.api_key = os.environ.get("open_ai_secret")
    generate_astrolgy_hourly_tweet()

def daily_tweet():
    openai.api_key = os.environ.get("open_ai_secret")
    thread_to_query = generate_horoscope_thread()
    thread_to_tweet = generate_astrology_horoscope(thread_to_query)
    tweet_thread(thread_to_tweet)
