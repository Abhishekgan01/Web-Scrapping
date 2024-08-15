from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/abhis/OneDrive/Desktop/Selenium/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
driver.save_screenshot("C:/Users/abhis/OneDrive/Desktop/Selenium/full-page.png")