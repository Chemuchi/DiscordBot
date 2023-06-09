from selenium import webdriver
from selenium.webdriver.common.by import By


def US():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%8B%AC%EB%9F%AC+%ED%95%9C%EC%9C%A8')
    element = driver.find_element(By.XPATH, '//*[@id="_cs_foreigninfo"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')
    D = float(element.text.replace(',',''))

    return D
def JP():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%97%94+%ED%99%98%EC%9C%A8')
    element = driver.find_element(By.XPATH, '//*[@id="_cs_foreigninfo"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')
    Y = float(element.text.replace(',',''))

    return Y
def EU():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9C%A0%EB%A1%9C+%ED%99%98%EC%9C%A8')
    element = driver.find_element(By.XPATH,'//*[@id="_cs_foreigninfo"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')
    E = float(element.text.replace(',', ''))

    return E
def TR():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%8A%80%EB%A5%B4%ED%82%A4%EC%98%88+%ED%99%98%EC%9C%A8')
    element = driver.find_element(By.XPATH,'//*[@id="_cs_foreigninfo"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')
    Y = float(element.text.replace(',', ''))

    return Y
def GB():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%EA%B5%AD+%ED%99%98%EC%9C%A8')
    element = driver.find_element(By.XPATH,'//*[@id="_cs_foreigninfo"]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/h3/a/span[2]/strong')
    P = float(element.text.replace(',', ''))

    return P