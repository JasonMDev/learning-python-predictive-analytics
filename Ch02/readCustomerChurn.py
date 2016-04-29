# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:58:48 2016

@author: jasonm_dev
"""
import pandas as pd
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch02'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data = pd.read_csv(fullpath)