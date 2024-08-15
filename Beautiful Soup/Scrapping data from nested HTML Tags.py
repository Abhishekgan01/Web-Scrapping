import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
r =requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

#navbar=soup.find_all("ul", class_="nav", id="side-menu")[0]
name = soup.find("li", class_="nav-item active")
print(name.text)