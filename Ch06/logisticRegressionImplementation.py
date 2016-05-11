# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:15:24 2016

@author: jasonm_dev
"""

# Implementing logistic regression with Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'bank.csv'
file = filepath+'/'+filename

bank=pd.read_csv(file, sep=';')
bank.head()
print(bank.shape) #Out: (4119, 21)

# Column Names
bank.columns.values

# Out: array(['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
#       'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
#       'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx',
#       'cons.conf.idx', 'euribor3m', 'nr.employed', 'y'], dtype=object)

# Type of the column from the dataset
bank.dtypes
#Out[6]: 
#age                 int64
#job                object
#marital            object
#education          object
#default            object
#housing            object
#loan               object
#contact            object
#month              object
#day_of_week        object
#duration            int64
#campaign            int64
#pdays               int64
#previous            int64
#poutcome           object
#emp.var.rate      float64
#cons.price.idx    float64
#cons.conf.idx     float64
#euribor3m         float64
#nr.employed       float64
#y                  object
#dtype: object

# Processing the data
# the 'y' column is the customer variable with outcome'yes' and 'no'.
# Convert column to something that can be used, i.e. '1' and '0'
bank['y']=(bank['y']=='yes').astype(int)

# Education column has many categories and needs to be reduced.
bank['education'].unique()

# The basic category has been repeated three times probably to 
# capture 4, 6, and 9 years of education. Let us club these three together 
# and call them basic. Other modified as well.
bank['education']=np.where(bank['education'] =='basic.9y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='basic.6y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='basic.4y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='university.degree', 'University Degree', bank['education'])
bank['education']=np.where(bank['education'] =='professional.course', 'Professional Course', bank['education'])
bank['education']=np.where(bank['education'] =='high.school', 'High School', bank['education'])
bank['education']=np.where(bank['education'] =='illiterate', 'Illiterate', bank['education'])
bank['education']=np.where(bank['education'] =='unknown', 'Unknown', bank['education'])

# Data exploration
# The number of people who purchased the term deposit
bank['y'].value_counts() # Out: Out[12]: [ '0' 3668, '1' 451]

# Many numbers, so lets gets an overview.
bank.groupby('y').mean()
# Categorical means
bank.groupby('education').mean()

# Data visualization

# Tabular data
pd.crosstab(bank.education,bank.y)
# %matplotlib inline
#pd.crosstab(bank.education,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Education Level')
#plt.xlabel('Education')
#plt.ylabel('Frequency of Purchase')

# Stacked bar chart of marital staus and purchase of term deposit.
#table=pd.crosstab(bank.marital,bank.y)
#table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
#plt.title('Stacked Bar Chart of Marital Status vs Purchase')
#plt.xlabel('Marital Status')
#plt.ylabel('Proportion of Customers')

# Bar chart of Purchase Frequency for Day of Week'
#pd.crosstab(bank.day_of_week,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Day of Week')
#plt.xlabel('Day of Week')
#plt.ylabel('Frequency of Purchase')

# Bar chart of Purchase Frequency for Day of Week'
#pd.crosstab(bank.month,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Month of the Year')
#plt.xlabel('Month of the Year')
#plt.ylabel('Frequency of Purchase')

# Histogram of Age
bank.age.hist()
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Creating dummy variables for categorical variables
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(bank[var], prefix=var)
    bank1=bank.join(cat_list)
    bank=bank1
    
# Remove actual categories once dummies have been created
bank_vars=bank.columns.values.tolist()
to_keep=[i for i in bank_vars if i not in cat_vars]

# Subset the bank dataframe to only keep the columns present
bank_final=bank[to_keep]
bank_final.columns.values

# Y outcomes and X predictors can now be calculated
bank_final_vars=bank_final.columns.values.tolist()
Y=['y']
X=[i for i in bank_final_vars if i not in Y ]

# Feature selection    
