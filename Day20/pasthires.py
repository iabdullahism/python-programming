

"""

Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or 
not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale
 of 0-2.

    Build and perform Decision tree based on the predictors and see how 
	accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of
 specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous 
	employers 4, went to top-tire school, having Bachelor's Degree without
	 Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers
 4, didn't went to any top-tire school, having Master's Degree with Internship.

"""
import pandas as pd
import numpy as np
dataset=pd.read_csv("PastHires.csv")
features=dataset.iloc[:,:-1]
labels=dataset.iloc[:,-1]
#check is any missing values or not
dataset.isnull().any(axis=0)
#
features['Level of Education']=features['Level of Education'].map(lambda x:0 if x=='BS' else (1 if x=='MS' else 2) )
features['Employed?']=features['Employed?'].map(lambda x1:1 if x1=='Y' else 0)
features['Top-tier school']=features['Top-tier school'].map(lambda x:1 if x=='Y' else 0)
features['Interned']=features['Interned'].map(lambda x:1 if x=='Y' else 0)
labels=labels.map(lambda x:1 if x=='Y' else 0)


#if we add values with iloc then it becomes array and map not works in nd array
#so before convert ndarray we must chnae object to int of features and labels
#now convert features and labels into ndarray
features=np.array(features)
labels=np.array(labels)

#now perfomr decimal scalling
#because years of experience contain big amount compare others

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)
#no need to perform labels to standerd scalling

#now split the data
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=.2,random_state=0)

#perform decision tree
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(features_train,labels_train)

pred=dt.predict(features_test)
print(pd.DataFrame({'actual':labels_test,'predction':pred}))


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(pred,labels_test)
print("decision tree algo")
print(cm)

"""
1.   Predict employment of a currently employed 10-year veteran, previous 
employers 4, went to top-tire school, having Bachelor's Degree without
 Internship.
"""
"""
yyears_ex=10
previus_emplo=4
top_scholl=1
btch=0
intesnhip=0
"""
employement_data=[10,1,4,1,0,0]
employement_array=np.array(employement_data)
#decimal scalling
employement_array=sc.transform(employement_array.reshape(1,-1))
#now apply decision tree algo
employement_pred=dt.predict(employement_array)



"""
Predict employment of an unemployed 10-year veteran, ,previous employers 4,
 didn't went to any top-tire school, having Master's Degree with Internship.
"""
year_exp=10
unemployed=0
previous_emp=4
top_school=0
mtech=1
internship=1

unemployed_data=[10,0,4,0,1,1]
unemployed_array=np.array(unemployed_data).reshape(1,-1)
#standerd scalling
unemployed_array=sc.transform(unemployed_array)

#now apply decision tree algo
unemployement_pred=dt.predict(unemployed_array)

"""
apply random forest for n=10 decsion tree
"""
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  
labels_pred = classifier.predict(features_test)
print(pd.DataFrame({'actual':labels_test,'predction':labels_pred}))

cm1=confusion_matrix(labels_pred,labels_test)

print("random forest algo=")
print(cm1)
"""
both question apply on random forest
"""

employement_randomForest_pred=classifier.predict(employement_array)


unemployement_randomForest_pred=classifier.predict(unemployed_array)



