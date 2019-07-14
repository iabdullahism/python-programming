
"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students
Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At 
The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors
 (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height
 Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height
 Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""
import numpy as np
import pandas as pd
dataset=pd.read_csv("Female_Stats.csv")
#we will solve this question using backward eluminition
labels=dataset.iloc[:,0].values
features=dataset.iloc[:,1:].values

"""
this problem is baed 
y=ax+[by+cz]
if we change in x in 1 unit then a unit change in y

"""


"""
1.first check if  dataset contain null or missing values
2.second cheeck the dataset have any catagorical data or not
if these contains of the dataset then first remove using preprocessing 
method
"""
import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features[:, [0, 1, 2, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
#regressor_OLS.pvalues

"""
1 .Build A Predictive Model And Conclude If Both Predictors
(Independent Variables) Are Significant For A Students’ Height Or Not
"""
#first takes both data and check
#this method takes 20% data for testing and 80% data for  training
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size = 0.2, random_state = 0)

#we traing the data using 

# Building the optimal model using Backward Elimination

#import statsmodels.formula.api as sm
#This is done because statsmodels library requires it to be done for constants.
#features = np.append(arr = np.ones((30, 1)), values = features, axis = 1)

#adds a constant column to input data set.
import statsmodels.api as sm
features = sm.add_constant(features_train)
"""
add one constant column in feature_train dataset
"""
features_opt = features_train[:, [0, 1, 2]]
regressor_OLS = sm.OLS(endog = labels_train, exog = features_opt).fit()
regressor_OLS.pvalues
regressor_OLS.summary()
pred=regressor_OLS.predict(features_test)
print(pd.DataFrame(pred,labels_test))















