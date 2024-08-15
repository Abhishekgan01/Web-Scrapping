import requests
from bs4 import BeautifulSoup
import re

url = "https://webscraper.io/test-sites/e-commerce/allinone/computer/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag=soup.find_all("a",class_="title") 
product_name=[]

for i in tag:
    product_name.append(i.text)

print(product_name)

