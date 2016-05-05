# -*- coding: utf-8 -*-
"""
Created on Thu May  5 21:05:23 2016

@author: jasonm_dev
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Advertising.csv'
file = filepath+'/'+filename

advert=pd.read_csv(file)
advert.head()

# SECTION 1: Linear regression using the statsmodel library
# Model Assumption
# A linear relationship between advertising costs on TV and sales
# i.e. Sales = f(TV)= alpha + beta*TV
# Created a best fit using the least sum of square method
model1=smf.ols(formula='Sales~TV',data=advert).fit()
model1.params # Intercept(alpha): 7.032594; TV(beta): 0.047537
model1.pvalues # Intercept(alpha): 1.406300e-35; TV(beta): 1.467390e-42
# p-values are very small, therfore parameters are significant.
model1.rsquared # 0.61187505085007099
model1.summary()
# the F-statistic for this model is very high 
# and the associated p-value is negligible, 
# suggesting that the parameter estimates for this model 
# were all significant and non-zero.

 # Predict the values of sales based on the equation
sales_pred=model1.predict(pd.DataFrame(advert['TV']))
sales_pred

# Calculate RSE term
advert['sales_pred']=0.047537*advert['TV']+7.03
advert['RSE']=(advert['Sales']-advert['sales_pred'])**2
RSEd=advert.sum()['RSE']
RSE=np.sqrt(RSEd/198) # Df Residuals: 198
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(advert['Sales'])
error=RSE/salesmean
RSE,salesmean,error
# (3.2586573692471279, 14.022500000000003, 0.23238776033140504)
# The current model carries a 23% error and the R2 is 0.61 < 0.9

# Plot the Sales predicted vs TV Advertising costs
#%matplotlib inline
advert.plot(kind='scatter', x='TV', y='Sales')
plt.plot(pd.DataFrame(advert['TV']),sales_pred,c='red',linewidth=2)
plt.title('Predicted Sales vs TV Advertising Costs')

# SECTION 2: Multiple linear regression 
