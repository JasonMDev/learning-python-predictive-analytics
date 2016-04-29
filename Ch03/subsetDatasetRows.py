# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:50:16 2016

@author: jasonm_dev
"""

import pandas as pd

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)
data.shape # Output: (3333, 21)

# Filter data by 'Day Calls' > 100
data1=data[data['Day Calls']>100]
data1.shape # Output: (1682, 21)

# Filter data by 'State' > VA
data2=data[data['State']=='VA']
data2.shape # Output: (77, 21)

# Filter data by 'Day Calls' > 100 and 'State' > VA
data3=data[(data['Day Calls']>100) & (data['State']=='VA')]
data3.shape # Output: (51, 21)