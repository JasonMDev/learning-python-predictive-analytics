# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 09:51:41 2016

@author: jasonm_dev
"""

import csv
import urllib.request
import codecs

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
html = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(html, 'utf-8'))
for line in csvfile:
    print(line) #do something with line