# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:15:24 2016

@author: jasonm_dev
"""

# Implementing logistic regression with Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Data from CSV file.
filepath = '/home/jasonm_dev/coding/learning-python-predictive-analytics/datasets'
filename= 'bank.csv'
file = filepath+'/'+filename

bank=pd.read_csv(file, sep=';')
bank.head()
print(bank.shape) #Out: (4119, 21)

# Column Names
bank.columns.values

# Out: array(['age', 'job', 'marital', 'education', 'default', 'housing', 'loan',
#       'contact', 'month', 'day_of_week', 'duration', 'campaign', 'pdays',
#       'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx',
#       'cons.conf.idx', 'euribor3m', 'nr.employed', 'y'], dtype=object)

# Type of the column from the dataset
bank.dtypes
#Out[6]: 
#age                 int64
#job                object
#marital            object
#education          object
#default            object
#housing            object
#loan               object
#contact            object
#month              object
#day_of_week        object
#duration            int64
#campaign            int64
#pdays               int64
#previous            int64
#poutcome           object
#emp.var.rate      float64
#cons.price.idx    float64
#cons.conf.idx     float64
#euribor3m         float64
#nr.employed       float64
#y                  object
#dtype: object

# Processing the data
# the 'y' column is the customer variable with outcome'yes' and 'no'.
# Convert column to something that can be used, i.e. '1' and '0'
bank['y']=(bank['y']=='yes').astype(int)

# Education column has many categories and needs to be reduced.
bank['education'].unique()

# The basic category has been repeated three times probably to 
# capture 4, 6, and 9 years of education. Let us club these three together 
# and call them basic. Other modified as well.
bank['education']=np.where(bank['education'] =='basic.9y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='basic.6y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='basic.4y', 'Basic', bank['education'])
bank['education']=np.where(bank['education'] =='university.degree', 'University Degree', bank['education'])
bank['education']=np.where(bank['education'] =='professional.course', 'Professional Course', bank['education'])
bank['education']=np.where(bank['education'] =='high.school', 'High School', bank['education'])
bank['education']=np.where(bank['education'] =='illiterate', 'Illiterate', bank['education'])
bank['education']=np.where(bank['education'] =='unknown', 'Unknown', bank['education'])

# Data exploration
# The number of people who purchased the term deposit
bank['y'].value_counts() # Out: Out[12]: [ '0' 3668, '1' 451]

# Many numbers, so lets gets an overview.
bank.groupby('y').mean()
# Categorical means
bank.groupby('education').mean()

# Data visualization

# Tabular data
pd.crosstab(bank.education,bank.y)
# %matplotlib inline
#pd.crosstab(bank.education,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Education Level')
#plt.xlabel('Education')
#plt.ylabel('Frequency of Purchase')

# Stacked bar chart of marital staus and purchase of term deposit.
#table=pd.crosstab(bank.marital,bank.y)
#table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
#plt.title('Stacked Bar Chart of Marital Status vs Purchase')
#plt.xlabel('Marital Status')
#plt.ylabel('Proportion of Customers')

# Bar chart of Purchase Frequency for Day of Week'
#pd.crosstab(bank.day_of_week,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Day of Week')
#plt.xlabel('Day of Week')
#plt.ylabel('Frequency of Purchase')

# Bar chart of Purchase Frequency for Day of Week'
#pd.crosstab(bank.month,bank.y).plot(kind='bar')
#plt.title('Purchase Frequency for Month of the Year')
#plt.xlabel('Month of the Year')
#plt.ylabel('Frequency of Purchase')

# Histogram of Age
#bank.age.hist()
#plt.title('Histogram of Age')
#plt.xlabel('Age')
#plt.ylabel('Frequency')

# Creating dummy variables for categorical variables
cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
for var in cat_vars:
    cat_list='var'+'_'+var
    cat_list = pd.get_dummies(bank[var], prefix=var)
    bank1=bank.join(cat_list)
    bank=bank1
    
# Remove actual categories once dummies have been created
bank_vars=bank.columns.values.tolist()
to_keep=[i for i in bank_vars if i not in cat_vars]

# Subset the bank dataframe to only keep the columns present
bank_final=bank[to_keep]
bank_final.columns.values

# Y outcomes and X predictors can now be calculated
bank_final_vars=bank_final.columns.values.tolist()
Y=['y']
X=[i for i in bank_final_vars if i not in Y ]

# Feature selection  
# All 12 columns can be selected
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

# Selct a model with 12 variables.
rfe = RFE(model, 12)
rfe = rfe.fit(bank_final[X],bank_final[Y] )

# Print out the support array
print(rfe.support_)
# Print out the ranking
print(rfe.ranking_) 
# The columns with true or 1 shall be selected for the final selection.

# 'previous', 'euribor3m', 'job_entrepreneur', 'job_self-employed', 
# 'poutcome_success', 'poutcome_failure', 'month_oct', 'month_may','month_mar',
# 'month_jun', 'month_jul', 'month_dec' 

# Fit a logistic regression model using the preceding selected variables 
# as predictor variables, with the y as the outcome variable
cols=['previous', 'euribor3m', 'job_entrepreneur', 'job_self-employed', 'poutcome_success', 'poutcome_failure', 'month_oct', 'month_may',
    'month_mar', 'month_jun', 'month_jul', 'month_dec'] 
# Dataframe taht just has the selected columns
X=bank_final[cols]
Y=bank_final['y']

# Implementing the model
import statsmodels.api as sm
logit_model=sm.Logit(Y,X)
result=logit_model.fit()
print (result.summary())

# The statsmodel.api method can be used while exploring and fine-tuning the model.
# One advantage of this method is that p-values are calculated automatically 
# in the result summary. 
# The scikit-learn method can be used in the final model used to predict the outcome.
# The scikit-learn method doesn't have this facility, 
# but is more powerful for calculation-intensive tasks such as prediction, 
# calculating scores, and advanced functions such as feature selection. 

# Fit the model
from sklearn import linear_model
clf = linear_model.LogisticRegression()
clf.fit(X, Y)

# Calculate the accuracy
clf.score(X,Y) #Out = 0.90216071862102454
# The value comes out to be .902. The mean value of the outcome is .11, 
# meaning that the outcome is positive (1) around 11% of the time and negative 
# around 89% of the time. 

# Get the values of the coefficients
zipped = list(zip(X.columns, np.transpose(clf.coef_)))
pd.DataFrame(zipped)

# Out: 
#                    0                  1
#0            previous   [0.379831612876]
#1           euribor3m  [-0.502749071837]
#2    job_entrepreneur  [-0.343066155888]
#3   job_self-employed  [-0.335064163493]
#4    poutcome_success    [1.07783253323]
#5    poutcome_failure  [-0.753161867894]
#6           month_oct   [0.411855745929]
#7           month_may  [-0.743089630936]
#8           month_mar     [1.2703612295]
#9           month_jun   [0.509694983142]
#10          month_jul   [0.382087449085]
#11          month_dec   [0.873316799315]

# Model validation and evaluation
# Split into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Build a logistic regression model ove the training dataset
from sklearn import linear_model
from sklearn import metrics
clf1 = linear_model.LogisticRegression()
clf1.fit(X_train, Y_train)

# Get probalities and classifications
probs = clf1.predict_proba(X_test)

# Out: [ Negative, Positive]
# array([[ 0.93352157,  0.06647843],
#       ..., 
#       [ 0.24746608,  0.75253392]])

# Get predicted outcomes
predicted = clf1.predict(X_test)
print(predicted) # Out: [0 0 0 ..., 0 0 1]
# Default cut off is at 0.5.
# We saw that 10% of customers brought product, hence 0.1 cut-off.

# Changing the threshold value
prob=probs[:,1] # Take second column, i.e. positive outcomes
prob_df=pd.DataFrame(prob) # Push to dataframe
prob_df['predict']=np.where(prob_df[0]>=0.10,1,0) 
prob_df.head() 
# [ @0.1 => 28%, @0.15 => 18%, @0.05 => 65%]

# Accuracy of the model
print (metrics.accuracy_score(Y_test, predicted)) # Out: 0.902103559871

# Cross validation
# Using the k-fold method
# Use a 8-fold cross validation method
# CAlculates the accuracy of each iteration
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(linear_model.LogisticRegression(), X, Y, scoring='accuracy', cv=8)
print (scores)
# Out: [ 0.91860465  0.90310078  0.89534884  0.90679612  0.89883268  
# 0.89299611  0.90466926  0.89883268]
print (scores.mean()) # Out: 0.902397639921


# Model Validation
# ROC Curve
# Run model and calculate the probabilities for each observation
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
clf1 = linear_model.LogisticRegression()
clf1.fit(X_train, Y_train)
probs = clf1.predict_proba(X_test)

# Each probable value is compared to threshold probability and categorized as 
# 1 (postive outcome)
prob=probs[:,1]
prob_df=pd.DataFrame(prob)
prob_df['predict']=np.where(prob_df[0]>=0.05,1,0)
prob_df['actual']=Y_test #TODO: Comes out as NAN 
prob_df.head()

# Confusion matrix
confusion_matrix=pd.crosstab(prob_df['actual'],prob_df['predict'])
confusion_matrix

# Plot ROC curve manually

#%matplotlib inline
Sensitivity=[1,0.95,0.87,0.62,0.67,0.59,0.5,0.41,0]
FPR=[1,0.76,0.62,0.23,0.27,0.17,0.12,0.07,0]
#plt.plot(FPR,Sensitivity,marker='o',linestyle='--',color='r')
x=[i*0.01 for i in range(100)]
y=[i*0.01 for i in range(100)]
#plt.plot(x,y)
#plt.xlabel('(1-Specificity)')
#plt.ylabel('Sensitivity')
#plt.title('ROC Curve')

# Using scikit-learn package to plot the ROC Curve
#TODO: 
from sklearn import metrics
from ggplot import *

prob = clf1.predict_proba(X_test)[:,1]
fpr, sensitivity, _ = metrics.roc_curve(Y_test, prob)

df = pd.DataFrame(dict(fpr=fpr, sensitivity=sensitivity))
ggplot(df, aes(x='fpr', y='sensitivity')) + geom_line() +\
    geom_abline(linetype='dashed')
    
# Area under the curve
auc = metrics.auc(fpr,sensitivity)
auc    

# Area under curve can be plotted.
ggplot(df, aes(x='fpr', ymin=0, ymax='sensitivity')) +\
    geom_area(alpha=0.2) +\
    geom_line(aes(y='sensitivity')) +\
    ggtitle("ROC Curve w/ AUC=%s" % str(auc))
    
