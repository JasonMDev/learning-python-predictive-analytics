# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:33:18 2016

@author: jasonm_dev
"""

# Classify wine by chemical composition
import pandas as pd
import matplotlib.pyplot as plt

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'wine.csv'
file = filepath+'/'+filename
df=pd.read_csv(file,sep=';')
df.head()

# Plot data to have a look at the quality
#% matplotlib inline
#plt.hist(df['quality'])

# Check the mean of the quality
df.groupby('quality').mean()

# Normalizing the values in the dataset
df_norm = (df - df.min()) / (df.max() - df.min())
df_norm.head() 

# Hierarchical clustering using scikit-learn
from sklearn.cluster import AgglomerativeClustering
ward = AgglomerativeClustering(n_clusters=6, linkage='ward').fit(df_norm)
md=pd.Series(ward.labels_)
ward.children_

# Plot the histogram of cluster labels
#plt.hist(md)
#plt.title('Histogram of Cluster Label')
#plt.xlabel('Cluster')
#plt.ylabel('Frequency')

# K-Means clustering using scikit-learn
# fits the k-means clustering model to the wine dataset
from sklearn.cluster import KMeans
from sklearn import datasets
model=KMeans(n_clusters=6)
model.fit(df_norm)

# an array depicting the cluster the row belongs to
model.labels_
# Out: array([4, 4, 4, ..., 0, 0, 3], dtype=int32)

# Make the array apart of the dataframe
md=pd.Series(model.labels_)
df_norm['clust']=md
df_norm.head()

# Centroids for each cluster
model.cluster_centers_

# j-score
model.inertia_

# Plot histogram of the cluster
plt.hist(df_norm['clust'])
plt.title('Histogram of Clusters')
plt.xlabel('Cluster')
plt.ylabel('Frequency')