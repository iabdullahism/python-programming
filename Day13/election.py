import pandas as pd
import numpy as np
dataset=pd.read_csv("election.csv")
"""
1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country
"""

"""
1. Fetch the top parties of each state within each constituency with their vote %.

"""
df=dataset[['State','%','Party','Constituency']]
state=list(df['State'].unique())

data=pd.DataFrame()

print("top party name in each state according with their vote")
for i in state:
	
	m=df[df['State']==i].sort_values(by='%',ascending=[False])
	print(list(m.iloc[0,:].values))

	
"""
2. Visualize the top parties vote % in each constituency for Rajasthan.
"""	
print("top party name in each city of rajasthan according with their vote")

Rajasthan=df[df['State']=='Rajasthan']
cityInRajasthan=list(Rajasthan['Constituency'].unique())

for topParties in cityInRajasthan:
	p=Rajasthan[Rajasthan['Constituency']==topParties].sort_values(by='%',ascending=[False])
	print(list(p.iloc[0,:].values))


"""
3. Visualize the total seats gained by each party in each states.
"""

for name in state:	
	p=df[df['State']==name]
	q=p.groupby('Party')['%'].sum()
	print('state=',name,'**********')
	print("party name and seat gain")    
	print(q)

"""
4. Visualize the total seats won by the parties in the whole country
"""

q=dataset.groupby('Party')['SN'].sum()
print(q.sort_values(ascending=[False]))































