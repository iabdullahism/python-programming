"""


Q1. (Create a program that fulfills the following specification.)

Program Specification:

Import breast_cancer.csv file.

This breast cancer database was obtained from the University of Wisconsin

Hospitals, Madison from Dr. William H. Wolberg.

Attribute Information: (class attribute has been moved to last column)

Sample Code Number(id number)                     ----> represented by column A.

Clump Thickness (1 – 10)                         ----> represented by column B.
Uniformity of Cell Size(1 - 10)                  ----> represented by column C.
Uniformity of Cell Shape (1 - 10)                 ---> represented by column D.
Marginal Adhesion (1 - 10)                       ----> represented by column E.
Single Epithelial Cell Size (1 - 10)             ----> represented by column F.
Bare Nuclei (1 - 10)                             ----> represented by column G.
Bland Chromatin (1 - 10)                         ----> represented by column H.
Normal Nucleoli (1 - 10)                        ----> represented by column I.
Mitoses (1 - 10)                                 ----> represented by column J.
Class: (2 for Benign and 4 for Malignant)         ----> represented by column K. 
A Benign tumor is not a cancerous tumor and Malignant tumor is a cancerous tumor

           Impute the missing values with the most frequent values.
Perform Classification on the given data-set to predict if the tumor is
 cancerous or not.
   Check the accuracy of the model.
  Predict whether a women has Benign tumor or Malignant tumor,
 if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity 
of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4,
 Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)
"""

from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd
dataset=pd.read_csv("breast_cancer.csv")
#first handle the misssing values
dataset.isnull().any(axis=0)

#first remove the nan values
#second drop the first column 
#then if label encoder then do
#train test split
"""
handle missing values using numpy
"""
# Cleaning dataset of NaN
#not use sequence no
dataset=dataset.replace(np.nan,0)

features=dataset.iloc[:,1:-1].values
labels=dataset.iloc[:,-1].values




#trian test split using only dataset 
from sklearn.model_selection import train_test_split
"""
different approach to train test
"""
features_train,feature_test,labels_train,labels_test=train_test_split(features,labels,random_state=0,test_size=0.2)

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

gnb = GaussianNB()
bnb=BernoulliNB()
mnb=MultinomialNB()
"""
there are the types of fnction that can predict prediction
"""
"""
Gussian navie bayes
when contius values data
"""

gnb.fit(features_train,labels_train)
pred=gnb.predict(feature_test)
print(pd.DataFrame({'actual':labels_test,'prediction':pred}))
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(pred,labels_test)
prediction21=gnb.predict(women_data)


print("Gussian navie bayes",cm)


"""
second method Beronuli navie bayes
binary format data  1,0 forms

"""
bnb.fit(features_train,labels_train)
pred1=bnb.predict(feature_test)
cm1=confusion_matrix(pred1,labels_test)

prediction1=bnb.predict(women_data)

print("Beronuli navie bayes",cm1)



"""
third  MultinomialNB
text format data

"""
mnb.fit(features_train,labels_train)
pred2=mnb.predict(feature_test)
cm2=confusion_matrix(pred2,labels_test)
prediction2=mnb.predict(women_data)

print(cm2)


#use svm as classifire and regressor
#mostly use in classifier
from sklearn.svm import SVC
"""
# kernels: linear, poly and rbf
#thesase are methods where we can apply 
"""
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

#model score
score = classifier.score(feature_test,labels_test)
print("score using support vector machine=",score)

pred3=classifier.predict(feature_test)
cm3=confusion_matrix(pred3,labels_test)

#now
"""
Check the accuracy of the model.
              Predict whether a women has Benign tumor or Malignant tumor,
 if her Clump thickness is around 6, uniformity of cell size is 2, Uniformity 
of Cell Shape is 5, Marginal Adhesion is 3, Bland Chromatin is 9, Mitoses is 4,
 Bare Nuclei is 7, Normal Nuclei is 2 and Single Epithelial Cell Size is 2

(you can neglect the id number column as it doesn't seem  a predictor column)
""" 
women_data=[6,2,5,3,2,7,9,2,4]
women_data=np.array(women_data).reshape(1,-1)

prediction=classifier.predict(women_data)
print("4 for Malignant tumor is a cancerous tumor",prediction)



"""
this question is based on svm but
check who gives best
prediction in svm and navie bayes
"""






