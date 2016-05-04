# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:12:24 2016

@author: jasonm_dev
"""

import pandas as pd
import numpy as np

# Check if first file works.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'Advertising.csv'
file = filepath+'/'+filename

advert=pd.read_csv(file)
advert.head()

# Function to determine correlation between var1 and var2
def corrcoeff(df,var1,var2):
    df['corrn']=(df[var1]-np.mean(df[var1]))*(df[var2]-np.mean(df[var2]))
    df['corrd1']=(df[var1]-np.mean(df[var1]))**2
    df['corrd2']=(df[var2]-np.mean(df[var2]))**2
    corrcoeffn=df.sum()['corrn']
    corrcoeffd1=df.sum()['corrd1']
    corrcoeffd2=df.sum()['corrd2']
    corrcoeffd=np.sqrt(corrcoeffd1*corrcoeffd2)
    corrcoeff=corrcoeffn/corrcoeffd
    return corrcoeff
    
# Correlation between TV and Radio
Corr_TV_Radio = corrcoeff(advert,'TV','Radio') # Out: 0.05480866446583009

# Correlation between TV and Newspaper
Corr_TV_Newspaper = corrcoeff(advert,'TV','Newspaper') # Out: 0.056647874965056993

# Correlation between TV and Sales
Corr_TV_Sales = corrcoeff(advert,'TV','Sales') # Out: 0.78222442486160604

# Correlation between Radio and Newspaper
Corr_Radio_Newspaper = corrcoeff(advert,'Radio','Newspaper') # Out: 0.35410375076117517

# Correlation between Radio and Sales
Corr_Radio_Sales = corrcoeff(advert,'Radio','Sales') # Out: 0.5762225745710553

# Correlation between Newspaper and Sales
Corr_Newspaper_Sales = corrcoeff(advert,'Newspaper','Sales') # Out: 0.22829902637616525

# Plot correlation of TV and Sales
import matplotlib.pyplot as plt
# %matplotlib inline
#plt.plot(advert['TV'],advert['Sales'],'ro')
#plt.title('TV vs Sales')

# Plot correlation of Radio and Sales
#plt.plot(advert['Radio'],advert['Sales'],'ro')
#plt.title('Radio vs Sales')

# Plot correlation of Newspaper and Sales
plt.plot(advert['Newspaper'],advert['Sales'],'ro')
plt.title('Newspaper vs Sales')