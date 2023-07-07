import json
import urllib.request

from tokenp import *

client_id = NaverClientID() # 개발자센터에서 발급받은 Client ID 값
client_secret = NaverClientSecret() # 개발자센터에서 발급받은 Client Secret 값

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