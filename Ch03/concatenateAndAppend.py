# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:50:48 2016

@author: jasonm_dev
"""

import pandas as pd

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename_red = 'winequality-red.csv'
filename_white = 'winequality-white.csv'
fullpath_red = path+'/'+filename_red
fullpath_white = path+'/'+filename_white

# RED WINE QUALITIES


data1=pd.read_csv(fullpath_red,sep=';') # delimiter is ';'
data1.head() 
data1.shape #Out: (1599, 12)
data1.columns.values 
# Out: array(['fixed acidity', 'volatile acidity', 'citric acid',
#   'residual sugar', 'chlorides', 'free sulfur dioxide',
#   'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
#   'quality'], dtype=object)

# WHITE WINE QUALITIES
data2=pd.read_csv(fullpath_white,sep=';')
data2.shape #Out: (4898, 12)
data2.head() 

# APPEND DATA
# Horizontal axis is denoted by 0.
wine_total=pd.concat([data1,data2],axis=0)
wine_total.shape #Out: (6497, 12)
wine_total.head()

#SCRAMBLING DATA WITH CONCAT
data1_head=data1.head(50)
data1_middle=data1[500:550]
data1_tail=data1.tail(50)
wine_scramble=pd.concat([data1_middle,data1_head,data1_tail],axis=0)
wine_scramble
wine_scramble.shape #Out: (150, 12)