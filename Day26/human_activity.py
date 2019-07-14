"""

Human Activity Recognition with Smartphones

(Recordings of 30 study participants performing activities of daily living)

(Click Here To Download Dataset):
https://github.com/K-Vaid/Python-Codes/blob/master/Human_activity_recog.zip



In an experiment with a group of 30 volunteers within an age bracket
 of 19 to 48 years, each person performed six activities
 (WALKING, WALKING UPSTAIRS, WALKING DOWNSTAIRS, SITTING, STANDING, LAYING)
 wearing a smartphone (Samsung Galaxy S II) on the waist. The experiments have 
 been video-recorded to label the data manually.

The obtained dataset has been randomly partitioned into two sets,
 where 70% of the volunteers was selected for generating the training data
 and 30% the test data.

 

Attribute information

For each record in the dataset the following is provided:

        Triaxial acceleration from the accelerometer (total acceleration) 
		and the estimated body acceleration.
        Triaxial Angular velocity from the gyroscope.
        A 561-feature vector with time and frequency domain variables.
        Its activity labels.
        An identifier of the subject who carried out the experiment.

Train a tree classifier to predict the labels from the test data set 
using the following approaches:

  (a) a decision tree approach,

  (b) a random forest approach and

  (c) a logistic regression.

  (d) KNN approach

Examine the result by reporting the accuracy rates of all approach
 on both the testing and training data set. Compare the results. Which 
 approach would you recommend and why?

	Perform feature selection and repeat the previous step. Does your 
	accuracy improve?
        Plot two graph showing accuracy bar score of all the approaches
		 taken with and without feature selection.

"""
import numpy as np
import pandas as pd
dataset=pd.read_csv("train.csv")
dataset1=pd.read_csv("test.csv")
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

#first check any missing value or not
#second approach is catagorical data
#third approach is decimal scalling
"""
#decision tree perform using Gini and Entropy index
"""
dataset.isnull().any(axis=0)
dataset1.isnull().any(axis=0)

"""
check_null=list(dataset1.isnull().any(axis=0))

print("if null then return true=",any(check_null))

if it gives return true then we understand that any missing values in dataset
"""
#so there is no any missing values
#no need have to label encodiung
# and decimal scalling


#this problem is based on classifirer
features_train=dataset.iloc[:,:-1].values
labels_train=dataset.iloc[:,-1].values

features_test=dataset1.iloc[:,:-1].values
labels_test=dataset1.iloc[:,-1].values

"""
no need to train test split becase already 
two file given test.csv and training.csv

"""

"""
first use 
  (a) a decision tree approach
  (1) using gini
  (2) using entropy-index
"""
from sklearn.tree import DecisionTreeClassifier
dt_gini=DecisionTreeClassifier(criterion='gini',random_state=0)
dt_entropy=DecisionTreeClassifier(criterion='entropy',random_state=0)  

#now perform fit method
dt_gini.fit(features_train,labels_train)

DecisionTreePrediciton_gini=dt_gini.predict(features_test)

#using critiaiton='entropy'
dt_entropy.fit(features_train,labels_train)

DecisionTreePrediciton_entropy=dt_entropy.predict(features_test)

from sklearn.metrics import confusion_matrix,accuracy_score
#check accuracy using confusion metrix
cm_gini=confusion_matrix(DecisionTreePrediciton_gini,labels_test)

cm_entropy=confusion_matrix(DecisionTreePrediciton_entropy,labels_test)

print("accuracy using gini in DecisionTree model=",accuracy_score(DecisionTreePrediciton_gini,labels_test))

print("accuracy using entropy in DecisionTree model=",accuracy_score(DecisionTreePrediciton_entropy,labels_test))

print("gini is more powerfull to entropy in DecisionTree model")
"""

(b) a random forest approach and
"""
from sklearn.ensemble import RandomForestClassifier
rf_gini=RandomForestClassifier(n_estimators=400,criterion='gini',random_state=0)

rf_entropy=RandomForestClassifier(n_estimators=400,criterion='entropy',random_state=0)

#perofrm model using rf_gini
rf_gini.fit(features_train,labels_train)
RandomForestPrediction_gini=rf_gini.predict(features_test)

#now perform model using rf entropy
rf_entropy.fit(features_train,labels_train)
RandomForestPrediction_entropy=rf_entropy.predict(features_test)


#now check accuracy using confusion matrix
rf_gini=confusion_matrix(labels_test,RandomForestPrediction_gini)
print(rf_gini)
print("accuracy od model using RendomForest gini=",accuracy_score(labels_test,RandomForestPrediction_gini))


#now check accuracy  of random_forest entropy

rf_entropy=confusion_matrix(labels_test,RandomForestPrediction_entropy)
print(rf_entropy)
print("accuracy od model using RendomForest entropy=",accuracy_score(labels_test,RandomForestPrediction_entropy))



"""
 (c) a logistic regression.
""" 
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()

lr.fit(features_train,labels_train)
LogisticRegression_pred=lr.predict(features_test)

LogisticRegression_cm=confusion_matrix(labels_test,LogisticRegression_pred)
print(LogisticRegression_cm)
print("accuracy of logistic matrix",accuracy_score(labels_test,LogisticRegression_pred))




"""
 KNN approach
"""
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3,p=2)

knn.fit(features_train,labels_train)

knn_pred=knn.predict(features_test)

knn_cm=confusion_matrix(labels_test,knn_pred)
print(knn_cm)
print("accuracy score=",accuracy_score(labels_test,knn_pred))












