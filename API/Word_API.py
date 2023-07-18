import random

import requests
import json

from tokens import Word_API

key = Word_API()

def word(word):
    definitions = []
    url = 'https://stdict.korean.go.kr/api/search.do'
    params ={
        "key" : key,
        "q" : word,
        "num": 10,
        "req_type" : 'json',

    }
    response = requests.get(url, params=params)
    data = response.json()
    items = data['channel']['item']
    for item in items:
        definition = item['sense']['definition']
        definitions.append(definition)

    return definitions

#역량부족
"""def get_word_info(word):
    url = 'https://stdict.korean.go.kr/api/search.do'
    params = {
        "key": key,
        "q": word,
        "advanced": "y",
        "pos": 1
    }
    response = requests.get(url, params=params)
    return response.json()

def is_valid_word(word):
    if word[-1] in ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '튼', '름', '늠', '쁨']:
        return False
    word_info = get_word_info(word)
    if not word_info["data"]:
        return False
    return True

def choose_next_word(last_word):
    url = 'https://stdict.korean.go.kr/api/search.do'
    params = {
        "key": key,
        "q": last_word,
        "advanced": "y",
        "pos": 1,
        "method": "start",
        "num": 100,
    }
    response = requests.get(url, params=params)
    data = response.json()
    words = [item["word"] for item in data["data"]]
    valid_words = [word for word in words if is_valid_word(word)]
    if not valid_words:
        return None
    return random.choice(valid_words)"""