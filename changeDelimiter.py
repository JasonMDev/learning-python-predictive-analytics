# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 21:41:13 2016

@author: jasonm_dev
"""
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics'
filename1 = 'Customer Churn Model.txt'
filename2 = 'Tab Customer Churn Model.txt'

infile= path+'/'+filename1
outfile= path+'/'+filename2
with open(infile) as infile1:
  with open(outfile,'w') as outfile1:
    for line in infile1:
      fields=line.split(',')
      outfile1.write('/t'.join(fields))
      
import pandas as pd
data=pd.read_csv(outfile,sep='/t')
print(data)