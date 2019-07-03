
"""

Q2. This famous classification dataset first time used in Fisher’s classic
 1936 paper, The Use of Multiple Measurements in Taxonomic Problems. Iris 
 dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris
 features to train an svm classifier and use the trained svm model to
 predict the Iris species type. To begin with let’s try to load the Iris 
 dataset.
 
 #load the dataset from skleran
"""
#from sklearn import dataset
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
iris.feature_names
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(iris.data, iris.target, test_size = 0.25, random_state = 0)

#first check dataset contains any missing values or not
# label encoding
# decimal scalling

"""
# kernels: linear, poly and rbf

"""
from sklearn.svm import SVC
classifier=SVC(kernel='poly',random_state=0)

classifier.fit(features_train,labels_train)

label_pred=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(label_pred,labels_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


print(confusion_matrix(labels_test,label_pred))  
print(classification_report(labels_test,label_pred))  
print(accuracy_score(labels_test, label_pred))












