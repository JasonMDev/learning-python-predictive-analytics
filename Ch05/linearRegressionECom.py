# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:18:59 2016

@author: jasonm_dev
"""
# Handling other issues in linear regression
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Ecom Expense.csv'
file = filepath+'/'+filename

df=pd.read_csv(file)
df.head()
print(df.shape) #Out: (2362, 9)
# Out: ['Transaction ID', 'Age ', ' Items ', 'Monthly Income', 
# 'Transaction Time', 'Record', 'Gender', City Tier', 'Total Spend']

# Create dummy variables for categorical and qualitive data
dummy_gender=pd.get_dummies(df['Gender'],prefix='Sex')
dummy_city_tier=pd.get_dummies(df['City Tier'],prefix='City')
print(df.shape) #Out: (2362, 9)

# Add dummy variables to the main data
column_name=df.columns.values.tolist()
df1=df[column_name].join(dummy_gender)
column_name1=df1.columns.values.tolist()
df2=df1[column_name1].join(dummy_city_tier)
df2
print(df2.shape) #Out: (2362, 14)

# For the preceding dataset, let's assume a linear relationship between 
# the output variable 'Total Spend' and the predictor variables: 
# 'Monthly Income' and 'Transaction Time', and both set of dummy variables

# Input Variables
feature_cols = ['Monthly Income','Transaction Time','City_Tier 1','City_Tier 2','City_Tier 3','Sex_Female','Sex_Male']
X = df2[feature_cols]
# Output Variable
Y = df2['Total Spend']
lm = LinearRegression()
lm.fit(X,Y)

# Model Parameters
print (lm.intercept_) # Out: 3655.72940769
print (lm.coef_)
# Out: [   0.15297825    0.12372609  119.6632516   -16.67901801 -102.9842336
#  -94.15779883   94.15779883]
zipped = zip(feature_cols, lm.coef_)
list(zipped)
# Out: 
#[('Monthly Income', 0.15297824609320515),
# ('Transaction Time', 0.12372608642620003),
# ('City_Tier 1', 119.66325160390119),
# ('City_Tier 2', -16.679018007990429),
# ('City_Tier 3', -102.98423359591075),
# ('Sex_Female', -94.157798830320132),
# ('Sex_Male', 94.157798830320075)]

# R2 Score
lm.score(X,Y) # Out: 0.19478920552885381

# Model written out:
# Total_Spend=
# 3655.72 + 0.12*Transaction Time + 0.15*Monthly Income 
# + 119*City_Tier 1-16*City_Tier 2 - 102*City_Tier 3
# -94*Sex_Female+94*Sex_Male

# Calculate the RSE
df2['total_spend_pred']=3720.72940769 + 0.12*df2['Transaction Time']+0.15*df2['Monthly Income']+119*df2['City_Tier 1']-16*df2['City_Tier 2']
-102*df2['City_Tier 3']-94*df2['Sex_Female']+94*df2['Sex_Male']
df2['RSE']=(df2['Total Spend']-df2['total_spend_pred'])**2
RSEd=df2.sum()['RSE']
RSE=np.sqrt(RSEd/2354) # 2362 - 7 - 1 = 2354 
salesmean=np.mean(df2['Total Spend'])
error=RSE/salesmean
RSE,salesmean,error
# Out: (2518.8520388731386, 6163.176415976714, 0.40869380800840849)

# IMPROVEMENT
# Mask the first variable from the resulting list using the iloc method of subsetting
dummy_gender=pd.get_dummies(df['Gender'],prefix='Sex').iloc[:, 1:]
dummy_city_tier=pd.get_dummies(df['City Tier'],prefix='City').iloc[:, 1:]
column_name=df.columns.values.tolist()
df3=df[column_name].join(dummy_gender)
column_name1=df3.columns.values.tolist()
df4=df3[column_name1].join(dummy_city_tier)
df4

feature_cols = ['Monthly Income','Transaction Time','City_Tier 2','City_Tier 3','Sex_Male']
X = df2[feature_cols]
Y = df2['Total Spend']
lm = LinearRegression()
lm.fit(X,Y)

# Model Parameters
print (lm.intercept_) # Out: 3681.23486046
print (lm.coef_)
# Out: [  1.52978246e-01   1.23726086e-01  -1.36342270e+02  -2.22647485e+02
#   1.88315598e+02]
zipped = zip(feature_cols, lm.coef_)
list(zipped)
# Out: 
#[('Monthly Income', 0.15297824609320468),
# ('Transaction Time', 0.12372608642590291),
# ('City_Tier 2', -136.34226961189117),
# ('City_Tier 3', -222.6474851998114),
# ('Sex_Male', 188.31559766064038)]
