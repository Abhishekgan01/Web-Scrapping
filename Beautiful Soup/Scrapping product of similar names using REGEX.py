import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computer/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag=soup.find_all(string ="Galaxy Tab") #Extracting the number of galaxy tabs
print((tag))

tag=soup.find_all(string =re.compile("Galaxy Tab")) #Extracting all the product that contains Galaxy Tabs
print((tag))