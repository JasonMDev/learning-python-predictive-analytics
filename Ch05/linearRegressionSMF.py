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
# Model 1: A linear relationship between advertising costs on TV and sales
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

# Calculate RSE term for model 1
advert['sales_pred']=0.047537*advert['TV']+7.03
advert['RSE']=(advert['Sales']-advert['sales_pred'])**2
RSEd=advert.sum()['RSE']
RSE=np.sqrt(RSEd/198) # # Df Residuals (n-p-1): 200-1-1 = 198 
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(advert['Sales'])
error=RSE/salesmean
RSE,salesmean,error
# (3.2586573692471279, 14.022500000000003, 0.23238776033140504)
# The current model carries a 23% error and the R2 is 0.61 < 0.9
# F-statistic: 312.1

# Plot the Sales predicted vs TV Advertising costs
#%matplotlib inline
advert.plot(kind='scatter', x='TV', y='Sales')
plt.plot(pd.DataFrame(advert['TV']),sales_pred,c='red',linewidth=2)
plt.title('Predicted Sales vs TV Advertising Costs')


# SECTION 2: Multiple linear regression 
# Model 2: 
# Sales = f(TV,Newspaper)= alpha + beta1*TV+ beta2*Newspaper
model2=smf.ols(formula='Sales~TV+Newspaper',data=advert).fit()
model2.params 
# Intercept(alpha): 5.774948; TV(beta1): 0.046901; Newspaper(beta2): 0.044219
model2.pvalues 
# Intercept(alpha): 3.145860e-22; TV(beta1): 5.507584e-44; 
# Newspaper(beta2): 2.217084e-05
# p-values are very small, therfore parameters are significant.
model2.rsquared # 0.64583549382932715
model2.summary()

 # Predict the values of sales based on the equation of model 2
sales_pred2=model2.predict(advert[['TV','Newspaper']])
sales_pred2

# Calculate RSE term for model 2
advert['sales_pred2']=5.77 + 0.046*advert['TV'] + 0.04*advert['Newspaper']
advert['RSE2']=(advert['Sales']-advert['sales_pred2'])**2
RSEd2=advert.sum()['RSE2']
RSE2=np.sqrt(RSEd2/197) # Df Residuals (n-p-1): 200-2-1 = 197 
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(advert['Sales'])
error2=RSE2/salesmean
RSE2,salesmean,error2
# (3.1346969895743846, 14.022500000000003, 0.22354765481008265)
# The current model carries a 22% error and the R2 is 0.64 < 0.9
# F-statistic: 179.6


# Model 3: 
# Sales = f(TV,Radio)= alpha + beta1*TV+ beta2*Radio
model3=smf.ols(formula='Sales~TV+Radio',data=advert).fit()
model3.params 
# Intercept(alpha): 2.921100; TV(beta1): 0.045755; Radio(beta2): 0.187994
model3.pvalues 
# Intercept(alpha): 4.565557e-19; TV(beta1): 5.436980e-82; 
# Radio(beta2): 9.776972e-59
# p-values are very small, therfore parameters are significant.
model3.rsquared # 0.89719426108289568
model3.summary()

 # Predict the values of sales based on the equation of model 3
sales_pred3=model3.predict(advert[['TV','Radio']])
sales_pred3

# Calculate RSE term for model 3
advert['sales_pred3']=2.92 + 0.045*advert['TV'] + 0.18*advert['Radio']
advert['RSE3']=(advert['Sales']-advert['sales_pred3'])**2
RSEd3=advert.sum()['RSE3']
RSE3=np.sqrt(RSEd3/197) # Df Residuals (n-p-1): 200-2-1 = 197 
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(advert['Sales'])
error3=RSE3/salesmean
RSE3,salesmean,error3
# (1.7136206211553162, 14.022500000000003, 0.12220507193120456)
# The current model carries a 12% error and the R2 is 0.89 < 0.9
# F-statistic: 859.6 =>  indicating a very efficient model.


# Model 4: 
# Sales = f(TV,Radio)= alpha + beta1*TV + beta2*Radio + beta3*Newspaper
model4=smf.ols(formula='Sales~TV+Radio+Newspaper',data=advert).fit()
model4.params 
# Intercept(alpha): 2.938889; TV(beta1): 0.045765; 
# Radio(beta2): 0.188530; Newspaper(beta3): -0.001037
model4.pvalues 
# Intercept(alpha): 1.267295e-17; TV(beta1): 1.509960e-81; 
# Radio(beta2): 1.505339e-54; Newspaper(beta3): 8.599151e-01
# p-values are very small, therfore parameters are significant.
model4.rsquared # 0.89721063817895219
model4.summary()

# Predict the values of sales based on the equation of model 4
sales_pred4=model4.predict(advert[['TV','Radio','Newspaper']])
sales_pred4

# Calculate RSE term for model 4
advert['sales_pred4']=2.938 + 0.045*advert['TV'] + 0.188*advert['Radio'] - 0.001*advert['Newspaper']
advert['RSE4']=(advert['Sales']-advert['sales_pred4'])**2
RSEd4=advert.sum()['RSE4']
RSE4=np.sqrt(RSEd4/196) # Df Residuals (n-p-1): 200-3-1 = 196
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(advert['Sales'])
error4=RSE4/salesmean
RSE4,salesmean,error4
# (1.691523011857319, 14.022500000000003, 0.12062920391209261)
# The current model carries a 12% error and the R2 is 0.89 < 0.9
# F-statistic: 570.3 =>  
# This suggests that the partial benefit of adding newspaper to the model 
# containing TV and radio is negative.
# RSE does not increase as book says. It decreases from 1.71 to 1.69.


# Multi-collinearity
# Calculate the Variance Inflation Factor
# It is a method to quantify the rise in the variability of the coefficient 
# estimate of a particular variable because of high correlation between two or
# more than two predictor variables.

# VIF for the Newspaper
modelVIF1=smf.ols(formula='Newspaper~TV+Radio',data=advert).fit()
rsquared1=modelVIF1.rsquared 
VIF1=1/(1-rsquared1)
VIF1 # Out: 1.1451873787239286

# VIF for the Radio
modelVIF2=smf.ols(formula='Radio~TV+Newspaper',data=advert).fit()
rsquared2=modelVIF2.rsquared 
VIF2=1/(1-rsquared2)
VIF2 # Out: 1.1449519171055353

# VIF for the TV
modelVIF3=smf.ols(formula='TV~Newspaper+Radio',data=advert).fit()
rsquared3=modelVIF3.rsquared 
VIF3=1/(1-rsquared3)
VIF3 # Out: 1.0046107849396502

# Summary:
# Newspaper and Radio have the same VIF and are thus correlated with one another.
# Model 3 with TV and Radio is superior to Model 2 with TV and Newspaper.
# Model 4 with all 3 variable is actually weaker than Model 3.

# Training and testing data split
a=np.random.randn(len(advert))
check=a<0.8
training=advert[check] # Out: 152
testing=advert[~check] # Out: 48

# Model 5: [model will changeeach time its run because of random generator.]
# Sales = f(TV,Radio)= alpha + beta1*TV+ beta2*Radio
model5=smf.ols(formula='Sales~TV+Radio',data=training).fit()
model5.params 
# Intercept(alpha): 2.771009; TV(beta1): 0.047188; Radio(beta2): 0.185030
model5.pvalues 
# Intercept(alpha): 6.613587e-13; TV(beta1): 2.625145e-62; 
# Radio(beta2): 1.803356e-41
# p-values are very small, therfore parameters are significant.
model5.rsquared # 0.89415688916044844
model5.summary() # F-statistic: 629.4 

# Predict the values of sales based on the equation of model 5 using testing data
sales_pred5=model5.predict(training[['TV','Radio']])
sales_pred5

# Calculate RSE term for model 5
testing['sales_pred5']=2.7710 + 0.0472*testing['TV'] + 0.1850*testing['Radio']
testing['RSE5']=(testing['Sales']-testing['sales_pred5'])**2
RSEd5=testing.sum()['RSE5']
RSE5=np.sqrt(RSEd5/45) # len(testing) = 48; (n-p-1): 48-2-1 = 45
# [1/(n-p-1)]:n=number of data points;p=number of predictor variables
salesmean=np.mean(testing['Sales'])
error5=RSE5/salesmean
RSE5,salesmean,error5
# (1.4032428224556619, 14.120833333333335, 0.099373938444779819)
# The current model carries a 11% error and the R2 is 0.89 < 0.9 