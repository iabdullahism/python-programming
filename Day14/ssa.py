"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year (use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     	
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
df=pd.DataFrame()
path=os.listdir('//home/rahul/Desktop/FSDP2019/Day14/baby_names')
for data in path:
	df1=pd.DataFrame()
	if(data[-4:]=='.txt'):
		with open(data,"rt") as file:
			file_read=file.readlines()
			df1[data] =file_read
	df=pd.concat([df,df1],axis=1)
	
"""
    Display the top 5 male and female baby names of 2010
"""
# first handle the nan value'
df = df.fillna(0)

p=list(df['yob2010.txt'])
name=[]
birth=[]
sex=[]

for data in p:
	if(data!=0):
		q=data.split(",")
		name.append(q[0])
		sex.append(q[1])
		birth.append(int(q[2].strip()))
#create a rows in dataframe using append
df2=pd.DataFrame()	
df3=pd.DataFrame()
df4=pd.DataFrame()
df2['name']=name	
df3['birth']=birth
df4['sex']=sex
df=pd.concat([df,df2],axis=1)	
df=pd.concat([df,df3],axis=1)	
df=pd.concat([df,df4],axis=1)	
		

#customer_concern= df[df['churn_binary'] == 1 ][['customer service calls','churn_binary']]

m= df[['name','sex','birth']].sort_values( by='sex', ascending = [False])
print("2010 top 5 males person name age and sex")
print(m.head())

f= df[['name','sex']].sort_values( by='sex', ascending = [True])
print("2010 top 5 females person name age and sex")
print(f.head())




male_birth= df[df['sex'] == 'M' ][['sex','birth']]
female_birth= df[df['sex'] == 'F' ][['sex','birth']]

slices=[sum(male_birth.iloc[:,1]),sum(female_birth.iloc[:,1])]
label=["male","female"]
plt.pie(slices,labels=label,autopct="%.0f%%")
plt.show()









