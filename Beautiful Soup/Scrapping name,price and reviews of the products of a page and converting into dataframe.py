import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

product_name=[]
product_price=[]
product_reviews=[]

url = "https://webscraper.io/test-sites/e-commerce/allinone/computer/tablets"
r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml")

pro_name=soup.find_all("a",class_="title") 
for i in pro_name:
    product_name.append(i.text)

pro_price=soup.find_all("h4",class_="price float-end card-title pull-right")
for i in pro_price:
    product_price.append(i.text)

pro_reviews = soup.find_all("p",class_="review-count float-end")
for i in pro_reviews:
    product_reviews.append(i.text)

df = pd.DataFrame({"Product Name":product_name, "Product Price":product_price, "Product Reviews": pro_reviews})
print(df)