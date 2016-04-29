# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:58:48 2016

@author: jasonm_dev

python2 uses next()
python3 uses readline()
"""

path = '/home/jasonm_dev/coding/learning-python-predictive-analytics'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename

# Open file in read mode.
data=open(fullpath,'r')
# readline() method:
# -> It navigates the computer memory to the line next to the header.
# strip() method: 
# -> Removes all the trailing and leading blank spaces from the line
# split() method: 
# -> Method breaks down a line into chunks separated by the argument provided
cols=data.readline().strip().split(',')
no_cols=len(data.readline().strip().split(','))

counter=0

main_dict={}
# Key: Column names
# Value: Values of columns. 
for col in cols:
    main_dict[col]=[]
    
for line in data:
    values = line.strip().split(',')
    for i in range(len(cols)):
        main_dict[cols[i]].append(values[i])
    counter += 1

#print ("The dataset has %d rows and %d columns") % (counter,no_cols)
print ('The dataset has ',counter,' rows and ',no_cols,' columns')

# Convert dataset to a dataframe similar pandas raed_csv
import pandas as pd
df=pd.DataFrame(main_dict)
print (df.head(10))