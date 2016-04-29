# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:49:07 2016

@author: jasonm_dev
"""

import pandas as pd
import matplotlib.pyplot as plt
#from pylab import figure, axes, pie, title, show
path = '/home/jasonm_dev/coding/learning-python-predictive-analytics/Ch02'
filename = 'Customer Churn Model.txt'
fullpath = path+'/'+filename
data=pd.read_csv(fullpath)

# Scatter plot
data.plot(kind='scatter',x='Day Mins',y='Day Charge')

# Using matplotlib
#figure,axs = plt.subplots(2, 2,sharey=True,sharex=True)
#data.plot(kind='scatter',x='Day Mins',y='Day Charge',ax=axs[0][0])
#data.plot(kind='scatter',x='Night Mins',y='Night Charge',ax=axs[0][1])
#data.plot(kind='scatter',x='Day Calls',y='Day Charge',ax=axs[1][0])
#data.plot(kind='scatter',x='Night Calls',y='Night Charge',ax=axs[1][1])

# Save figure as a jpeg
#figname = 'ScatterPlots.jpeg'
#figpath = path+'/'+filename
#figure.savefig(figname)

# Histograms
#plt.hist(data['Day Calls'],bins=8)
#plt.xlabel('Day Calls Value')
#plt.ylabel('Frequency')
#plt.title('Frequency of Day Calls')

# Boxplots
plt.boxplot(data['Day Calls'])
plt.ylabel('Day Calls')
plt.title('Box Plot of Day Calls')