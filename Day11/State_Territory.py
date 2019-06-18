
"""
Code Challenge ( Pie Chart )

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 

Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

import requests
import pandas as pd
from bs4 import BeautifulSoup as BS
from collections import OrderedDict
import csv
import matplotlib.pyplot as plt

url="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source=requests.get(url).text
soup=BS(source,"lxml")
#source data pass into beautifull pass for scrapping
table=soup.find('table', class_='wikitable sortable')

#find mathod first occerence using thie classname,div,and many more...
state=[]
share=[]

for row in table.findAll('tr'):
    cells = list(row.findAll('td'))
    if(len(cells)==7):
        state.append(cells[1].text.strip())
        share.append(cells[4].text.strip())
    
    
#if we want to store data into csv file then    
col_name = ["State or UN","Share"]
col_data = OrderedDict(zip(col_name,[state,share]))
df = pd.DataFrame(col_data) 
df.to_csv("State_Territory.csv")

#this is work to take data into table and store into csv file

#for sort top 10 data use dict to sort
dict_data={}
i=0
while(i<len(state[:-2])):
    dict_data[state[i]]=float(share[i])
    i=i+1
    
sort_list=sorted(dict_data.items(),key=lambda x:x[1])   
top_six_state=[]
National_share=[]
for top_state in sort_list[-6:]:
    top_six_state.append(top_state[0])
    National_share.append(top_state[1])



explode = (0, 0, 0, 0,0,0.2)  # explode 1st slice to 10% of the radius
plt.pie(National_share, explode=explode,labels=top_six_state, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#here auto pact use round offf function




