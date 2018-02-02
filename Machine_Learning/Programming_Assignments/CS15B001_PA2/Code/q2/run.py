"""
Performs LDA on 3 dimensional data

Author: Ameet Deshpande
Roll No: CS15B001
"""

import pandas as pd 
from pandas import read_csv
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LinearRegression
from tabulate import tabulate
from sklearn.metrics import precision_recall_fscore_support
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from generate_lda_plot import plot_data
from generate_3d_plot import generate_3d

# Load the data and labels
# The data has a very small range and there is thus no need to normalize
train_data = read_csv("../../Dataset/DS3/train.csv", header=None)
train_labels = read_csv("../../Dataset/DS3/train_labels.csv", header=None)
test_data = read_csv("../../Dataset/DS3/test.csv", header=None)
test_labels = read_csv("../../Dataset/DS3/test_labels.csv", header=None)

# Plot the 3D data
generate_3d()

# Fit the training data to get a dimension to project the data
LDA = LinearDiscriminantAnalysis(solver='svd', n_components=None)	# SVD Solver, one feature is learnt
LDA.fit(train_data, np.array(train_labels).flatten())

# Project the training and test data on the dimension
train_data = LDA.transform(train_data)
test_data = LDA.transform(test_data)

# Use a Linear Regressor with indicator variable
# Setting threshold as 1.5 = (1+2)/2
lr = LinearRegression()

# Full Batch Gradient Descent and hence need not worry about shuffling the data
lr.fit(train_data, train_labels)

# Predict the values using the model
threshold = 1.5
lda_predicted_labels = lr.predict(test_data)
lda_predicted_labels[lda_predicted_labels>=threshold] = 2
lda_predicted_labels[lda_predicted_labels<threshold] = 1

# Calculate the evaluations metrics
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, lda_predicted_labels)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2'])

# Plotting the compressed data
plot_data(train_data, test_data, train_labels, test_labels, [float(lr.intercept_[0]), float(lr.coef_[0])])