
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
  driver="/home/rahul/Desktop/FSDP2019/Day08"
"""
bid_no=[]
item_name=[]
department_name=[]
date=[]
import csv
from collections import OrderedDict
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
url = "https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Firefox(executable_path="/home/rahul/Desktop/FSDP2019/Day08/geckodriver")
driver.get(url)
# Opening the submission url
 
sleep(2)

get_pdf_file = driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/p[1]')
get_pdf_file.click()

sleep(2)
#page source technique used to get source of the page
html_page = driver.page_source
#when the html_page pass in soup the data is scrapping
soup = BeautifulSoup(html_page,"lxml")
data_table=soup.findAll('div', class_='border block')

for row in data_table:
    cells = row.find('div', class_='block_header') 
    # first row has 7 TH 
    detail = row.findAll('div', class_='col-block')
    bid_no.append(cells.p.text.strip(""))   
    item_name.append(detail[0].p.text.strip(""))
    department_name.append(detail[1].text.strip("\n"))
    date.append(detail[2].text.strip("\n"))



col_name = ["bid_no","item_name","department_name","date"]
col_data = OrderedDict(zip(col_name,[bid_no,item_name,department_name,date]))
#pandas library is used to convert dictonary and row data into table format    
df = pd.DataFrame(col_data) 
df.to_csv("gemselenium.csv",index=False)


with open("gemselenium.csv") as file:
    read_file=csv.reader(file,delimiter=",")
    for data in read_file:
        print(data)

