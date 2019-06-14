"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


     

"""
s_no=[]
team=[]
weighted_match=[]
point=[]
rating=[]
#start of data scraping using beautifulsoup
import requests
from bs4 import BeautifulSoup as BS
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
data=requests.get(url).text
#request method get data using url
soup=BS(data,"lxml")
#beautiful soup use to scrap the data
html_data=soup.find('tbody')
#tbody is unique so find method use
row=html_data.findAll('tr')
#in tbody there are many tr so i use findall and make list
for i in row:
   j=i.findAll('td')
   s_no.append(j[0].text.strip())   
   team.append(j[1].text.strip())
   weighted_match.append(j[2].text.strip())
   point.append(j[3].text.strip())
   rating.append(j[4].text.strip())
   
#end of data scrapping   
import mysql.connector 
import dns
import pymongo
client = pymongo.MongoClient("mongodb+srv://rahulpandit:rahulpandit123@cluster0-e2nbu.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.icc_cricket   
   
def insert_icc(sno,team,weight,points,rating):
     mydb.cricket_data.insert_one(
             {
               "s_no":sno,
               "team":team,
               "weighted_match":weight,
               "points":points,
               "rating":rating
                     
             })
     return "Employee added successfully"
            
i=0
while(i<len(s_no)):
    insert_icc(s_no[i],team[i],weighted_match[i],point[i],rating[i])
    i+=1
