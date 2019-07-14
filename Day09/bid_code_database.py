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
    department_name.append(detail[1].text.strip("\n"))
    date.append(detail[2].text.strip("\n"))
    
    
    
conn = mysql.connector.connect(user='rahulpandit', password='rahulpandit123',
                              host='db4free.net', database = 'roomseeker')
c = conn.cursor()
c.execute("Drop table Gem_data;")

c.execute ("""CREATE TABLE Gem_data(
          id INTEGER,
          bid_no  TEXT,
          item_name TEXT,
          department_name TEXT,
          date Text
          )""")  




i=0
while(i<len(bid_no)):
    p=bid_no[i]
    q=item_name[i]
    r=department_name[i]
    s=date[i]
    c.execute("INSERT INTO Gem_data VALUES ({},'{}', '{}', '{}','{}')".format(i,bid_no[i],item_name[i],department_name[i],date[i]))
    i=i+1 
conn.commit()

c.execute("SELECT * FROM Gem_data")
data=c.fetchall()
for value in data:
    print(value[3])





