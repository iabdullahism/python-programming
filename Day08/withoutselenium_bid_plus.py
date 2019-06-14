#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 09:12:54 2019

@author: rahul
"""


"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
      
      div="//*[@id="pagi_content"]"

"""

bid_no=[]
item_name=[]
department_name=[]
date=[]
from bs4 import BeautifulSoup
import requests
from collections import OrderedDict

#specify the url
url = "https://bidplus.gem.gov.in/bidlists"

source = requests.get(url).text

soup = BeautifulSoup(source,"lxml")
#pass the data into beautiful by method lxml
right_table=soup.findAll('div', class_='border block')

for row in right_table:
      # first row has no TH, but other rows have one TH and 6 TD
    cells = row.find('div', class_='block_header') 
    # first row has 7 TH 
    detail = row.findAll('div', class_='col-block')
    bid_no.append(cells.p.text.strip())
    item_name.append(detail[0].text.strip())
    department_name.append(detail[1].text.strip())
    date.append(detail[2].text.strip())
   


col_name = ["bid_no","item_name","department_name","date"]
col_data = OrderedDict(zip(col_name,[bid_no,item_name,department_name,date]))
#pandas library is used to convert dictonary and row data into table format    
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("gem.csv")
