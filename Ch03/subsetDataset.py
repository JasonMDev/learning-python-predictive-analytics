# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:35:32 2016

@author: jasonm_dev
"""

import pandas as pd

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)

# Creates subset of the DataFrame by using square brackets.
# Selecting one column creates a Series object similar to Dataframe
account_length = data['Account Length']
account_length.head()
type(account_length) # Output: pandas.core.series.Series

# Creates subset of the DataFrame by using square brackets.
# Using multiple columns
subdata = data[['Account Length','VMail Message','Day Calls']]
subdata.head()
type(subdata) # Output: pandas.core.frame.DataFrame

# Alternative
wanted_columns=['Account Length','VMail Message','Day Calls']
subdata1=data[wanted_columns]
subdata1.head()

# Alternative
wanted=['Account Length','VMail Message','Day Calls']
# Gets list of columns names
column_list=data.columns.values.tolist()
# Removes 'wanted' column names from the column_list
sublist=[x for x in column_list if x not in wanted]
subdata2=data[sublist]
subdata2.head()