import requests
from setting import word_token

def word(word):
    definitions = []
    url = 'https://stdict.korean.go.kr/api/search.do'
    params ={
        "key" : word_token(),
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
