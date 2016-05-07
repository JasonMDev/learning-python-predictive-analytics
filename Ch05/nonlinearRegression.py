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

# Try linear model.
X=data['horsepower'].fillna(data['horsepower'].mean())
Y=data['mpg'].fillna(data['mpg'].mean())
lm=LinearRegression()
lm.fit(X[:,np.newaxis],Y)

# Plot Again
plt.plot(data['horsepower'],data['mpg'],'ro')
plt.plot(X,lm.predict(X[:,np.newaxis]),color='blue')

# R2 score
lm.score(X[:,np.newaxis],Y) # Out: 0.57465334064502505

# Alternative method for RSE
RSEd=(Y-lm.predict(X[:,np.newaxis]))**2
RSE=np.sqrt(np.sum(RSEd)/389)
ymean=np.mean(Y)
error=RSE/ymean
RSE,error # Out: (5.1496254786975237, 0.21899719414044677)

# In the form of mpg = co+a1.horsepower2,
Xp=data['horsepower'].fillna(data['horsepower'].mean())*data['horsepower'].fillna(data['horsepower'].mean())
Yp=data['mpg'].fillna(data['mpg'].mean())
lm2=LinearRegression()
lm2.fit(Xp[:,np.newaxis],Yp)

type(lm2.predict(Xp[:,np.newaxis]))
RSEd=(Yp-lm2.predict(Xp[:,np.newaxis]))**2
RSE=np.sqrt(np.sum(RSEd)/390)
ymean=np.mean(Yp)
error=RSE/ymean
RSE,error,ymean 
# Out: (5.6591995312606125, 0.24066775798625065, 23.51457286432162)

# Attempt polynomial fit with 2 degrees
X2=data['horsepower'].fillna(data['horsepower'].mean())
Y2=data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=2)
X2_ = poly.fit_transform(X2[:,np.newaxis])
clf2 = linear_model.LinearRegression()
clf2.fit(X2_, Y2)

print (clf2.intercept_) # Out: 55.0261924471
print (clf2.coef_) # Out:[ 0. -0.43404318  0.00112615]

# R2 score # R2 = 0.688
clf2.score(X2_,Y2) # Out:  0.6439066584257469


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

# Attempt polynomial fit with 10 degrees
X10=data['horsepower'].fillna(data['horsepower'].mean())
Y10=data['mpg'].fillna(data['mpg'].mean())
poly = PolynomialFeatures(degree=10)
X10_ = poly.fit_transform(X10[:,np.newaxis])
clf10 = linear_model.LinearRegression()
clf10.fit(X10_, Y10)

print (clf10.intercept_) # Out: 38.4429617473
print (clf10.coef_) 
# Out:[  0.00000000e+00  -8.91906448e-10  -7.66530280e-13  -2.72221136e-11
#  -1.29904249e-09  -3.51786115e-08   8.70655852e-10  -8.87303697e-12
#   4.60555310e-14  -1.20912891e-16   1.27851931e-19]

# R2 = 0.7
clf10.score(X10_,Y10) # Out: 0.65235699758560406

# Plot All
plt.plot(data['horsepower'],data['mpg'],'ro')
plt.plot(X,lm.predict(X[:,np.newaxis]),color='blue')
plt.plot(Xp,lm2.predict(Xp[:,np.newaxis]),color='blue')
#plt.plot(X,clf2.predict(X2_[:,np.newaxis]),color='blue')
#plt.plot(X,Y5,color='blue')
#plt.plot(X,Y10,color='blue')

##TODO:

# Add higher degrees fits and plot them.


# R2 = 0.7