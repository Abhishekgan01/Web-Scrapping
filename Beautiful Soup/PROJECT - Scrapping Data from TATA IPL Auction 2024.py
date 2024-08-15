import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction"
r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")
table=soup.find("table",class_="ih-td-tab auction-tbl")

titles=[]
header = table.find_all("th")
for i in header:
    titles.append(i.text.strip())

df = pd.DataFrame(columns=titles)
#print(df)

data = table.find_all("tr")
#print(data)

for i in data[1:]:
    rows=i.find_all("td")
    row_data=[tr.text.strip() for tr in rows]
    print(row_data)

    l=len(df)
    df.loc[l] = row_data

print(df)

"""  Output
['Chennai Super Kings', '₹1,00,00,000', '8', '25']
['Delhi Capitals', '₹9,90,00,000', '8', '25']
['Gujarat Titans', '₹7,85,00,000', '8', '25']
['Kolkata Knight Riders', '₹1,35,00,000', '8', '23']
['Lucknow Super Giants', '₹95,00,000', '8', '25']
['Mumbai Indians', '₹1,05,00,000', '8', '25']
['Punjab Kings', '₹4,15,00,000', '8', '25']
['Rajasthan Royals', '₹20,00,000', '8', '22']
['Royal Challengers Bengaluru', '₹2,85,00,000', '8', '25']
['Sunrisers Hyderabad', '₹3,20,00,000', '8', '25']

                TEAM            FUNDS REMAINING    OVERSEAS PLAYERS TOTAL PLAYERS
0          Chennai Super Kings    ₹1,00,00,000                8            25
1               Delhi Capitals    ₹9,90,00,000                8            25
2               Gujarat Titans    ₹7,85,00,000                8            25
3        Kolkata Knight Riders    ₹1,35,00,000                8            23
4         Lucknow Super Giants      ₹95,00,000                8            25
5               Mumbai Indians    ₹1,05,00,000                8            25
6                 Punjab Kings    ₹4,15,00,000                8            25
7             Rajasthan Royals      ₹20,00,000                8            22
8  Royal Challengers Bengaluru    ₹2,85,00,000                8            25
9          Sunrisers Hyderabad    ₹3,20,00,000                8            25
"""