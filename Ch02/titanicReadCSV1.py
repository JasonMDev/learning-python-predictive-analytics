# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:55:36 2016

@author: jasonm_dev
"""
import pandas as pd
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch02'
filename = 'titanic3.csv'
fullpath = path+'/'+filename
data = pd.read_csv(fullpath)
