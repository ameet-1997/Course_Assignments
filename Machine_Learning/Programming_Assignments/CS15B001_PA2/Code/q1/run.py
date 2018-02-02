"""
Performs PCA on 3 dimensional data

Author: Ameet Deshpande
Roll No: CS15B001
"""

import pandas as pd 
from pandas import read_csv
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from tabulate import tabulate
from sklearn.metrics import precision_recall_fscore_support
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from generate_pca_plot import plot_data
from generate_3d_plot import generate_3d

# Load the data and labels
# The data has a very small range and there is thus no need to normalize
train_data = read_csv("../../Dataset/DS3/train.csv", header=None)
train_labels = read_csv("../../Dataset/DS3/train_labels.csv", header=None)
test_data = read_csv("../../Dataset/DS3/test.csv", header=None)
test_labels = read_csv("../../Dataset/DS3/test_labels.csv", header=None)

# 2000 training examples and 400 test examples
# Labels are denoted by 1 and 2
train_size = train_data.shape[0]
compressed_data = pd.concat([train_data, test_data])

# 3D plot
generate_3d()

# Learn the Principal Component using the Training data
features = PCA(n_components=1)
features.fit(train_data)

# Project the training data and test data on the principal component
train_data = features.transform(train_data)
test_data = features.transform(test_data)

# Use a Linear Regressor with indicator variable
# Setting threshold as 1.5 = (1+2)/2
lr = LinearRegression()

# Full Batch Gradient Descent and hence need not worry about shuffling the data
lr.fit(train_data, train_labels)

# Predict the values using the model
threshold = 1.5
pca_predicted_labels = lr.predict(test_data)
pca_predicted_labels[pca_predicted_labels>=threshold] = 2
pca_predicted_labels[pca_predicted_labels<threshold] = 1

# Calculate the evaluations metrics
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, pca_predicted_labels)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2'])

# Plotting the compressed data
plot_data(train_data, test_data, train_labels, test_labels, [float(lr.intercept_[0]), float(lr.coef_[0])]) 