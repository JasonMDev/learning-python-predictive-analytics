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
####SubChapter
- [ ] Section
 - [ ] File:
 - [ ] SubSection
- [x] 
- [x] 
- [x] 
- [x] 