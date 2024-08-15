import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag=soup.find("h4",class_="price float-end card-title pull-right")
print(tag.string)