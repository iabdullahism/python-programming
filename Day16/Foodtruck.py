
"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    1-You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Foodtruck.csv")
features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)


plt.boxplot(dataset.values)
plt.show()
#let's plot our data points on 2-D graph to eyeball our dataset 
# and see if we can manually find any relationship between the data. 
#dataset.plot(x='Population', y='Profit', style='o')  
plt.scatter(labels,features)
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
regressor.fit(features, labels) 

#To see the value of the intercept and slop calculated by the linear
# regression algorithm for our dataset, execute the following code.
#intercept means c and coef means m   y=mx+c
print("b=",regressor.intercept_)  
print ("a=",regressor.coef_)


#here 2d array work that means model read the data fist rows second rows 
#so make a 2d array of value which we want to predict
x=np.array(3.073).reshape(-1,1)
print ("it may loss=",regressor.predict(x))









