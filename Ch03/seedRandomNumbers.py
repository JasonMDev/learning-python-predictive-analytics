# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:55:21 2016

@author: jasonm_dev
"""
import numpy as np

# No seed is set and a set of new 5 random numbers 
# will be generate each time.
for i in range(5):
    print (np.random.random())

# Seed is set as 1 and generate 5 random numbers.
# The 5 random numbers will be repeated.
np.random.seed(1)
for i in range(5):
    print (np.random.random())
    
