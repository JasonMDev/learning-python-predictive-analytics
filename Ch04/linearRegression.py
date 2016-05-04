
# -*- coding: utf-8 -*-
# Linear Regression
"""
Created on Wed May  4 21:08:54 2016

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

# Determine correlation between 
# the advertisement costs on TV 
# and the resultant sales
advert['corrn']=(advert['TV']-np.mean(advert['TV']))*(advert['Sales']-np.mean(advert['Sales']))
advert['corrd1']=(advert['TV']-np.mean(advert['TV']))**2
advert['corrd2']=(advert['Sales']-np.mean(advert['Sales']))**2
corrcoeffn=advert.sum()['corrn']
corrcoeffd1=advert.sum()['corrd1']
corrcoeffd2=advert.sum()['corrd2']
corrcoeffd=np.sqrt(corrcoeffd1*corrcoeffd2)
corrcoeff=corrcoeffn/corrcoeffd
corrcoeff #Out: 0.78222442486160604