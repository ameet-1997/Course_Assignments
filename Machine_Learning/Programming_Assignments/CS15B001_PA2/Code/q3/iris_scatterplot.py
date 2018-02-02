"""
Python script used to plot the datasets using
the petal width and length as features.

Author: Ameet Deshpande
RollNo: CS15B001
"""

import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data and get the attributes and labels
data = read_csv("iris.csv", header=None)
labels = data.iloc[:,4]
labels[labels == "Iris-setosa"] = 0
labels[labels == "Iris-versicolor"] = 1
labels[labels == "Iris-virginica"] = 2
labels = pd.to_numeric(labels)

# Only petal width and petal length are used as features
# Normalize the data
data = data.iloc[:,2:4]
data = scale(data)

# Train-Test Split on the data
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.33, random_state=42) 

# Plot only the training data
boolean_array = np.array(train_labels == 0)
class1 = train_data[boolean_array]
boolean_array = np.array(train_labels == 1)
class2 = train_data[boolean_array]
boolean_array = np.array(train_labels == 2)
class3 = train_data[boolean_array]

fig = plt.figure()
sub = fig.add_subplot(111)
c1 = sub.scatter(class1[:,0], class1[:,1], s=50, c='red')
c2 = sub.scatter(class2[:,0], class2[:,1], s=50, c='blue')
c3 = sub.scatter(class3[:,0], class3[:,1], s=50, c='green')

sub.set_xlabel('Petal length (cm)')
sub.set_ylabel('Petal width (cm)')
plt.show()