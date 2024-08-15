import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag = soup.header
#print(tag.attrs)
atb = (tag.attrs)
print(atb['class'])