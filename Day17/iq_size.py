"""
Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 
Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ?

#sample code is also attached
"""
import pandas as pd
import numpy as np
dataset=pd.read_csv("iq_size.csv")
#iq is labels and all data are features
labels=dataset.iloc[:,0] 
features=dataset.iloc[:,1:]

#Check if any NaN values in dataset
dataset.isnull().any(axis=0)

# not have any categorical data we canot ...
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)
#there are features value that have crossponnding a,,b,c,d corf_
# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))

#accuracy of my data
Score1 = regressor.score(features_train, labels_train)
Score2 = regressor.score(features_test, labels_test)

"""
What is the IQ of an individual with a given brain size of 90,
 height of 70 inches, and weight 150 pounds ?

"""
#x=['brain','height','weight']
x=[90,70,150]
x=np.array(x).reshape(1,3)
print(regressor.predict(x))