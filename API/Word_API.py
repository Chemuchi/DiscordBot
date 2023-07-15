import requests
import json

from tokens import Word_API

key = Word_API()

def word(text):
    definitions = []
    response = requests.get(f"https://stdict.korean.go.kr/api/search.do?certkey_no=5650&key={key}&type_search=search&req_type=json&q={text}")
    data = json.loads(response.text)
    items = data['channel']['item']
    for item in items:
        definition = item['sense']['definition']
        definitions.append(definition)

    return definitions

'''a = input()
b = word(a)
for i, definition in enumerate(b):
    print(f"{i+1}. {definition}")'''