# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:48:24 2016

@author: jasonm_dev
"""

import pandas as pd
import numpy as np

# METHOD 1 – using the Customer Churn Model
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)

len(data)

# Generate set of random numbers with length of data.
a=np.random.randn(len(data))
# Create filter
check=a<0.8
# Filter training data below 0.8.
training=data[check]
# Filter testing data above 0.8.
testing=data[~check]

# Check lengths
len(training)
len(testing)

# METHOD 2 – using sklearn
# The test size specifies the size of the testing dataset: 
# 0.2 means that 20 percent of the rows of the dataset should go to testing 
# and the remaining 80 percent to training.
from sklearn.cross_validation import train_test_split
train, test = train_test_split(data, test_size = 0.2)

# METHOD 3 – using the shuffle function
# Using 'rb' means opening in binary mode 
# and create a 'bytes' object used in dataframes.
with open(fullpath,'rb') as f:
    #data_shuffle=f.readline().split('\n')
    data_shuffle=f.readline()    
#data_shuffle=open(fullpath,'r')
#np.random.shuffle(data_shuffle)
#train_data = data_shuffle[:3*len(data_shuffle)/4]
#test_data = data_shuffle[len(data_shuffle)/4:]
    
    
# Just readline creates a bytes object.
    #do a loop like the opdn one and main dict
