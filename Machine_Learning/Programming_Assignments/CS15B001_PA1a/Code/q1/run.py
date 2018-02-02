"""
This file has been used to complete assignment parts 1,2,3 of PA1
Includes generation of synthetic data, learning Linear and KNN classifiers
and getting the accuracy values

Author: Ameet Deshpande
RollNo: CS15B001
"""

import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier


# Create a diagonal covariance matrix by sampling numbers from a range 1-40
# The variables in this case will thus be independent of each other
diagonal_covariance = np.array(random.sample(xrange(1,40), 20))
diagonal_covariance_matrix = np.diagflat(diagonal_covariance)

# Choose the centers for the classes
# Class 1 is centered at [0,..0] and class 2 at overlap*diagonal_covariance
# A overlap value of 0.1 gives an accuracy score of 80%
# A overlap value of 0.2 gives an accuracy score of 96%
b = 0.2
a = 0.1
overlap_array = np.random.random_sample(20)*(b-a) + a
class1_center = np.zeros(20, dtype=float)
class2_center = overlap_array*diagonal_covariance

# Generate random data using Multivariate Gaussian
class1_data = np.random.multivariate_normal(mean=class1_center, cov=diagonal_covariance_matrix, size=2000)
class2_data = np.random.multivariate_normal(mean=class2_center, cov=diagonal_covariance_matrix, size=2000)

# Split the two classes into 0.7-0.3 train-test dataset
class1_train, class1_test, class2_train, class2_test = train_test_split(class1_data, class2_data, test_size=0.30, random_state=42)

# 0 is used to represent class1 and 1 is used to represent class2
# Assign target variables
class1_train_target = np.zeros(class1_train.shape[0])
class2_train_target = np.ones(class2_train.shape[0])
class1_test_target = np.zeros(class1_test.shape[0])
class2_test_target = np.ones(class2_test.shape[0])

# Stack the data
# vstack is used for data and hstack for labels (as it is a row vector initially)
train_data = np.vstack((class1_train, class2_train))
train_labels = np.hstack((class1_train_target, class2_train_target))
test_data = np.vstack((class1_test, class2_test))
test_labels = np.hstack((class1_test_target, class2_test_target))

# Shuffle the data for use in models
train_data, train_labels = shuffle(train_data, train_labels, random_state=42)
test_data, test_labels = shuffle(test_data, test_labels, random_state=42)

# Generate the csv files after manipulating the datastructures
# The generated files will represent the train and the test data
np.savetxt("DS1-train.csv", np.hstack((train_data, np.transpose(np.atleast_2d(train_labels)))) ,delimiter=',')
np.savetxt("DS1-test.csv", np.hstack((test_data, np.transpose(np.atleast_2d(test_labels)))) ,delimiter=',')