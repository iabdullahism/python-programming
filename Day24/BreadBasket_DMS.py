
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has 
data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support 
should be 0.0025, min_confidence=0.2, min_lift=3.0
3. Out of given results sets, show only names of the 
associated item from given result row wise.

"""

import numpy as np
import pandas as pd

dataset=pd.read_csv("BreadBasket_DMS.csv")
#check is null values or not
dataset.isnull().any(axis=0)

from matplotlib import pyplot as plt
top_item=dataset['Item'].value_counts().head(15)

item_name=list(top_item.index)
sell_count=list(top_item.values)


"""
#1. Draw the pie chart of top 15 selling items.
"""
explode=list(np.zeros(14,dtype=np.int16))

plt.pie(sell_count,labels=item_name,autopct="%.0f%%")
plt.show()


"""

2. Find the associations of items where min support 
should be 0.0025, min_confidence=0.2, min_lift=3.0

"""

from apyori import apriori
transactions = []

#here we only use transection and items
#so i will make a new dataset which contain these item only
dataset1=dataset[['Transaction','Item']]



for i in range(1,len(dataset1)):
	p=dataset1[dataset1['Transaction']==i]
	if(len(p!=0)):
		q=list(p.iloc[:,1])
		transactions.append(q)


#here we are using only
# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
#rules is type of genertor
# Visualising the results
results = list(rules)




"""
3. Out of given results sets, show only names of the 
associated item from given result row wise.
"""
i=0
while(i<len(results)):
	print(results[i][0])
	i+=1


















