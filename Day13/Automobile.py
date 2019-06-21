"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np
Automobile=pd.read_csv("Automobile.csv")
"""
#handle missing value in price 
#fill avarage value in price

#df['salary'] = df['salary'].replace(0, np.NaN)
check missing value in perticular column
Automobile[Automobile['price'].isnull()]
total = Automobile.isnull().sum(axis=0).sort_values(ascending=False)
"""
Automobile['price'] = Automobile['price'].fillna(Automobile['price'].mean())
#create a series into ndarray
price_array=np.array(Automobile['price'])
print("Avarage price=",np.mean(price_array))
print("standard daviation =",np.std(price_array))
print("minimum value from price=",np.min(price_array))
print("max value from price=",np.max(price_array))



