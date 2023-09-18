import urllib.request
import json
from setting import naver_clientsec, naver_clientid



client_id = naver_clientid()
client_secret = naver_clientsec()

def detect_language(text):
    encQuery = urllib.parse.quote(text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        return result['langCode']
    else:
        print("Error Code:" + rescode)

def translate(text, target_lang):
    source_lang = detect_language(text)
    encText = urllib.parse.quote(text)
    data = f"source={source_lang}&target={target_lang}&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode("utf-8"))
        return (result['message']['result']['translatedText'])
    else:
        return("Error Code:" + rescode)

def dic(text):
    encText = urllib.parse.quote(text)
    url = "https://openapi.naver.com/v1/search/encyc.json?query=" + encText  # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200) :
        response_body = response.read()
        data = json.loads(response_body.decode('utf-8'))
        items = data['items']
        min_description = min(items, key=lambda x: len(x['description']))
        return min_description['description']
    else :
        return("Error Code:" + rescode)

def short_url(text):
    encText = urllib.parse.quote(text)
    data = "url=" + encText
    url = "https://openapi.naver.com/v1/util/shorturl"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200) :
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        return (result['result']['url'])
    else :
        print("Error Code:" + rescode)
