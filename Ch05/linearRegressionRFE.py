# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:03:02 2016

@author: jasonm_dev
"""

# Linear regression with scikit-learn

import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.svm import SVR

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Advertising.csv'
file = filepath+'/'+filename

advert=pd.read_csv(file)
advert.head()

# Feature selection with scikit-learn
# Recursive Feature Elimination (RFE)
feature_cols = ['TV', 'Radio','Newspaper']
X = advert[feature_cols]
Y = advert['Sales']
# Choose 'linear' model.
estimator = SVR(kernel="linear")
# number of desired variables
selector = RFE(estimator,2,step=1)
selector = selector.fit(X, Y)

# Selected variables.
selector.support_ # Out: array([ True,  True, False], dtype=bool)
 # X consists of three variables: TV, radio, and newspaper.
# Newspaper hasn't been selected.

# Selector ranking
selector.ranking_ # Out: array([1, 1, 2])
# All the selected variables will have a ranking of 1.
# Rest are shown in descending order.