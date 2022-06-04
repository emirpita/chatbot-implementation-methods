import json

import nltk

from mlmodule import predict_wrapper
from main import filter_command
import random
from weblib import search_wrapper, play, book, get_weather, get_news_update, scrape

nltk.download("punkt")


def get_res(res):
    with open('support/intents.json') as file:
        intents = json.load(file)
    tag = res[0]['intent']
    all_tags = intents['intents']
    for tags in all_tags:
        if tags['tag'] != tag:
            continue
        result = random.choice(tags['responses'])
        break
    return result, tag


def response(phrase):
    task, work_f, subject, number, adj, query = filter_command(phrase)
    if task == 0:
        res_1 = predict_wrapper(phrase)
        result, tag = get_res(res_1)
        if tag == "noanswer":
            results = "Here are some google search results"
            search_wrapper(subject, phrase)

    elif task == 1:
        scrape(phrase)
        result = "Here are some results"

    elif task == 2:
        play(phrase, subject)
        result = "Here you go"

    elif task == 3:
        book(phrase)
        result = "Here are some results"

    elif task == 4:
        get_weather()
        result = "Here are the results"

    elif task == 5:
        get_news_update()
        result = "Here are the results"

    else:
        result = "Sorry, I don't think i understand"

    print(result)

# Testing
#response("What is GCP")