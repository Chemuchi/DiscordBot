from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def temp():
    driver = webdriver.Edge("\msedgedriver.exe")
    driver.get('https://hangang.ivlis.kr/')
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id="dgr"]')
    text = element.text
    return text
