
"""

Q1. (Create a program that fulfills the following specification.)
affairs.csv


Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, 
in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age

yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college,
 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled,
 3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business,
 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

    Now, perform Classification using logistic regression and check your model 
	accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb,
 since they should be treated as categorical variables. Careful from dummy variable trap for both!!

 What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond 
to a decrease in the likelihood of having an affair.)

    Predict the probability of an affair for a random woman not present 
	in the dataset. She's a 25-year-old teacher who graduated college,
	 has been married for 3 years, has 1 child, rates herself as strongly
	  religious, rates her marriage as fair, and her husband is a farmer.

Optional

    Build an optimum model, observe all the coefficients.

"""
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
dataset=pd.read_csv("affairs.csv")
#first check the data cleaning and missing the data
dataset.isnull().any(axis=0)

features=dataset.iloc[:,:-1].values
labels=dataset.iloc[:,-1].values

"""
#check if any catagorical data or not then remove first
#there occuption and husband occupation are catagorical data
#remove one by one labeloncoder is alredy so perform onhotencoder
#and remove one dummy variable
"""
"""
first encode occuption encoder and then remove dummy variabile
dataset['occupation'].value_counts()
"""

onhotencoder1=OneHotEncoder(categorical_features=[6])
features=onhotencoder1.fit_transform(features).toarray()

"""
remove first column
"""
features=features[:,1:]

"""
now we onhotencoder the husband occupation column
"""
onhotencoder2=OneHotEncoder(categorical_features=[11])
features=onhotencoder2.fit_transform(features).toarray()

"""
remove first column
"""
features=features[:,1:]


"""

decimal scallling
"""
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

pd.DataFrame(labels_pred, labels_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)


"""

Predict the probability of an affair for a random woman not present 
in the dataset. She's a 25-year-old teacher who graduated college,
has been married for 3 years, has 1 child, rates herself as strongly
religious, rates her marriage as fair, and her husband is a farmer.

year=25
occupation=4
educ=16
yrs_merries=3
childern=1
regilous=4
hus_occ=2
rate_fair=0
#first onehotencoder of hus_occupation and occupation
"""


Random_women_data=[3,25,3,1,4,16,4,2]
Random_women_data1=np.array(Random_women_data).reshape(1,-1)
Random_women_data1=onhotencoder1.transform(Random_women_data1).toarray()
Random_women_data1=Random_women_data1[:,1:]


Random_women_data1=onhotencoder2.transform(Random_women_data1).toarray()
Random_women_data1=Random_women_data1[:,1:]


labels_pred1 = classifier.predict(Random_women_data1)


print("this predict merital affair is zero",labels_pred1)
