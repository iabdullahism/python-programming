"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database on cloud 

"""
bid_no=[]
item_name=[]
department_name=[]
date=[]
import mysql.connector 
from bs4 import BeautifulSoup as bs
import requests
url = "https://bidplus.gem.gov.in/bidlists"
source = requests.get(url).text
soup=bs(source,"lxml")
soup.prettify()
html_data=soup.findAll('div', class_='border block')

for row in html_data:
    cells = row.find('div', class_='block_header') 
    # first row has 7 TH 
    detail = row.findAll('div', class_='col-block')
    bid_no.append(cells.p.text.strip(""))   
    item_name.append(detail[0].p.text.strip(""))
    department_name.append(detail[1].text.replace("\n",""))
    date.append(detail[2].text.strip("\n"))
    
import dns
import pymongo
client = pymongo.MongoClient("mongodb+srv://rahulpandit:rahulpandit123@cluster0-e2nbu.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.gem_data
#gem_data database

#for use mongo db to send data we create our own function and then we can send data

def add_data(idd,bidno,itemname,departname,dat):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.gem.insert_one(
            {
            "id" : idd,
            "bid_no" : bidno,
            "itemname" : itemname,
            "departmentname" : departname,
            "date":dat
            })
    return "Employee added successfully"



i=0
while(i<len(bid_no)):
    add_data(i,bid_no[i],item_name[i],department_name[i],date[i])
    i+=1
    
#and also fetch the data make  function and call mydb.fetchall method