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

# Build the regression tree model.
from sklearn.tree import DecisionTreeRegressor
# min number of observation per node for split: 30
# min number of observations per node to classify as leaf: 10
regression_tree = DecisionTreeRegressor(min_samples_split=30,min_samples_leaf=10,random_state=0)
regression_tree.fit(X,Y)

# Use model to make predictions
reg_tree_pred=regression_tree.predict(data[predictors])
data['pred']=reg_tree_pred
cols=['pred','medv']
# Compare prediction with actual
data[cols]

# Cross-validate the model and check accuracy
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

crossvalidation = KFold(n=X.shape[0], n_folds=10,shuffle=True, random_state=1)
score = np.mean(cross_val_score(regression_tree, X, Y,scoring='mean_squared_error', cv=crossvalidation,n_jobs=1))
score #Out[14]: -20.107307036443846

# The feature importance can be checked
regression_tree.feature_importances_
"""Out[16]: 
array([ 0.03421203,  0.        ,  0.00116059,  0.        ,  0.01856163,
        0.6308568 ,  0.01725115,  0.00137451,  0.        ,  0.00236983,
        0.00933325,  0.        ,  0.28488021])
In [8]: colnames
Out[8]: 
['crim',
 'zn',
 'indus',
 'chas',
 'nox',
 'rm',
 'age',
 'dis',
 'rad',
 'tax',
 'ptratio',
 'black',
 'lstat',
 'medv']
 
The most important varaibles are age, lstat and rm in ascending order.
Highest values have the most impoprtance. DOn't agree with selected variables.
"""

