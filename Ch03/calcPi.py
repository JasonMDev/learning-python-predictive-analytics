# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:26:46 2016

@author: jasonm_dev
"""

# Calculate pi

import numpy as np
import matplotlib.pyplot as plt

def pi_run(nums,loops):
    pi_avg=0
    pi_value_list=[]
    for i in range(loops):
        value=0
        # Generate points within 0 to 1.        
        x=np.random.uniform(0,1,nums).tolist()
        y=np.random.uniform(0,1,nums).tolist()
        # Check to see if they lie within circle.
        for j in range(nums):
            z=np.sqrt(x[j]*x[j]+y[j]*y[j])
            if z<=1:
                value+=1
        # Amount of hits withion circle.        
        float_value=float(value)
        # Using probabilty to calculate pi using hits       
        pi_value=float_value*4/nums
        pi_value_list.append(pi_value)
        # Get pi value for this loop.
        pi_avg+=pi_value
    # Averag pi value from all loops.
    pi=pi_avg/loops
    ind=range(1,loops+1)
    fig=plt.plot(ind,pi_value_list)
    return (pi,fig)
    
pi_run(1000,100)    