from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

s = Service("C:/Users/abhis/OneDrive/Desktop/Selenium/chromedriver-win32/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.tutorialsfreak.com/")

driver.find_element_by_xpath("""/html/body/div/div[2]/div[2]/section[1]/div/div[1]/div/div/div/div[3]/span/img""").screenshot("C:/Users/abhis/OneDrive/Desktop/Selenium/full-page.png")