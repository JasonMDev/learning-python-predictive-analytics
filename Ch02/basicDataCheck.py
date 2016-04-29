# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:11:24 2016

@author: jasonm_dev
"""

import pandas as pd
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch02'
filename = 'titanic3.csv'
fullpath = path+'/'+filename

data=pd.read_csv(fullpath)

# Specify the number of rows to see.
data.head(5)
# Confirm dimension
data.shape
# List the data frame
data.columns.values
# Create summary statistics
data.describe()
# FInd out the data type of each column
data.dtypes

# Find entries with that have missing values.
pd.isnull(data['body'])
# Opposite method
pd.notnull(data['body'])

# Count the number of missing values. 1189
pd.isnull(data['body']).values.ravel().sum()
# Opposite: 121
pd.notnull(data['body']).values.ravel().sum()


# HANDLING MISSING DATA
# Deletion
# Drop any row with where all columns have missing info.
data.dropna(axis=0,how='all')
# Drop any rows where column have any empty cells of information.
data.dropna(axis=0,how='any')

#Imputation
#data.fillna(0)
#data.fillna('missing')
data['body'].fillna(0)
data['age'].fillna(data['age'].mean()) #29.881135
data['age'].fillna(method='ffill') #Fill in with preceding non-missing value.
data['age'].fillna(method='backfill') #Fill in with succeding non-missing value.

# CREATING DUMMY VARIABLE
# Split into new variable 'sex_female' and 'sex_male'
dummy_sex=pd.get_dummies(data['sex'],prefix='sex')
column_name=data.columns.values.tolist()
column_name.remove('sex') # Remove column 'sex'
data[column_name].join(dummy_sex) # Add dummy column created above.