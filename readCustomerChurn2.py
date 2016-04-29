# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:58:48 2016

@author: jasonm_dev
"""
import pandas as pd
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics'
filename1 = 'Customer Churn Columns.csv'
filename2 = 'Customer Churn Model.txt'
fullpath1 = path+'/'+filename1
fullpath2 = path+'/'+filename2


data_columns = pd.read_csv(fullpath1)
data_column_list = data_columns['Column_Names'].tolist()
data=pd.read_csv(fullpath2,header=None,names=data_column_list)
data.columns.values