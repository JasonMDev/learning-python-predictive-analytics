# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:58:58 2016

@author: jasonm_dev
"""

import pandas as pd

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)
data.shape # Output: (3333, 21)

# Filter data for the first 50 rows.
subdata_first_50=data[['Account Length','VMail Message','Day Calls']][1:50]
subdata_first_50

# Filter data by 'Day Calls' > 100
data1=data[data['Day Calls']>100]
data1.shape # Output: (1682, 21)

# Alternative .ix[rowstart:rowend,colstart:colend]
data.ix[1:100,1:6]
data.ix[:,1:6]
data.ix[1:100,[2,5,7]]
data.ix[[1,2,5],['Area Code','VMail Plan','Day Mins']]