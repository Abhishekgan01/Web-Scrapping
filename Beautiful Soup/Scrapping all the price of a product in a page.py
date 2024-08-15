import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag=soup.find_all("h4",class_="price float-end card-title pull-right")
print(len(tag))

for i in tag:
    price = i.text
    print(price)