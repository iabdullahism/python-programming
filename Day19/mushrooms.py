"""
--------------------------

Q2. (Create a program that fulfills the following specification.)
mushrooms.csv

Import mushrooms.csv file

This dataset includes descriptions of hypothetical samples corresponding to 
23 species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn 
from The Audubon Society Field Guide to North American Mushrooms (1981). Each 
species is identified as definitely edible, definitely poisonous, or of unknown 
edibility and not recommended. This latter class was combined with the poisonous
 one.

 

Attribute Information:

classes: edible=e, poisonous=p (outcome)

cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s

cap-surface: fibrous=f,grooves=g,scaly=y,smooth=s

cap-color: brown=n, buff=b,cinnamon=c,gray=g,green=r,pink=p,
purple=u,red=e,white=w,yellow=y

 

bruises: bruises=t, no=f

 

odor: almond=a,anise=l,creosote=c,fishy=y,foul=f,musty=m,none=n,
pungent=p,spicy=s

 

gill-attachment: attached=a,descending=d,free=f,notched=n

 

gill-spacing: close=c,crowded=w,distant=d

 

gill-size: broad=b,narrow=n\

 

gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g,

green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y

 

stalk-shape: enlarging=e,tapering=t

 

stalk-root: bulbous=b,club=c,cup=u,equal=e,rhizomorphs=z,rooted=r,missing=?

 

stalk-surface-above-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-surface-below-ring: fibrous=f,scaly=y,silky=k,smooth=s

 

stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p
,red=e,white=w,yellow=y

 

stalk-color-below-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o,pink=p,
red=e,white=w,yellow=y

 

veil-type: partial=p,universal=u

 

veil-color: brown=n,orange=o,white=w,yellow=y

ring-number: none=n,one=o,two=t

 

ring-type: cobwebby=c,evanescent=e,flaring=f,large=l,none=n,pendant=p
,sheathing=s,zone=z

 

spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r,orange=o
,purple=u,white=w,yellow=y

 

population: abundant=a,clustered=c,numerous=n,scattered=s,several=v,solitary=y

 

habitat: grasses=g,leaves=l,meadows=m,paths=p,urban=u,waste=w,woods=d

    Perform Classification on the given dataset to predict if the mushroom
	 is edible or poisonous w.r.t. it’s different attributes.

(you can perform on habitat, population and odor as the predictors)

    Check accuracy of the model.

"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

dataset=pd.read_csv("mushrooms.csv")

"""
 perform on habitat, population and odor as the feature
 and class is labels
"""
dataset1=dataset.iloc[:,[0,5,21,22]]
"""
first labels and feature
"""
labels=dataset1.iloc[:,0].values
features=dataset1.iloc[:,1:].values
"""
now we remove catagorical ony by one
"""
#first takes labesl and make a seperate object of onehotencoder
"""
labelencoder=LabelEncoder()
labels[:, 0] = labelencoder.fit_transform(labels[:,0]]

	
in classification we need'nt to labels onhotencode
if we want we can otherwise not	
"""

"""
for apply label encoder of multiple catagorical data
must before all data label encode and then after onhotencoder
"""
labelencoder1 = LabelEncoder()
features[:, 0] = labelencoder1.fit_transform(features[:, 0])


labelencoder2 = LabelEncoder()
features[:, 1] = labelencoder2.fit_transform(features[:, 1])



labelencoder2 = LabelEncoder()
features[:, 2] = labelencoder2.fit_transform(features[:, 2])
#now onehot encoder

onhotencoder1=OneHotEncoder(categorical_features=[0])
features=onhotencoder1.fit_transform(features).toarray()

features=features[:,1:]




onhotencoder2=OneHotEncoder(categorical_features=[-2])
features=onhotencoder2.fit_transform(features).toarray()

features=features[:,1:]

onhotencoder3=OneHotEncoder(categorical_features=[-1])
features=onhotencoder3.fit_transform(features).toarray()

features=features[:,1:]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,label_test=train_test_split(features,labels,test_size = 0.25, random_state = 0)


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(label_test, labels_pred)







