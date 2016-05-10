# -*- coding: utf-8 -*-
"""
Created on Tue May 10 20:28:13 2016

@author: jasonm_dev
"""

# Building the logistic regression model from scratch
# Step 1: defining the likelihood function
def likelihood(y,pi):
    import numpy as np
    ll=1
    ll_in=list(range(1,len(y)+1))
    for i in range(len(y)):
        ll_in[i]=np.where(y[i]==1,pi[i],(1-pi[i]))
        ll=ll*ll_in[i]
    return ll
    
# Step 2: calculating probability for each observation
def logitprob(X,beta):
    import numpy as np
    rows=np.shape(X)[0]
    cols=np.shape(X)[1]
    pi=list(range(1,rows+1))
    expon=list(range(1,rows+1))
    for i in range(rows):
        expon[i]=0
        for j in range(cols):
            ex=X[i][j]*beta[j]
            expon[i]=ex+expon[i]
        with np.errstate(divide='ignore', invalid='ignore'):
            pi[i]=np.exp(expon[i])/(1+np.exp(expon[i]))
    return pi
    
# Step 3: Calculate the W diagonal matrix
def findW(pi):
    import numpy as np
    W=np.zeros(len(pi)*len(pi)).reshape(len(pi),len(pi))
    for i in range(len(pi)):
        print (i)
        W[i,i]=pi[i]*(1-pi[i])
        W[i,i].astype(float)
    return W
    
# Step 4: defining the logistic function
def logistic(X,Y,limit):
    import numpy as np
    from numpy import linalg
    nrow=np.shape(X)[0]
    bias=np.ones(nrow).reshape(nrow,1)
    X_new=np.append(X,bias,axis=1)
    ncol=np.shape(X_new)[1]
    beta=np.zeros(ncol).reshape(ncol,1)
    root_diff=np.array(range(1,ncol+1)).reshape(ncol,1)
    iter_i=10000
    while(iter_i>limit):
        print (iter_i, limit)
        pi=logitprob(X_new,beta)
        print (pi)
        W=findW(pi)
        print (W)
        print (X_new)
        print (Y-np.transpose(pi))
        print (np.array((linalg.inv(np.matrix(np.transpose(X_new))*np.matrix(W)*np.matrix(X_new)))*(np.transpose(np.matrix(X_new))*np.matrix(Y-np.transpose(pi)).transpose())))
        print (beta)
        print (type(np.matrix(np.transpose(Y-np.transpose(pi)))) )
        print (np.matrix(Y-np.transpose(pi)).transpose().shape)
        print (np.matrix(np.transpose(X_new)).shape)
        root_diff=np.array((linalg.inv(np.matrix(np.transpose(X_new))*np.matrix(W)*np.matrix(X_new)))*(np.transpose(np.matrix(X_new))*np.matrix(Y-np.transpose(pi)).transpose()))
        beta=beta+root_diff
        iter_i=np.sum(root_diff*root_diff)
        ll=likelihood(Y,pi)
        print (beta)
        print (beta.shape)
    return beta
    
# Testing the model
import numpy as np
X=np.array(range(10)).reshape(10,1)
Y=[0,0,0,0,1,0,1,0,1,1]
bias=np.ones(10).reshape(10,1)
X_new=np.append(X,bias,axis=1)

# Running logistic Regression using our function
a=logistic(X,Y,0.000000001)
ll=likelihood(Y,logitprob(X,a))
#Coefficient of X = 0.66 , Intercept = -3.69

# From stasmodel.api
import statsmodels.api as sm
logit_model=sm.Logit(Y,X_new)
result=logit_model.fit()
print (result.summary())
#Coefficient of X = 0.66, Intercept = -3.69