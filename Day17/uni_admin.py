"""

Code Challenges:
    Name:
        University Admission Prediction Tool
    File Name:
        uni_admin.py
    Dataset:
        University_data.csv
    Problem Statement:
         Perform Linear regression to predict the chance of admission based on all the features given.
         Based on the above trained results, what will be your estimated chance of admission.

"""
import numpy as np
import pandas as pd

dataset=pd.read_csv("University_data.csv")
features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1]
#this features is not open because it is array of object so convert the 
#catagorical data

#now next step is check is any missing data or not
dataset.isnull().any(axis=0)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
#LabelEncoder is a class we make a object of this class
labelencoder = LabelEncoder()
features[:, 0] = labelencoder.fit_transform(features[:, 0])
#fit_transform method first its convert into 0,1,2,3 format

from sklearn.preprocessing import OneHotEncoder
#OneHotEncoder is a class
onehotencoder = OneHotEncoder(categorical_features = [0])
#categorical_features = [0] takes only first column 
#onehotencoder.fit_transform method convert 
#1 0 0 0 0
#0 1 0 0 0
#0 0 1 0 0
#this format type that means no catgorical datatype has high prirrity
features = onehotencoder.fit_transform(features).toarray()
#if we a 4 columns data then we can find 5th column data so we remove first coliumn
# of 1 or 0 type for space reduce

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
#we take test_size=.2 that means 20% data for test and 80% data for  training model 
#this can be done by (train_test_split) method
# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
#import LinearRegression classs
regressor = LinearRegression()
# make the object of this class
regressor.fit(features_train, labels_train)
#now train the model

#multiple regression types y=ax+by+cz+d types
# Predicting the Test set results
Pred = regressor.predict(features_test)
prediction=pd.DataFrame(Pred,labels_test)
#here labels_test work as index
print (prediction)


# Prediction for a new values 
# make this accorifng to the data csv
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap
"""
import numpy as np
x = [0,0, 1500, 1, 2]
x = np.array(x)
x = x.reshape(1,5)
#make 2d array
regressor.predict(x)



le = labelencoder.transform(['Development'])
ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
x = [ohe[0][1],ohe[0][2],1100,1,3]
x = np.array(x)


regressor.predict(x.reshape(1, -1))
"""

Score1 = regressor.score(features_train, labels_train)
Score2 = regressor.score(features_test, labels_test)

print("train model is greater than train model")














