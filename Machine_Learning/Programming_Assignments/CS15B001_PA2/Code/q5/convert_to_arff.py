"""
Converts the downloaded csv file to arff
format
The attribute names are supplied as the first
row of the data
The columns are reordered as the target variable 
is the first column whereas arff expects it in the
last column

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
import pandas as pd
from pandas import read_csv

# Read the file and store in dataframe
data = read_csv("CSVFiles/mushroom.csv")

# Split the dataset to get test and train dataset
# The last 1124 instances are used as test data
train_data = data.iloc[0:-1124, :]
test_data = data.iloc[-1124:, :]

# Create csv files for arff to load
train_data.to_csv("CSVFiles/mushroom_train.csv", na_rep='?', index=False)
test_data.to_csv("CSVFiles/mushroom_test.csv", na_rep='?', index=False)

# Convert csv files to arff files
# The -B flag is used to set the buffer size. Here set as 10000 because about 8000 rows are present in the file
os.system("java -cp weka-3-8-1/weka.jar weka.core.converters.CSVLoader CSVFiles/mushroom_train.csv >ARFFFiles/mushroom_train.arff -B 10000")
os.system("java -cp weka-3-8-1/weka.jar weka.core.converters.CSVLoader CSVFiles/mushroom_test.csv >ARFFFiles/mushroom_test.arff -B 10000")

# In test file, the last field has a random inverted comma, remove it
# Some attributes in the test data are completely missing, attributes from main
# mushroom file are thus used to copy the same