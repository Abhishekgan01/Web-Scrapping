import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://ticker.finology.in/"
r =requests.get(url)

soup = BeautifulSoup(r.text,"lxml")
table=soup.find("table",class_="table table-sm table-hover screenertable")
headers = table.find_all("th")

titles=[]
for i in headers:
    titles.append(i.text.strip())
#print(titles)

df = pd.DataFrame(columns=titles)

rows = table.find_all("tr")

for i in rows[1:]:
    data =i.find_all("td")
    row=[tr.text.strip() for tr in data]
    print(row)

    l=len(df)
    df.loc[l] = row

print(df)
