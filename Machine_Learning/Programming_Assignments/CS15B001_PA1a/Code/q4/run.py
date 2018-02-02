"""
This file has been used to complete assignment part 4 of PA1
Includes imputing the values of the dataset

Author: Ameet Deshpande
RollNo: CS15B001
"""

import pandas as pd
from pandas import read_csv
from sklearn.preprocessing import Imputer

# Load the data by using '?' to denote missing values
# header=None is passed as there are no column names
raw_data = read_csv("CandC.csv", header=None, na_values=["?"])

# The first 5 attributes are not predictive attributes and 
# are nominal and thus are not replaced with their means

# Subset the data to remove the first 5 columns
feature_data = raw_data.loc[:,5:]
raw_data = raw_data.loc[:,0:4]

# axis=0 takes the mean along the columns
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0, verbose=0, copy=True)
feature_data = imputer.fit_transform(feature_data)

# Merge the two dataframes
data = pd.concat([raw_data, pd.DataFrame(feature_data)], axis=1)

# Replace any remaining Nan values (in the first 5 columns) with 0
data.fillna(value=0, inplace=True)

# Write the generated dataset to a csv file
# Do not include header or index
data.to_csv('CandC-generated.csv', header=False, index=False)