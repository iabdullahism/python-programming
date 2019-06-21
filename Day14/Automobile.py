
"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import pandas as pd
from matplotlib import pyplot as plt 
from collections import OrderedDict
df=pd.read_csv("Automobile.csv")
p=df.groupby(['make']).apply(lambda x: len(x))
car_name=list(p.index[:])
car_makers=list(p.values[:])
dict_data = OrderedDict(zip(car_name,car_makers))
dict1=sorted(dict_data.items(),key=lambda x:x[1])
#take last 10 values in list
label=[]
index=[]
length=len(dict1)
i=length-1
while(i>=length-10):
	label.append(dict1[i][0])
	index.append(dict1[i][1])
	i=i-1
explode=(.2,0,0,0,0,0,0,0,0,0)
plt.pie(index,labels=label,autopct="%.0f%%",explode=explode)
plt.show()