
"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght?
   Predict and print it
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
7. In which area code the international plan is most availed?
"""
import pandas as pd
import numpy as np
df=pd.read_csv("Telecom_churn.csv")
"""
1. Predict the count of Churned customer availing both
 voice mail plan and international plan schema
"""

#df_sorted= df.sort_values( by=['international plan','international plan','churn'], ascending = [True,True,True])
#df_sorted.head(10)
#for count we add new column true is 1 and false is 0
df["churn_binary"] = df["churn"].map(lambda x: 1 if x == bool(1) else 0 )
df["voice_binary"] = df["voice mail plan"].map(lambda x: 1 if x =='yes' else 0 )
df["international_binary"] = df["international plan"].map(lambda x: 1 if x =='yes' else 0 )
"""
1-count those churn whose value 1 in all three column that means customer availing both
 voice mail plan and international plan schema
"""
df_sub= df['churn_binary'][(df['churn_binary'] == 1) & \
		           (df['voice_binary'] ==1) & \
                (df['international_binary'] == 1 )
           ].value_counts()
print("1.the value count of churn both in schema=",df_sub.to_list()[0])
		     
"""
2. Total charges for international calls made by 
churned and non-churned customer and visualize it
"""          
#first we multiply total int charge by crossponding its total intl calls
#create  2 ndarray for perform operation
intl_charges=np.array(df['total intl calls'])
intl_call=np.array(df['total intl charge'])
total_intl_charge=sum(intl_charges+intl_call)
print("2.Total charges for international calls=",total_intl_charge)


"""3. Predict the state having highest night call
 minutes for churned customer
"""
day_charge= df[df['churn_binary']==1].sort_values('total night minutes')
day_charge.max()


"""
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
	most popular calls that means total calls in night day and intl
"""
day_call = df[df['churn_binary'] == 1 ][['total day calls','churn_binary']]
sum_day_call=sum(day_call.iloc[:, 0])

night_call = df[df['churn_binary'] == 1 ][['total night calls','churn_binary']]
sum_night_call=sum(night_call.iloc[:, 0])

intl_call = df[df['churn_binary'] == 1 ][['total intl calls','churn_binary']]
sum_intl_call=sum(intl_call.iloc[:, 0])
print("4.a.most popular call of churned users is daya calls=",sum_day_call)

"""
my approch

df.groupby('churn_binary')['total day calls'].sum()
df.groupby('churn_binary')['total eve calls'].sum()
df.groupby('churn_binary')['total night calls'].sum()
df.groupby('churn_binary')['total intl calls'].sum()

"""
"""
    b. the minimum charges among all call type among churned user
"""

day_charge= df[df['churn_binary']==1].sort_values('total day charge')
print(day_charge['total day charge'][day_charge['total day charge']==day_charge['total day charge'].min()])


night_charge= df[df['churn_binary']==1].sort_values('total night charge')
print(night_charge['total night charge'][night_charge['total night charge']==night_charge['total night charge'].min()])

intl_charge= df[df['churn_binary']==1].sort_values('total intl charge')
print(intl_charge['total intl charge'][intl_charge['total intl charge']==intl_charge['total intl charge'].min()])
print("4.b.so the minimum charges among all call type among churned user is day call charge")

"""
5. Which category of customer having maximum account lenght?
   Predict and print it
   """
account_length=df.groupby('churn')[['account length']].max()
customer=account_length.values[:]
print("5.non churn customer having maximum account lenght=",customer[0])

"""
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
"""
#Select salary and sex of only those rows that contain female faculty:
customer_concern= df[df['churn_binary'] == 1 ][['customer service calls','churn_binary']]
customer_concern.head()
if(sum(customer_concern.iloc[:,1])<sum(customer_concern.iloc[:,0])):
	print("6.the total no of churn customer is less their custoemr calls that means thay talk customer care for problem")

"""
7. In which area code the international plan is most availed?
"""


area_code_record=df.groupby(['area code','international plan']).apply(lambda x: len(x))
#for divide the data among male survivde/male dead and female servived/dead
q=list(area_code_record)
print("7. 415-area code the international plan is most availed",q[3])





df.groupby('area code')['international plan'].value_counts()


""""
new logics
1-  
p=df.groupby(['voice_binary','international_binary'])['churn_binary'].value_counts()
"""