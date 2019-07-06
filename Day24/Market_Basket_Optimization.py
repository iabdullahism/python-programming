
"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values 
before fitting the data to model, 
remove the null values from each row and perform the 
associations once again.
Also draw the bar chart of top 10 edibles.

"""

import pandas as pd
import numpy as np
dataset=pd.read_csv("Market_Basket_Optimisation.csv")


from apyori import apriori
transactions = []

for i in range(0, len(dataset)):
	p=dataset.iloc[i].dropna(axis=0)
	q=list(p)
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
	transactions.append(q)




# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
results = list(rules)















