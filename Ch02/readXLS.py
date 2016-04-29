# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:51:11 2016

@author: jasonm_dev
"""
import pandas as pd
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch02'

filename1 = 'titanic3.xls'
filename2 = 'titanic3.xlsx'
fullpath1 = path+'/'+filename1
fullpath2 = path+'/'+filename2
# Read .xls
data1=pd.read_excel(fullpath1,'titanic3')

# Read .xlsx
data2=pd.read_excel(fullpath2,'titanic3')