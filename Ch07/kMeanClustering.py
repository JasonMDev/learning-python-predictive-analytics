# -*- coding: utf-8 -*-
"""
Created on Fri May 13 13:15:01 2016

@author: jasonm_dev
"""
# K-means clustering
import numpy as np

# Define an observation set of 30x3
obs=np.random.random(90).reshape(30,3)
obs

# I decided that I want two clusters 
c1=np.random.choice(range(len(obs)))
c2=np.random.choice(range(len(obs)))
clust_cen=np.vstack([obs[c1],obs[c2]])
clust_cen # 2 rows in array correspond to 2 cluster centroids.

# Implement k-menas clustering
from scipy.cluster.vq import vq
vq(obs,clust_cen)

# First array tells us which cluster the observation belongs to.
# '0' for c1, '1' for c2
# i.e. obs1 is with c2, obs2 is with c1
# Second array tells us how far the observation is from it cluster centroid.
# obs1 is 0.25 units away from c2 cluster centroid
# obs1 is 0.49 units away from c1 cluster centroid
#(array([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1,
#        0, 0, 1, 1, 0, 0, 1], dtype=int32),
# array([ 0.24932073,  0.49594229,  0.28098465,  0.50348212,  0.        ,
#        0.61496506,  0.26303013,  0.42779775,  0.59958318,  0.3468564 ,
#         0.40935109,  0.58624004,  0.42803874,  0.78335592,  0.50565815,
#         0.61892717,  0.57338804,  0.51580769,  0.37107392,  0.54979847,
#         0.48482825,  0.5257047 ,  0.50568491,  0.43748909,  0.71436479,
#         0.        ,  0.39646343,  0.47429546,  0.21875716,  0.59853208]))

# FInd the cluster centroid for the two centroids
from scipy.cluster.vq import kmeans
kmeans(obs,clust_cen)
# The two rows in the array correspond to the two final cluster centroids.
# At the end, J-score, which we seek to minimize
# (array([[ 0.62260732,  0.69445579,  0.50227104],
#        [ 0.37635439,  0.32446748,  0.32121864]]), 0.36366199194289345)


# Alternatively, just provide the number of required clusters.
from scipy.cluster.vq import kmeans
kmeans(obs,2)