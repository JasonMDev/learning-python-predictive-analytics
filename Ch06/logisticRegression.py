# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:48:26 2016

@author: jasonm_dev
"""

# Understanding the math behind logistic regression
import pandas as pd
import numpy as np

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Gender Purchase.csv'
file = filepath+'/'+filename

df=pd.read_csv(file)
df.head()
print(df.shape) #Out: (511, 2)

# Contingency table for the dataset
contingency_table=pd.crosstab(df['Gender'],df['Purchase'])
contingency_table
# Add horizontally
contingency_table.sum(axis=1)
# Add vertically
contingency_table.sum(axis=0)

# Calculate the proportions
contingency_table.astype('float').div(contingency_table.sum(axis=1),axis=0)