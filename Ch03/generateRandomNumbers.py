# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:28:15 2016

@author: jasonm_dev
"""
import pandas as pd
import numpy as np

# Generate Random Numbers
np.random.randint(1,100) #Random number between 1 and 100
np.random.random() #Random number between 1 and 100

# Generate n amount of random numbers between a and b
def randint_range(n,a,b):
    x=[]
    for i in range(n):
        x.append(np.random.randint(a,b))
    return x
    
# Generate 10 amount of random numbers between 5 and 200
randint_range(10,5,200) 
# Out: [169, 47, 124, 73, 109, 63, 84, 93, 8, 129]

# Random range of number in specific multiple
import random
for i in range(3):
    print (random.randrange(0,100,5))
    
# Shuuffle list or array in a random order.
b = randint_range(10,5,200) 
b # Out: [93, 194, 30, 38, 146, 40, 177, 172, 197, 182]
np.random.shuffle(b) 
b # Out: [177, 182, 146, 40, 194, 30, 197, 172, 38, 93]

# 'Choice' method is used to select a random item from a list of items.
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch03'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)
data.shape # Output: (3333, 21)

# Create a list from the column names
column_list=data.columns.values.tolist()

# Select an item at random from the list.
np.random.choice(column_list) #Out: "Int'l Plan"
np.random.choice(column_list) #Out: 'VMail Plan'
np.random.choice(column_list) #Out: 'Eve Calls'
np.random.choice(column_list) #Out: 'Eve Mins'