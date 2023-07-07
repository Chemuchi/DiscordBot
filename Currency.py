import requests
from lxml import html


def US():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8B%AC%EB%9F%AC+%ED%95%9C%EC%9C%A8'
    response = requests.get(url)
    tree = html.fromstring(response.text)
    element = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/section[2]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')[0]
    D = float(element.text.replace(',', ''))

    return D
def JP():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%94%ED%99%94+%ED%99%98%EC%9C%A8'
    response = requests.get(url)
    tree = html.fromstring(response.text)
    element = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')[0]
    Y = float(element.text.replace(',', ''))

    return Y
def EU():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9C%A0%EB%A1%9C+%ED%99%98%EC%9C%A8'
    response = requests.get(url)
    tree = html.fromstring(response.text)
    element = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')[0]
    R = float(element.text.replace(',', ''))

    return R
def TR():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%84%B0%ED%82%A4+%ED%99%98%EC%9C%A8'
    response = requests.get(url)
    tree = html.fromstring(response.text)
    element = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')[0]
    Y = float(element.text.replace(',', ''))

    return Y
def GB():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%EA%B5%AD+%ED%99%98%EC%9C%A8'
    response = requests.get(url)
    tree = html.fromstring(response.text)
    element = tree.xpath('/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')[0]
    P = float(element.text.replace(',', ''))

    return P