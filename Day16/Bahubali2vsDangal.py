

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Bahubali2_vs_Dangal.csv")
#reshape creates 2d array
features = dataset.iloc[:, 0].values.reshape(-1,1) 
labels1 = ((dataset.iloc[:, 1].values).reshape(-1,1))
labels2 = ((dataset.iloc[:, 2].values).reshape(-1,1))
labels3 = dataset.iloc[:, 1:3].values
#labels3 is also 2d array
#Check if any NaN values in dataset
dataset.isnull().any(axis=0)


plt.boxplot(dataset.values)
plt.show()
#let's plot our data points on 2-D graph to eyeball our dataset 
# and see if we can manually find any relationship between the data. 
#dataset.plot(x='Population', y='Profit', style='o')  
plt.scatter(labels1,features,color='green')
plt.scatter(labels2,features)
plt.title('company profit in city')  
plt.xlabel('city population')  
plt.ylabel('profit')  
plt.show()


"""
train the model now 
"""

from sklearn.linear_model import LinearRegression  
#make a object of LinearRegression() class
#and predict train the model using fit method
regressor = LinearRegression()  
regressor.fit(features, labels1)
regressor.fit(features, labels2)  
regressor.fit(features, labels3)

print(regressor.intercept_)  
print (regressor.coef_)


#here 2d array work that means model read the data fist rows second rows 
#so make a 2d array of value which we want to predict
x=np.array(10).reshape(-1,1)
print ("prediction of bahubali",regressor.predict(x)[0][0])


y=np.array(10).reshape(-1,1)
print ("prediction of Dangal",regressor.predict(y)[0][0])

"""
2nd     Second Approach - Create one model with two labels
"""

z=np.array(10).reshape(-1,1)
print ("prediction of both data",regressor.predict(z)[0][0])


