# Ruby on Rails Tutorial: Sample Application

These are my notes from working through the book
[*Learning Predictive Analytics with Python*](https://www.packtpub.com/big-data-and-business-intelligence/learning-predictive-analytics-python)
by [Ashish Kumar](https://in.linkedin.com/in/ashishk64)
and published on Feb 2016.

## General
###Chapter 1: Getting Started with Predictive Modelling
- [x] Installed Anaconda Package.
 - [x] Python3.5 has been installed.
 - [x] Book follows python2, so some codes is modified along the way for python3.

###Chapter 2: Data Cleaning
- [x] Reading the data: variations and examples
- [x] Data frames and delimiters.

####Case 1: Reading a dataset using the read_csv method
- [x] File: titanicReadCSV.py
- [x] File: titanicReadCSV1.py
- [x] File: readCustomerChurn.py
- [x] File: readCustomerChurn2.py
- [x] File: changeDelimiter.py

####Case 2: Reading a dataset using the open method of Python
- [x] File: readDatasetByOpenMethod.py

####Case 3: Reading data from a URL
- [x] Modified the code that it works and prints out line by line dictionary of the dataset.
- [x] File: readURLLib2Iris.py
- [x] File: readURLMedals.py

####Case 4: Miscellaneous cases
- [x] File: readXLS.py
- [x] Created the file above to read from both .xls an .xlsx

####Basics: Summary, dimensions, and structure
- [x] File: basicDataCheck.py
- [x] Created the file above to read from both .xls an .xlsx

####Handling missing values
- [x] File: basicDataCheck.py
- [x] RE: Treating missing data like NaN or None
- [x] Deletion orr imputaion

####Creating dummy variables
- [x] File: basicDataCheck.py
- [x] Split into new variable 'sex_female' and 'sex_male'
- [x] Remove column 'sex'
- [x] Add both dummy column created above.

####Visualizing a dataset by basic plotting
- [x] File: plotData.py
- [x] Figure file: ScatterPlots.jpeg
- [x] Plot Types: Scatterplot, Histograms and boxplots

###Chapter 3: Data Wrangling
####Subsetting a dataset
- [x] Selecting Columns
 - [x] File: subsetDataset.py
- [x] Selecting Rows
 - [x] File: subsetDatasetRows.py
- [x] Selecting a combination of rows and columns
 - [x] File: subsetColRows.py
- [x] Creating new columns
 - [x] File: subsetNewCol.py

####Generating random numbers and their usage
- [x] Various methods for generating random numbers
 - [x] File: generateRandomNumbers.py
- [x] Seeding a random number
 - [x] File: generateRandomNumbers.py
- [x] Generating random numbers following probability distributions
 - [x] File: generateRandomProbDistr.py
 - [x] Probability density function: PDF = Prob(X=x)
 - [x] Cumulative density function: CDF(x) = Prob(X<=x)
 - [x] Uniform distribution: random variables occur with the same (uniform) frequency/probability
 - [x] Normal distribution: Bell Curve and most ubiquitous and versatile probability distribution
- [x] Using the Monte-Carlo simulation to find the value of pi
 - [x] File: calcPi.py
 - [x] Geometry and mathematics behind the calculation of pi
- [x] Generating a dummy data frame
 - [x] File: generateDummyDataFrame.py

####Grouping the data – aggregation, filtering, and transformation
- [x] File: groupData.py
- [x] Grouping
- [x] Aggregation
- [x] Filtering
- [x] Transformation
- [x] Miscellaneous operations

####Random sampling – splitting a dataset in training and testing datasets
- [ ] File: splitDataTrainTest.py
 - [x] Method 1: using the Customer Churn Model
 - [x] Method 2: using sklearn
 - [ ] Method 3: using the shuffle function

####Concatenating and appending data
- [x] File: concatenateAndAppend.py
- [x] File: appendManyFiles.py

####Merging/joining datasets
- [x] File: mergeJoin.py
- [x] Inner Join
- [x] Left Join
- [x] Right Join
- [x] An example of the Inner Join
- [x] An example of the Left Join
- [x] An example of the Right Join
- [x] Summary of Joins in terms of their length

###Chapter 4: Statistical Concepts for Predictive Modelling
####Random sampling and central limit theorem
####Hypothesis testing
- [x] Null versus alternate hypothesis
- [x] Z-statistic and t-statistic
- [x] Confidence intervals, significance levels, and p-values
- [x] Different kinds of hypothesis test
- [x] A step-by-step guide to do a hypothesis test
- [x] An example of a hypothesis test

####Chi-square testing
####Correlation
- [x] File: linearRegression.py
- [x] File: linearRegressionFunction.py
- [x] Picture: TVSalesCorrelationPlot.png
- [x] Picture: RadioSalesCorrelationPlot.png
- [x] Picture: NewspaperSalesCorrelationPlot.png

###Chapter 5: Linear Regression with Python
####Understanding the maths behind linear regression
- [x] Linear regression using simulated data
 - [x] File: linearRegression.py
 - [x] Picture: CurrentVsPredicted1.png
 - [x] Picture: CurrentVsPredictedVsMean1.png
 - [x] Picture: CurrentVsPredictedVsModel1.png

####Making sense of result parameters
- [x] File: linearRegression.py
- [x] p-values
- [x] F-statistics
- [x] Residual Standard Error (RSE)

####Implementing linear regression with Python
- [x] File: linearRegressionSMF.py
- [x] Linear regression using the statsmodel library
- [x] Multiple linear regression
- [x] Multi-collinearity: sub-optimal performance of the model
 - [x] Variance Inflation Factor
  - [x]  It is a method to quantify the rise in the variability of the coefficient estimate of a particular variable because of high correlation between two or more than two predictor variables.

####Model validation
- [x] Training and testing data split 
 - [x] File: linearRegressionSMF.py
- [x] Linear regression with scikit-learn
 - [x] File: linearRegressionSKL.py 
- [x] Feature selection with scikit-learn
 - [x] Recursive Feature Elimination (RFE)
 - [x] File: linearRegressionRFE.py

####Handling other issues in linear regression
- [x] Handling categorical variables
 - [x] File: linearRegressionECom.py
- [x] Transforming a variable to fit non-linear relations
 - [x] File: nonlinearRegression.py
 - [x] Picture:  MPGVSHorsepower.png
 - [x] Picture:  MPGVSHorsepowerVsLine.png
 - [x] Picture:  MPGVSHorsepowerModels.png
- [x] Handling outliers
- [x] Other considerations and assumptions for linear regression

###Chapter 6: Logistic Regression with Python
####Linear regression versus logistic regression
####Understanding the math behind logistic regression
- [x] File: logisticRegression.py
- [x] Contingency tables
- [x] Conditional probability
- [x] Odds ratio
- [x] Moving on to logistic regression from linear regression
- [x] Estimation using the Maximum Likelihood Method
 - [x] Building the logistic regression model from scratch
 - [x] File: logisticRegressionScratch.py
 - [ ] Read above again.
- [x] Making sense of logistic regression parameters
 - [x] Wald test
 - [x] Likelihood Ratio Test statistic
 - [x] Chi-square test
- [x]

####Implementing logistic regression with Python
- [x] File: logisticRegressionImplementation.py
- [x] Processing the data
- [x] Data exploration
- [x] Data visualization
- [x] Creating dummy variables for categorical variables
- [x] Feature selection
- [x] Implementing the model

####Model validation and evaluation
- [x] File: logisticRegressionImplementation.py
- [x] Cross validation

####Model validation
- [x] File: logisticRegressionImplementation.py
- [x] The ROC curve {see terms}

###Chapter 7: Clustering with Python 
####Introduction to clustering – what, why, and how?
- [x] What is clustering?
- [x] How is clustering used?
- [x] Why do we do clustering?

####Mathematics behind clustering
- [x] Distances between two observations
 - [x] Euclidean distance
 - [x] Manhattan distance
 - [x] Minkowski distance
 - [x] The distance matrix
- [x] Normalizing the distances
- [x] Linkage methods
 - [x] Single linkage
 - [x] Compete linkage
 - [x] Average linkage
 - [x] Centroid linkage
 - [x] Ward's method uses ANOVA method
- [x] Hierarchical clustering
- [x] K-means clustering
 - [x] File: kMeanClustering.py

####Implementing clustering using Python
- [x] File: clusterWine.py
- [x] Importing and exploring the dataset
- [x] Normalizing the values in the dataset
- [x] Hierarchical clustering using scikit-learn
- [x] K-Means clustering using scikit-learn
 - [x] Interpreting the cluster

####Fine-tuning the clustering 
- [x] The elbow method
- [x] Silhouette Coefficient
- [x] 
- [x] 
- [x] 

