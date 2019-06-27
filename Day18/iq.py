
"""

Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or 
her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

    What is the IQ of an individual with a given brain size of 90, height
	 of 70 inches, and weight 150 pounds ? 
    Build an optimal model and conclude which is more useful in predicting
	 intelligence Height, Weight or brain size.

"""
#this question is based on backward eluminition
import pandas as pd
import numpy as np
dataset=pd.read_csv("iq_size.csv")
labels=dataset.iloc[:,0].values
features=dataset.iloc[:,1:].values
# Building the optimal model using Backward Elimination

#import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for
# constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.

import statsmodels.api as sm
features = sm.add_constant(features)
#those work we are doing linearregression this can be done by using sm 
#but there y=ax+by+c than c is constant because here multiply is 1
# so linear regression method by default create a 1's column but in 
#sm model diffrent it called that you add 1's column yourself
# then i'am predicting the values
#sm is mainly use for there are multiple columns but its choose those column 
#who really effect of predicted model this take a criteria p values if 
# if p values is 5% then it taken otherwise remove from column
#sm method have property .add_constant to add column 1's in dataset


#feature takes the new column for again and again predict p values
# and remove the column according p values
#sm method use endog and exog to fit the dataset
features_opt = features[:, [0, 1, 2, 3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.pvalues
#now we takes that p>|t|  for x3 0.998% so we remove its
#and again predict

features_opt = features[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary() 
# the constant data cloumns have greater 5% p values then we romve it
#this process

features_opt = features[:, [1, 2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary() 
# the constant x[2] data cloumns have greater 5% p values then we romve it
#this process

features_opt = features[:, [1]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary() 