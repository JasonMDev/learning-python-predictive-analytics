# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:56:09 2016

@author: jasonm_dev
"""

# Transforming a variable to fit non-linear relations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Auto.csv'
file = filepath+'/'+filename

data=pd.read_csv(file)
data.head()
print(data.shape) #Out: (406, 9)

# Plot data to check linearity
#%matplotlib inline
data['mpg']=data['mpg'].dropna()
data['horsepower']=data['horsepower'].dropna()
plt.plot(data['horsepower'],data['mpg'],'ro')
plt.xlabel('Horsepower')
plt.ylabel('MPG (Miles Per Gallon)')

# Model 1
# Try linear model.
# MPG = co + alpha*HP
X=data['horsepower'].fillna(data['horsepower'].mean())
Y=data['mpg'].fillna(data['mpg'].mean())
lm=LinearRegression()
lm.fit(X[:,np.newaxis],Y)

# Plot Again
#plt.plot(data['horsepower'],data['mpg'],'ro')
#plt.plot(X,lm.predict(X[:,np.newaxis]),color='blue')

# R2 score
lm.score(X[:,np.newaxis],Y) # Out: 0.57465334064502505

# Alternative method for RSE
RSEd=(Y-lm.predict(X[:,np.newaxis]))**2
RSE1=np.sqrt(np.sum(RSEd)/389)
ymean=np.mean(Y)
error1=RSE1/ymean
RSE1,error1 # Out: (5.1496254786975237, 0.21899719414044677)

# Model 2
# In the form of mpg = co+a1.horsepower**2,
X2=data['horsepower'].fillna(data['horsepower'].mean())*data['horsepower'].fillna(data['horsepower'].mean())
Y2=data['mpg'].fillna(data['mpg'].mean())
lm2=LinearRegression()
lm2.fit(X2[:,np.newaxis],Y2)

type(lm2.predict(X2[:,np.newaxis]))
RSEd=(Y2-lm2.predict(X2[:,np.newaxis]))**2
RSE2=np.sqrt(np.sum(RSEd)/390)
ymean=np.mean(Y2)
error2=RSE2/ymean
RSE2,error2,ymean 
# Out: (5.6591995312606125, 0.24066775798625065, 23.51457286432162)

# R2 score
lm2.score(X2[:,np.newaxis],Y2) # Out: 0.48498870348232048

print (lm2.intercept_) # Out: 30.405683105
print (lm2.coef_) # Out:[ 0. -0.43404318  0.00112615]

# Model 3
# Attempt polynomial fit with 2 degrees
X3=data['horsepower'].fillna(data['horsepower'].mean())
Y3=data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=2)
X3_ = poly.fit_transform(X3[:,np.newaxis])
clf3 = linear_model.LinearRegression()
clf3.fit(X3_, Y3)

print (clf3.intercept_) # Out: 55.0261924471
print (clf3.coef_) # Out: [-0.00055043]

# R2 score # R2 = 0.688
clf3.score(X3_,Y3) # Out:  0.6439066584257469

# Model 4
# Attempt polynomial fit with 5 degrees
X5=data['horsepower'].fillna(data['horsepower'].mean())
Y5=data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=5)
X5_ = poly.fit_transform(X5[:,np.newaxis])
clf5 = linear_model.LinearRegression()
clf5.fit(X5_, Y5)

print (clf5.intercept_) # Out: -40.6939920548
print (clf5.coef_) 
# Out:[  0.00000000e+00   4.00021890e+00  -7.54802463e-02   6.19621638e-04
#  -2.36220983e-06   3.41983064e-09]

# R2 = 0.7
clf5.score(X5_,Y5) # Out: 0.6547512491826567


# Plot All
XP = np.arange(45,248,0.5)
M2 = 30.405683105 -0.00055043*XP**2
M3 = 55.0261924471 - 0.43404318*XP + 0.00112615*XP**2
M4 = -40.6939920548 + 4.00021890e+00*XP -7.54802463e-02*XP**2 + 6.19621638e-04*XP**3 -2.36220983e-06*XP**4 + 3.41983064e-09*XP**5

plt.plot(data['horsepower'],data['mpg'],'ro') # Actual Data
plt.plot(XP,lm.predict(XP[:,np.newaxis]),color='magenta')
plt.plot(XP,M2,color='blue') # Model 2
plt.plot(XP,M3,color='green') # Model 3
plt.plot(XP,M4,color='yellow') # Model 4