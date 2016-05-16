# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:11:39 2016

@author: jasonm_dev
"""
# Implementing a decision tree with scikit-learn

import pandas as pd
import numpy as np

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'iris.csv'
file = filepath+'/'+filename
data=pd.read_csv(file)
data.head()

# Unique species
data['Species'].unique() 
# Out: array(['setosa', 'versicolor', 'virginica'], dtype=object)

# 1st get the predictor and the target variables
colnames=data.columns.values.tolist()
predictors=colnames[:4]
target=colnames[4]

# Split into training and test data
# Generate a uniform random distribution of numbers between 0 and 1.
# train data selected is any data which has a number less than 0.75.
# Complement goes to the test data 
data['is_train'] = np.random.uniform(0, 1, len(data)) <= .75
train, test = data[data['is_train']==True], data[data['is_train']==False]

# Create a decision tree.
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion='entropy',min_samples_split=20, random_state=99)
dt.fit(train[predictors], train[target])
# min_samples_split specifies the mnimum number of observations required 
# to split a node into a subnode.
# Default = 2
# Recommended = 20


# Test predicted model
# Predicts class (species) of the flower via decision tree
preds=dt.predict(test[predictors])
# Creates a tablecomparing the Actual species and the predicted species.
pd.crosstab(test['Species'],preds,rownames=['Actual'],colnames=['Predictions'])

# Visualizing the tree
# Create a .dot file from the Decision Tree Classifier
from sklearn.tree import export_graphviz
dotfilename= 'dtree2.dot'
dotfiles = filepath+'/'+dotfilename
with open(dotfiles, 'w') as dotfile:
    export_graphviz(dt, out_file = dotfile, feature_names = predictors)
dotfile.close()

# Rendering a dotfile into a tree
# After installing graphviz
from os import system

system("dot -Tpng //home/jasonm_dev/coding/learning-python-predictive-analytics/datasets/dtree2.dot -o //home/jasonm_dev/coding/learning-python-predictive-analytics/datasets/dtree2.png")

# Cross validate the etire dataset.
X=data[predictors]
Y=data[target]
dt1 = DecisionTreeClassifier(criterion='entropy',max_depth=5, min_samples_split=20, random_state=99)
dt1.fit(X,Y)
# Import the cross validation methods from sklearn and perform the cross validation
from sklearn.cross_validation import KFold
crossvalidation = KFold(n=X.shape[0], n_folds=10, shuffle=True, random_state=1)
from sklearn.cross_validation import cross_val_score
score = np.mean(cross_val_score(dt1, X, Y, scoring='accuracy', cv=crossvalidation, n_jobs=1))
score #Out: 0.93333333333333335

# Feature importance test
# Higher the value, the higher the feature importance
dt1.feature_importances_ 
# Out: array([ 0. ,  0. ,  0.66869158,  0.33130842])
# Out: ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']
# 1st: petal.length then petal width