
"""

Q2. (Create a program that fulfills the following specification.)
tshirts.csv


T-Shirt Factory:

You own a clothing factory. You know how to make a T-shirt given the height 
and weight of a customer.

You want to standardize the production on three sizes: small, medium,
 and large. How would you figure out the actual size of these 3 types
 of shirt to better fit your customers?

Import the tshirts.csv file and perform Clustering on it to make sense
 out of the data as stated above.

"""
import numpy as np
import pandas as pd
dataset=pd.read_csv("tshirts.csv")
#first check any missing value
#and check catagorical data
#decimal scalling
dataset.isnull().any(axis=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

features=dataset.iloc[:,1:].values
features=sc.fit_transform(features)
#now check data how see in graph

import matplotlib.pyplot as plt
plt.scatter(features[:,0],features[:,1],label='t-shirt')
plt.xlabel("t shirt size")
plt.ylabel("t shirt weight")

#here data is uniform disturbution so we aply knn
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)
pred_cluster = kmeans.fit_predict(features)

#now make graph
plt.scatter(features[pred_cluster==0,0],features[pred_cluster==0,1],label='small t shirt', c = 'red')
plt.scatter(features[pred_cluster==1,0],features[pred_cluster==1,1],label='medium t-shirt',c = 'green')
plt.scatter(features[pred_cluster==2,0],features[pred_cluster==2,1],label='large t-shirt',c = 'blue')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')

plt.xlabel("t-shirt size")
plt.ylabel("t shirt weight")
plt.legend()
plt.show()























