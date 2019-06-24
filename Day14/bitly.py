
"""
Code Challenge
  Name: 
    URL shortening service Bitly
  Filename: 
    bitly.py
  Problem Statement:
    (usagov_bitly_data.json)
    In 2011, URL shortening service Bitly partnered with the US government website
    USA.gov to provide a feed of anonymous data gathered from users who shorten links
    ending with .gov or .mil. 
    In 2011, a live feed as well as hourly snapshots were available
    as downloadable text files. 
    This service is shut down at the time of this writing (2017),
    but we preserved one of the data files.
    In the case of the hourly snapshots, each line in each file contains a common form of
    web data known as JSON. (Use usagov_bitly_data.txt file from Resources)

    Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
   
    Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
  
  Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
  
    From field 'a' which contains browser information and separate out browser capability
	(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot
	 bar graph for top 5 values (using Seaborn)
	 
    Add a new Column as 'os' in the dataset, separate users by 'Windows' for the 
	values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't

Hint:
    http://1usagov.measuredvoice.com/2011/
    
"""
item=[]
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
with open("usagov_bitly_data.json", "r") as read_file:
	jsondata=read_file.readlines()
	for data in jsondata:
	 item.append(json.loads(data))
#jsondata is a list we canot read it
#the data is a string and in string a dictonary we take data as a dictnarry then first we convert
#data into dictonary
#the create a list of dictonary
#=insert the list into the dataframe	 
df=pd.DataFrame(item)	 
"""
   1. Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
"""
df['al'] = df['al'].replace(np.NaN,'Unknown')
df['c'] = df['c'].replace(np.NaN,'Unknown')
df['cy'] = df['cy'].replace(np.NaN,'Unknown')
df['kw'] = df['kw'].replace(np.NaN,'Unknown')
df['gr'] = df['gr'].replace(np.NaN,'Unknown')
df['tz']=df['tz'].replace('','Unknown')
"""
   2- Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    Count the number of occurrence for each time-zone
"""
time_zone=df['tz'].value_counts()
#top 10 most time zone
time_zone[1:11]

"""
 3- Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
"""
freq=list(time_zone[1:11])
zone=list(time_zone[1:11].index)
index=list(range(10))
plt.bar(index,freq,label="top 10 time-zones")
plt.xlabel("zone name")
plt.ylabel("frequency")
plt.xticks(index,zone,rotation=-90)
plt.legend()
plt.show()

"""

    From field 'a' which contains browser information and separate out browser capability
	(i.e. the first token in the string eg. Mozilla/5.0)
    Count the number of occurrence for separated browser capability field and plot
	 bar graph for top 5 values (using Seaborn)
	 
"""
browser=df['a'].value_counts()
browser_name=list(browser[0:5].index)
accurance=list(browser[0:5])
index=list(range(5))
plt.bar(index,accurance,label="top 10 time-zones")
plt.xlabel("browser name")
plt.ylabel("frequency")
plt.xticks(index,browser_name,rotation=-90)
plt.legend()
plt.show()

"""
  Add a new Column as 'os' in the dataset, separate users by 'Windows' for the 
	values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" for those who don't
"""

df['os']=df['a'].map(lambda x: 'Window user' if (x.find('Windows')!=-1) else 'Not Windows')

df['os'].value_counts()


