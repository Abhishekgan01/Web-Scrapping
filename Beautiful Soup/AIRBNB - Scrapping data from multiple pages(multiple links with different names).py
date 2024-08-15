import requests
from bs4 import BeautifulSoup
import pandas as pd

Names=[]
Price=[]
Description=[]
Reviews=[]

url="https://www.airbnb.co.in/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wll&refinement_paths%5B%5D=%2Fhomes"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")
#print(soup)

for i in range(1,14):
    np = soup.find("a",class_="_1bfat5l").get("href")
    cnp = "https://www.airbnb.co.in"+np
    print(cnp)

    url=cnp
    r=requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")

    names=soup.find_all("div",class_="t1jojoys dir dir-ltr")
    for i in names:
        Names.append(i.text)
    #print(names)

    prices=soup.find_all("span",class_="a8jt5op dir dir-ltr")
    for i in prices:
        Price.append(i.prices)
    #print(prices)
    
    desc=soup.find_all("div",class_="nguyp1l s1cjsi4j dir dir-ltr")
    for i in desc:
        Description.append(i.text)
    #print(desc)

    reviews= soup.find_all("span",class_="r1dxllyb dir dir-ltr")
    for i in reviews:
        Reviews.append(i.text)
    #print(reviews)

df = pd.DataFrame({"Name":Names, "Prices":Price, "Description":Description, "Reviews":Reviews})
print(df)