#first remove is,am are in text using stopword
#second stemming to convrt first form of word loved->love
"""
Q1. Code Challegene (NLP)
Dataset: amazon_cells_labelled.txt


The Data has sentences from Amazon Reviews

Each line in Data Set is tagged positive or negative

Create a Machine learning model using Natural Language Processing
 that can 
predict wheter a given review about the product is positive or negative
"""
import numpy as np
import pandas as pd
dataset=pd.read_csv("amazon_cells_labelled.txt", delimiter = '\t',header=None)
dataset.columns=['text','comment']

# Cleaning the texts
# Noise removal
""" language stopwords 
(commonly used words of a language – is, am, the, of, in etc), 
URLs or links, social media entities (mentions, hashtags), 
punctuations and industry specific words. 
This step deals with removal of all types of noisy entities present 
in the text.
"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#stopwords is a library that contains is am the and remove it in text

#Stemming:  Stemming is a rudimentary rule-based process 
# of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.
"""
The most common lexicon normalization practices are :

Stemming:  Stemming is a rudimentary rule-based process of stripping the 
suffixes (“ing”, “ly”, “es”, “s” etc) from a word.

Lemmatization: Lemmatization, on the other hand, is an 
organized 
& step by step procedure of obtaining the root form of 
the word, 
it makes use of vocabulary (dictionary importance of words) 
and 
morphological analysis (word structure and grammar relations).
"""

from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 
corpus = []
#perform row wise noise removal and stemming
#let's do it on just first row data

#sub means subtract anything except alphabat

ps = PorterStemmer()
for i in range(0,len(dataset)):
	
	review = re.sub('[^a-zA-Z]', ' ', dataset['text'][i])
	review = review.lower()
	review = review.split()
	
	review = [word for word in review 
	          if not word 
	          in set(stopwords.words('english'))]
	

#lem = WordNetLemmatizer() #Another way of finding root word

	review = [ps.stem(word) for word in review]
	#review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
	review = ' '.join(review)
	corpus.append(review)



# Creating the Bag of Words model
# Also known as the vector space model
# Text to Features (Feature Engineering on text data)

"""
this is the way that convert text data into column wise and label encoding
this can be done by creating dictonary
{
'good':2000
'best':1200
'bad':200
.....
these make a dict according to the value order and max_feature means take 
only top-1500 feature in text data
}
"""
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 800)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,random_state=0,test_size=0.1)


#this problem is based on classification
#first i use decision tree and navie bayes in maltimonial
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(features_train,labels_train)

pred=dt.predict(features_test)
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(labels_test,pred)

#now check random forest classifier
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=7, random_state=0)

rf.fit(features_train,labels_train)
pred1=rf.predict(features_test)

cm1=confusion_matrix(pred1,labels_test)
print("accuracy score",accuracy_score(pred1,labels_test))









