# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:08:00 2016

@author: jasonm_dev
"""


import pandas as pd

# Check if first file works.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets/lotsofdata'
filename= '001.csv'
file = filepath+'/'+filename

data=pd.read_csv(file)
data.head()
data.shape #Out: (1461, 4)

# Loop through all dataset files.
data_final=pd.read_csv(file)
data_final_size=len(data_final)
for i in range(1,12): #range(1,333):
    if i<10:
        filename='0'+'0'+str(i)+'.csv'
    if 10<=i<100:
        filename='0'+str(i)+'.csv'
    #if i>=100:
    #    filename=str(i)+'.csv'
        
    file=filepath+'/'+filename
    data=pd.read_csv(file)
    data_final_size+=len(data)
    data_final=pd.concat([data_final,data],axis=0)
    
data.shape # Out: (1461, 4)
data_final.shape # Out: (27391, 4)
print (data_final_size) # 27391