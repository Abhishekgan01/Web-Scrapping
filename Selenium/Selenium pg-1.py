from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("D:/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = s)
driver.get("https://www.wscubetech.com/")