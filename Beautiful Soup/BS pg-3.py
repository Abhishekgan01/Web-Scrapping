import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
tag=soup.header.div.a.button.span
print(tag.string)