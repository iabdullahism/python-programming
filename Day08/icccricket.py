"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
#url pass into soyrce 
source = requests.get(url).text
#when the url send using get method and text format bydefault its binary foramt
soup = BeautifulSoup(source,"lxml")
#source data pass into beautifull pass for scrapping
right_table=soup.find('table', class_='table')
#find mathod first occerence using thie classname,div,and many more...
#print(right_table.prettify())
#prettify uses  to  tree fromaat show data
serial=[]
team=[]
weighted_matchs=[]
points=[]
rating=[]

for row in right_table.findAll('tr'):   
     cells = row.findAll('td')
     if len(cells)==5:
            serial.append(cells[0].text.strip())
            team.append(cells[1].text.strip())
            weighted_matchs.append(cells[2].text.strip())
            points.append(cells[3].text.strip())
            rating.append(cells[4].text.strip())

    
    
    
from collections import OrderedDict

col_name = ["serial_no","team","weighted_macth","points","rating"]
col_data = OrderedDict(zip(col_name,[serial,team,weighted_matchs,points,rating]))
    
    
import pandas as pd
import csv
df = pd.DataFrame(col_data) 
df.to_csv("cricket_score.csv",index=False)

with open("cricket_score.csv") as file:
    file_read=csv.reader(file,delimiter=",")
    for row in file_read:
        print ( row )
    

    
    
    
    
    
    
    
    