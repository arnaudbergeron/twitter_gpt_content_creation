import tweepy
import os
from dotenv import load_dotenv
from requests_oauthlib import OAuth1Session
import json
import openai
import random

def get_random_element_of_list(list_to_rand_1, list_to_rand_2=None):
    rand_element_index = random.randint(0, len(list_to_rand_1)-1)
    rand_element = [list_to_rand_1[rand_element_index]]
    if list_to_rand_2 is not None:
        rand_element.append(list_to_rand_2[rand_element_index])
    return rand_element


def generate_astrology_gpt_list_of_query():
    astological_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo",\
    "Virgo","Libra","Scorpio", "Sagittarius",\
        "Capricorn","Aquarius","Pisces"]
    astrological_planets = ["Mars", "Venus", "Mercury", "Moon","Sun","Mercury","Venus","Pluto","Jupiter","Saturn","Uranus","Neptune"]
    subjects=["love","luck","career and education", "health"]

    random_sign_planet = get_random_element_of_list(astological_signs, astrological_planets)
    random_sign = random_sign_planet[0]
    random_planet = random_sign_planet[1]
    random_subjects = get_random_element_of_list(subjects)[0]
    gpt_prompt_1 = "Write a tweet about astrology and what is going to happen to {} today about {}, be specific and format for posting and add hashtags".format(random_sign,random_subjects)
    gpt_prompt_2 = "Write an inspiring tweet about astrology and be very specific about what is going to happen to {} today about {} and why the alignment of {} will influence this event, be specific and format for posting and add hashtags".format(random_sign,random_subjects, random_planet)
    gpt_prompt_3 = "Write a tweet about astrology and be very specific about what {} should do today as an activity to make {} better, be specific and format for posting and add hashtags".format(random_sign,random_subjects)
    gpt_prompt_4 = "Write a tweet about astrology and be very specific about what {} should do today to make their love life better and how they should go after what they are looking for, be specific and format for posting and add hashtags".format(random_sign)
    gpt_prompt_5 = "Write a tweet aimed at young adult girls about astrology about how they should tag their {} friends in order to help them with their {} today, be specific and format for posting and add hashtags".format(random_sign, random_subjects)
    prompts = [gpt_prompt_1, gpt_prompt_2, gpt_prompt_3, gpt_prompt_4, gpt_prompt_5]

    return prompts
