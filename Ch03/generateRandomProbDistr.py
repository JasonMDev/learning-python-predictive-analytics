# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:01:52 2016

@author: jasonm_dev
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate 100 random numbers lying between 1 and 100.
randnum=np.random.uniform(1,100,100)

# Plot histogram to confirm uniform distribution.
# Used with ipython/spyder notepad.
#%matplotlib inline

# Not so uniform distribution with 10 numbers
a=np.random.uniform(1,100,100)
b=range(1,101)
#plt.hist(a)

# Better uniform distribution with a million numbers
c=np.random.uniform(1,1000000,1000000)
d=range(1,101)
#plt.hist(c)

# Normal distribution
# Used with ipython/spyder notepad.
#%matplotlib inline

# Plot a random noise plot.
e=np.random.randn(100)
f=range(1,101)
#plt.plot(f,e)

# Plot a random noise plot with mean of 1.5 and standard deviation of 2.5.
g=2.5*np.random.randn(100)+1.5
h=range(1,101)
#plt.plot(h,g)

# Generate enough numbers to create belll curve
i=np.random.randn(100000)
j=range(1,101)
plt.hist(i)