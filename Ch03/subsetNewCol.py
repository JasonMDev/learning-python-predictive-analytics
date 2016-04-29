# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:06:22 2016

@author: jasonm_dev
"""

import pandas as pd

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)
data.shape # Output: (3333, 21)

# Create new column by totalling the minutes columns.
data['Total Mins']=data['Day Mins']+data['Eve Mins']+data['Night Mins']
data['Total Mins'].head() # Name: Total Mins, dtype: float64