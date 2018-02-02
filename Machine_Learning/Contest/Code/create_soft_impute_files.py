import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
import time
from fancyimpute import KNN, SoftImpute, MICE

# Load and impute the data using the mean
train_data = pd.read_csv("../Data/train.csv")

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,1:-1]

# Get test data
test_data = pd.read_csv("../Data/test.csv").iloc[:,1:]

print("Before imputation :: "+str(train_data.shape)+" :: "+str(test_data.shape))

# Convert the whole data into one stack
train_data_size = train_data.shape[0]
total_data = pd.concat([train_data, test_data])
total_data = pd.DataFrame(MICE().complete(total_data))

# Subset back the data
train_data = total_data.iloc[:train_data_size,:]
test_data = total_data.iloc[train_data_size:,:]

print("After imputation :: "+str(train_data.shape)+" :: "+str(test_data.shape))

# Write to files
train_data.to_csv("train_MICE.csv", header=None, index=False)
test_data.to_csv("test_MICE.csv", header=None, index=False)