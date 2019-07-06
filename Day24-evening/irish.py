

"""
Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species
 of Iris flower (Iris setosa, Iris virginica and Iris versicolor).

    Four features were measured from each sample: the length and the
	 width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the 
	

following command:\
from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to
 distinguish the 3 species.


"""
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data
#first check is there any null values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
iris=sc.fit_transform(iris)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features_train = pca.fit_transform(iris)
explained_variance = pca.explained_variance_ratio_


from sklearn.cluster import KMeans
kmean=KMeans(n_clusters=3,init='k-means++',random_state=0)

pred=kmean.fit_predict(features_train)

from matplotlib import pyplot as plt

plt.scatter(features_train[pred==0,0],features_train[pred==0,1],c='red',label='cluster 1')
plt.scatter(features_train[pred==1,0],features_train[pred==1,1],c='green',label='cluster 2')
plt.scatter(features_train[pred==2,0],features_train[pred==2,1],c='blue',label='cluster 3')
plt.legend()
plt.xlabel("length")
plt.ylabel("width")
plt.show()


















