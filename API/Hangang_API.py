import requests, json

def hangang_temp():
    response = requests.get('https://api.hangang.msub.kr/')
    data = json.loads(response.text)
    temp = data['temp']
    return temp