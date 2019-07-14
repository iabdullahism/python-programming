"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/
data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before 
you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the 
mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well 
and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import numpy as np
import pandas as pd
dataset=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')
#1-now first check any missing data or not
#2-if there any decimal scalling
#3-find outlyers
dataset.isnull().any(axis=0)
"""
(a) Can we predict lpsa from the other variables?

"""
#use decision tree algo regressor because the lpsa column takes continus values no class
labels=dataset.iloc[:,-1].values
features=dataset.iloc[:,:-1].values

#train test split of features data

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.2,random_state=0)

#first we perform decimal scalling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
#here we directly apply transform because  fit_transfrom save all 
#columns std and mean when we give the feature_test it apply std and mean of 
#given std and mean
features_test=sc.transform(features_test)

"""
(a) Can we predict lpsa from the other variables?


(1) Train the unregularized model (linear regressor) and calculate the 
mean squared error.

(2) Apply a regularized model now - Ridge regression and lasso as well 
and check the mean squared error.
"""
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)

lpsa_pred=regressor.predict(features_test)

print(pd.DataFrame({'actual':labels_test,'pred':lpsa_pred}))


"""
(1) Train the unregularized model (linear regressor) and calculate the 
mean squared error.
"""
from sklearn import metrics
print("mean squard error lr>",metrics.mean_squared_error(labels_test,lpsa_pred))
print("mean absolut error lr>",metrics.mean_absolute_error(labels_test,lpsa_pred))


"""

(2) Apply a regularized model now - Ridge regression and lasso as well 
and check the mean squared error.
"""
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

lm_lasso = Lasso() 
lm_ridge =  Ridge() 

lm_lasso.fit(features_train,labels_train)
lm_lasso_pred=lm_lasso.predict(features_test)

print("mean squard error of lasso>",metrics.mean_squared_error(labels_test,lm_lasso_pred))
print("mean absolut error lasso>",metrics.mean_absolute_error(labels_test,lm_lasso_pred))

#ridge technique
lm_ridge.fit(features_train,labels_train)
lm_ridge_pred=lm_ridge.predict(features_test)

print("mean squard error of ridge>",metrics.mean_squared_error(labels_test,lm_ridge_pred))
print("mean absolut error ridge>",metrics.mean_absolute_error(labels_test,lm_ridge_pred))


"""
(b) Can we predict whether lpsa is high or low, from other variables?
"""
#this question syas that if value in label is less their mean
#then no and if greater then yes

label_mean=np.mean(labels)
#lables is ndarray and map function not work in ndarray so 
#first convert into series
labels1=dataset.iloc[:,-1]
labels_cat=labels1.map(lambda x: 'Y' if x>2.47 else 'N')

"""
first  i use decision tree and random forest
and now.
features=features
labels=labels_cat
"""
#train test split
features_train1,features_test1,labels_cat_train1,labels_cat_test1=train_test_split(features,labels_cat)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(features_train1,labels_cat_train1)

lpsa_dt=dt.predict(features_test1)

labels_cat_test1=labels_cat_test1.values
#convert labels into numpy array
from sklearn.metrics import confusion_matrix
cm_dt=confusion_matrix(lpsa_dt,labels_cat_test1)



