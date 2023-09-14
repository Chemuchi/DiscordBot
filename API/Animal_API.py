import requests, json

def cat():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = json.loads(response.text)
    return data[0]['url']
def dog():
    response = requests.get('https://api.thedogapi.com/v1/images/search')
    data = json.loads(response.text)
    return data[0]['url']

