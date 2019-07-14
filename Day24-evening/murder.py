"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.

    Perform dimension reduction and group the cities using 
	k-means based on Rape, Murder and assault predictors.


"""
import pandas as pd
import numpy as np
dataset=pd.read_csv("crime_data.csv")

features=dataset.iloc[:,1:]
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features=sc.fit_transform(features)


# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(features)

explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmean=KMeans(n_clusters=3,init='k-means++',random_state=0)

pred=kmean.fit_predict(features_train)

from matplotlib import pyplot as plt
plt.scatter(features_train[pred==0,0],features_train[pred==0,1],c='red',label='cluster 1')
plt.scatter(features_train[pred==1,0],features_train[pred==1,1],c='blue',label='cluster 2')
plt.scatter(features_train[pred==2,0],features_train[pred==2,1],c='green',label='cluster 3')
plt.xlabel("crime state")
plt.ylabel("crime rate")
plt.legend()
plt.show()


















