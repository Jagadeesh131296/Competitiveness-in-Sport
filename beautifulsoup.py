# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 21:00:52 2022

@author: jagan
"""
#Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import dateutil
import pandas as pd

#Requesting url
result = requests.get("https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=14452;type=tournament")
# assert result.status_code==200  
src = result.content
document = BeautifulSoup(src, 'lxml')
table = document.find("table")
assert table.find("th").get_text() == "Player"
rows = table.find_all("tr")  # Note: this works because find_all is resursive by default    
#Created a array 
ar =[]
#Created a for loop to go through all the rows of the table
for row in rows[1:]:
    cells = row.find_all(["td", "th"])
    
    cells_text = [cell.get_text(strip=True) for cell in cells]
    print(cells_text)
    ar.append(cells_text)
    
#Created a dataframe 
df = pd.DataFrame(ar)
# adding column name to the respective columns
df.columns =['Player','Mat','Inns','NO','Runs','HS','Ave','BF','SR','100','50','0','4s','6s']
# displaying the DataFrame
print(df)

#df.to_csv('iplbattingaverage_2021season.csv')