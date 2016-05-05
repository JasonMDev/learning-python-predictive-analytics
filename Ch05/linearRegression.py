# -*- coding: utf-8 -*-
"""
Created on Thu May  5 20:26:46 2016

@author: jasonm_dev
"""
# LINEAR REGRESSION

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# Input_Variable(X)
# 100 normally distributed random numbers 
# with a mean of 1.5, and standard deviation 2.5
x=2.5*np.random.randn(100)+1.5

# Residual term (RES) which israndom variable distributed normally  
# with a mean of 0 and  standard deviation of 0.5.
res=.5*np.random.randn(100)+0

# Predicted Value (Ye)
# i.e. Predicted_Output(ypred)
# Intercept of 2 and a slope of 0.3
ypred=2+.3*x

# Actual Value (Ya)
# i.e. Actual_Output(yact)
# We add the random residual.
yact=2+.3*x+res

# Create a dataframe with above lists.
xlist=x.tolist() # Convert datatype 'numpy.ndarray' to a 'list'
ypredlist=ypred.tolist() # Convert datatype 'numpy.ndarray' to a 'list'
yactlist=yact.tolist() # Convert datatype 'numpy.ndarray' to a 'list'
# Convert lists to a dataframe.
df=pd.DataFrame({'Input_Variable(X)':xlist,'Predicted_Output(ypred)':ypredlist,'Actual_Output(yact)':yactlist})
df.head()

# Get the mean of the actual data.
ymean=np.mean(yact)
yavg=[ymean for i in range(1,len(xlist)+1)]


# Calculation of the R-squared or coefficient of determination
# A way to judge the efficacy of the model
# Total Sum of Squares (SST) = SSD + SSR = f(yact-yavg)
# Difference Sum of Squares or SSD = f(yact-ypred)
# Regression Sum of Squares or SSR = f(ypred-yavg)
df['SSR']=(df['Predicted_Output(ypred)']-ymean)**2
df['SST']=(df['Actual_Output(yact)']-ymean)**2
SSR=df.sum()['SSR']
SST=df.sum()['SST']
SSR/SST # Out: 0.7354410334035838

# Calculating alpha and beta coefficients
xmean=np.mean(df['Input_Variable(X)'])
ymean=np.mean(df['Actual_Output(yact)'])
df['beta']=(df['Input_Variable(X)']-xmean)*(df['Actual_Output(yact)']-ymean)
df['xvar']=(df['Input_Variable(X)']-xmean)**2
betan=df.sum()['beta']
betad=df.sum()['xvar']
beta=betan/betad

alpha=ymean-(betan/betad)*xmean
beta,alpha # beta : 0.29063 alpha: 2.04474

# Generate new colum to incoporate our new parameters or coefficients
df['ymodel']=beta*df['Input_Variable(X)']+alpha

# Calculation of the R-squared or coefficient of determination
# for the new model.
df['SSR']=(df['ymodel']-ymean)**2
df['SST']=(df['Actual_Output(yact)']-ymean)**2
SSR2=df.sum()['SSR']
SST2=df.sum()['SST']
SSR2/SST2

# Plot the current model.
plt.plot(x,ypred)
plt.plot(x,df['ymodel'])
plt.plot(x,yact,'ro')
plt.plot(x,yavg)
plt.title('Actual vs Predicted vs Model')

# Residual Standard Error (RSE)
df['RSE']=(df['Actual_Output(yact)']-df['ymodel'])**2
RSEd=df.sum()['RSE']
RSE=np.sqrt(RSEd/98) 
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
RSE