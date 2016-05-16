# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:01:46 2016

@author: jasonm_dev
"""
"""
Implementing a regression tree using Python
"""
import pandas as pd
import numpy as np

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Boston.csv'
file = filepath+'/'+filename
data=pd.read_csv(file)
data.head() #Out: (506, 14)

# First 13 varaibles set as predictor variables
# and the last (MEDV) as the target variable
colnames=data.columns.values.tolist()
predictors=colnames[:13]
target=colnames[13]
X=data[predictors]
Y=data[target]

# Build the random forest model.
from sklearn.ensemble import RandomForestRegressor
# Node size(min_samples_leaf): not so important here
# Number of trees (n_estimators): generally around 500 
# Number of predictors sampled: 2 - 5 
# number of jobs running parallel (n_jobs)
rf = RandomForestRegressor(n_jobs=2,oob_score=True,n_estimators=10)
rf.fit(X,Y)

# The predicted values can be obtained
rf.oob_prediction_
#Let us now make the predictions a part of the data frame and have a look at it. 
data['rf_pred']=rf.oob_prediction_
cols=['rf_pred','medv']
data[cols].head()

# To calculate a mean squared error we use oob predicted and actual values.
data['rf_pred']=rf.oob_prediction_
data['err']=(data['rf_pred']-data['medv'])**2
sum(data['err'])/506 # Out[23]: 23.031183503507172

# oob score
rf.oob_score_ # Out[24]: 0.72718189300945413

# Try with bigger sample
rf2 = RandomForestRegressor(n_jobs=2,oob_score=True,n_estimators=500)
rf2.fit(X,Y)
data['rf2_pred']=rf2.oob_prediction_
cols2=['rf2_pred','medv']
data[cols2].head()
data['rf2_pred']=rf2.oob_prediction_
data['err2']=(data['rf2_pred']-data['medv'])**2
sum(data['err2'])/506 # Out[23]: 10.05342135115402
rf2.oob_score_ # Out[24]: 0.88091122710291847