
"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day 
(Distance_feature) and the mean percentage of time a driver was >5 mph over
 the speed limit (speeding_feature).

Perform K-means clustering to distinguish urban drivers and rural drivers.
Perform K-means clustering again to further distinguish speeding drivers from
 those who follow speed limits, in addition to the rural vs. urban division.
Label accordingly for the 4 groups.


"""
from sklearn.cluster import KMeans

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("deliveryfleet.csv")
features=dataset.iloc[:,1:].values
#first check dataset contais any missing values
#check catagorical data
#check label encoding
#decimal scalling
dataset.isnull().any(axis=0)
dataset.head(5)
#no there is no need decimal scalling but i do
#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()

# Fitting K-Means to the dataset
kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)





# Visualising the clusters
#plt.scatter(features[:,0][y_kmeans == 0], features[:,1][y_kmeans == 0], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()


#this graph shows that the urban is less fast due to traffic red-urban
# and village is move fast becasue there is no traffic police




#now we are converting into four clusters
kmeans1 = KMeans(n_clusters = 4, init = 'k-means++', random_state = 0)
pred_cluster1 = kmeans1.fit_predict(features)

plt.scatter(features[pred_cluster1 ==0,0],features[pred_cluster1 ==0,1], c='blue',label='cluster 1')
plt.scatter(features[pred_cluster1 ==1,0],features[pred_cluster1 ==1,1],c='red',label='cluster 2')
plt.scatter(features[pred_cluster1 ==2,0],features[pred_cluster1 ==2,1],c='yellow',label='cluster 2')
plt.scatter(features[pred_cluster1 ==3,0],features[pred_cluster1 ==3,1],c='black',label='cluster 2')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'green', label = 'Centroids')
plt.title('Clusters of datapoints')
plt.xlabel('X Cordindates')
plt.ylabel('Y Cordinates')
plt.legend()
plt.show()






wcss=[]
for i in range(1,11):
	kmean=KMeans(n_clusters=i,random_state=0,init='k-means++')
	kmean.fit_predict(features)
	wcss.append(kmean.inertia_)
	
plt.plot(range(1,11),wcss)	


