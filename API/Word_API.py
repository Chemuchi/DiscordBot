import json
import os

import requests


# 현재 스크립트 파일의 경로를 얻습니다.
script_dir = os.path.dirname(os.path.abspath(__file__))
# 상위 폴더의 경로를 얻습니다.
parent_dir = os.path.dirname(script_dir)
# config.json 파일의 경로를 생성합니다.
config_path = os.path.join(parent_dir, 'config.json')

# 파일을 읽어올 때 config_path를 사용합니다.
with open(config_path, 'r') as f:
    config = json.load(f)

key = config["word_token"]["token"]

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
