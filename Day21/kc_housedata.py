"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score

"""

"""
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
use for overfitting case
"""
#we use backward elimination
#we use decimal scalling
#handle missing values

import pandas as pd
import numpy as np

dataset=pd.read_csv("kc_house_data.csv")
#check miising value
dataset.isnull().any(axis=0)
#sqft_above columns have missing value
labels=dataset.iloc[:,2].values

features=dataset.iloc[:,3:]
#features.isnull().any(axis=0)
#handel sqft_above using fill mean values
features['sqft_above']=features['sqft_above'].fillna(features['sqft_above'].mean())
#use backward eluminition
features=features.values



import statsmodels.api as sm
features = sm.add_constant(features)

features_opt = features
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
p=list(regressor_OLS.pvalues)
print(max(p))
"""
p=list(regressor_OLS.pvalues)
a= np.delete(a, 1, 1)  # delete second column of a


"""
#after drop 11th column
features=np.delete(features,11,1)

features_opt = features
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()
p=list(regressor_OLS.pvalues)
print(max(p))
#all column data have less p value 5%

#now perform linear regression
#first decimal scalling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)


#train test split
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,random_state=0,test_size=0.005)

#now perform multiple linear regression
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
pred=regressor.predict(features_test)
print(pd.DataFrame({'actual':labels_test,'pred':pred}))
















