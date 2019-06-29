"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption
 in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower",
	"weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the
	 two is more accurate in predicting the MPG value
	 
	 
	 
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs 
	with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 
	horsepower engine giving it a displacement of about 215. 
	(Give the prediction from both the models)




"""


import pandas as pd
import numpy as np
column_name=['Mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','car name']

dataset=pd.read_fwf("Auto_mpg.txt",header=None,names=column_name)

features=dataset.iloc[:,1:-1]
labels=dataset.iloc[:,0].values
#first check dataset contains the null values or not
dataset.isnull().any(axis=0)
#preproccessing method
#1.check label encoding
#2.decimal scalling

#replace ? in mean values
features['horsepower']=features['horsepower'].replace('?',np.NaN).astype(np.float64)
features['horsepower']=features['horsepower'].fillna(features['horsepower'].mean())
features=np.array(features)


#now standerd scalling

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)

#now model training
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.2,random_state=0)


#now apply decision tree model 
"""
this problem is regression problem because mpg is a value continues
in regression not use confusion matrix
"""
from sklearn.tree import DecisionTreeRegressor
dt= DecisionTreeRegressor()
dt.fit(features_train,labels_train)
labels_pred = dt.predict(features_test) 
print(pd.DataFrame({'predicated':labels_pred,'actual':labels_test}))












 """
Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs 
with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 
horsepower engine giving it a displacement of about 215. 
(Give the prediction from both the models)

"""

"""
find mpg
model_year=80
origin=3
weight=2630
cylender=6
accelartion=22.2
hp=100
displacement=215
"""
car_data=[6,215,100,2630,22.2,80,3]
#convert if label encoder but here use only decimal scalling
car_data1=np.array(car_data).reshape(1,-1)
car_data1=sc.transform(car_data1)

labels_pred1 = dt.predict(car_data1)


print("this predict merital affair is zero",labels_pred1)

















