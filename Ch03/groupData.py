# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:57:12 2016

@author: jasonm_dev
"""

import numpy as np
import pandas as pd

# GENERATE DATAFRAME
a=['Male','Female']
b=['Rich','Poor','Middle Class']
gender=[]
seb=[]
for i in range(1,101):
    gender.append(np.random.choice(a))
    seb.append(np.random.choice(b))
height=30*np.random.randn(100)+155
weight=20*np.random.randn(100)+60
age=10*np.random.randn(100)+35
income=1500*np.random.randn(100)+15000

df=pd.DataFrame({'Gender':gender,'Height':height,'Weight':weight,'Age':age,'Income':income,'Socio-Eco':seb})
df.head()

# GROUPING OF DATA
# Splits data into data objects with attributes 'name' and 'group'.
# df.groupby('Gender') # Out: <pandas.core.groupby.DataFrameGroupBy object at 0x7f970d9b9828>

# Group by gender.
grouped = df.groupby('Gender')
# Object created is 'Male' and its group of data, and 'Female' and its group of data.
# grouped.groups

for names,groups in grouped:
    print (names)
    print (groups)
    

# Get a single group can be found.
grouped_female=grouped.get_group('Female')

# A set of categories can be used.
grouped_gender_socio=df.groupby(['Gender','Socio-Eco'])

for names,groups in grouped_gender_socio:
    print (names)
    print (groups)    
    
# AGGREGATION OF DATA
# Sum of data
grouped_gender_socio.sum() # Sum of dataheads
grouped_gender_socio.size() # Calculates the size of each group.
grouped_gender_socio.describe() # Summary statistics for each group separately.
grouped_gender_socio.aggregate({'Age':np.mean,'Height':lambda x:np.mean(x)/np.std(x)})
#  Use the lambda method for ratio of mean and standard deviation for height
grouped_gender_socio.aggregate([np.sum, np.mean, np.std]) # Apply to all columns.

# Grouped subsets behave like their own dataframes.
grouped_income=grouped['Income'] # You can apply function above here as well.

# FILTERING
grouped_gender_socio['Age'].filter(lambda x:x.sum()>700)

# TRANSFORMATION
# Calculate the standard normal values for all the elements 
# in the numerical columns of our data frame
zscore = lambda x: (x - x.mean()) / x.std()
#grouped.transform(zscore)

# Fills the missing values with the mean of the non-missing values.
f = lambda x: x.fillna(x.mean())
#grouped.transform(f) 

# MISCELLANEOUS OPERTAIONS
grouped.head(1) # Gets the first row of the male and female groups respectively.
grouped_gender_socio.head(1) # First row of each group.

grouped.tail(1) # Gets last rows of each group.
grouped_gender_socio.tail(1) # Gets last rows of each group.

# Good practise. First sort data frame before creating the groupby object.
df1=df.sort_values(by=['Age','Income']) # Sort by age and income.
sort_grouped=df1.groupby('Gender') # Group by gender
sort_grouped.head(1) # Show rows for the youngest of each gender.
sort_grouped.tail(1) # Show rows for the eldest of each gender.
