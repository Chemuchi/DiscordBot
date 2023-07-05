'''import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def temp():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://hangang.ivlis.kr/')
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//*[@id="dgr"]')
    text = element.text
    return text
'''