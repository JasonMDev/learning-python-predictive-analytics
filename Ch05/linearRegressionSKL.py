# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:03:02 2016

@author: jasonm_dev
"""

# Linear regression with scikit-learn

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Advertising.csv'
file = filepath+'/'+filename

advert=pd.read_csv(file)
advert.head()

# Split dataset into training and testing
feature_cols = ['TV', 'Radio']
X = advert[feature_cols]
Y = advert['Sales']
trainX,testX,trainY,testY = train_test_split(X,Y, test_size = 0.2)
lm = LinearRegression()
lm.fit(trainX, trainY)

print (lm.intercept_) # Out: 2.98314900713
print (lm.coef_) # Out: [ 'TV': 0.04536014  'Radio': 0.18767089]

zipped = zip(feature_cols, lm.coef_)
list(zipped)
# Out:
#[('TV', 0.044571627228483394), ('Radio', 0.19465327712760053)]

# Rsquared
lm.score(trainX, trainY) # Out: 0.89235897920220186

# The model can be used to predict the value of sales using TV and radio 
# variables from the test dataset
lm.predict(testX)