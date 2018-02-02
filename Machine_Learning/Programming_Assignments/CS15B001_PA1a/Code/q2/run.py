"""
This file has been used to complete assignment parts 1,2,3 of PA1
Includes generation of synthetic data, learning Linear and KNN classifiers
and getting the accuracy values

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the data generated in question 1 after changing the working directory
os.chdir("..")
train = pd.read_csv("q1/DS1-train.csv", header=None)
test = pd.read_csv("q1/DS1-test.csv", header=None)

# Change back the working directory
os.chdir(os.getcwd()+"/q2")

# Subset the data and the labels
train_data = train.iloc[:,0:20]
train_labels = np.array(train.iloc[:,20])

test_data = test.iloc[:,0:20]
test_labels = np.array(test.iloc[:,20])

# Train Linear Regression Model on the data
lr = LinearRegression()
lr.fit(train_data, train_labels)

# Predict the values for testdata
predicted_labels_linear = lr.predict(test_data)

# Using threshold as 0.5 to check which class it belongs to
predicted_labels_linear[predicted_labels_linear >= 0.5] = 1
predicted_labels_linear[predicted_labels_linear < 0.5] = 0

# Calculate the scores for the predicted labels
lin_accuracy = accuracy_score(test_labels, predicted_labels_linear)
lin_precision = precision_score(test_labels, predicted_labels_linear)	# average='macro'
lin_recall = recall_score(test_labels, predicted_labels_linear)
lin_f = f1_score(test_labels, predicted_labels_linear)

print("Accuracy: "+str(lin_accuracy))
print("Precision: "+str(lin_precision))
print("Recall: "+str(lin_recall))
print("F-Score: "+str(lin_f))
print("Coefficients Learnt: "+str(lr.coef_))

np.savetxt("coeffs.csv", lr.coef_,delimiter=',')