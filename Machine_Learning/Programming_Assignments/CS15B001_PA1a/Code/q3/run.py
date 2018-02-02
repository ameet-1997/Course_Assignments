"""
This file has been used to complete assignment parts 3 of PA1
Includes KNN classification
and getting the accuracy values

Author: Ameet Deshpande
RollNo: CS15B001
"""

# Best fit is achieved with 82 neighbours

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
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

max_knn_accuracy = 0
neighbor_value = 0
knn_values = []

# Note that the maximum is taken only based on accuracy
for i in range(100):
	kn = KNeighborsClassifier(n_neighbors=i+1)
	kn.fit(train_data, train_labels)
	predicted_labels_knn = kn.predict(test_data)
	acc = accuracy_score(test_labels, predicted_labels_knn)
	if max_knn_accuracy < acc:
		neighbor_value = i+1
		max_knn_accuracy = acc
	print(str(i+1)+" neighbors considered with accuracy of "+str(acc))
	knn_values.append(acc)

# Learn a KNN classifier for the best fit
kn = KNeighborsClassifier(n_neighbors=neighbor_value)
kn.fit(train_data, train_labels)

# Predict the values for testdata using the best fit model
predicted_labels_knn = kn.predict(test_data)

# Calculate the scores for the predicted labels
knn_accuracy = accuracy_score(test_labels, predicted_labels_knn)
knn_precision = precision_score(test_labels, predicted_labels_knn)	# average='macro'
knn_recall = recall_score(test_labels, predicted_labels_knn)
knn_f = f1_score(test_labels, predicted_labels_knn)

print("Max Accuracy: "+str(knn_accuracy))
print("Max Precision: "+str(knn_precision))
print("Max Recall: "+str(knn_recall))
print("Max F-Score: "+str(knn_f))

# Store the accuracy values in a csv file
# np.savetxt("accuracies.csv", np.array(knn_values),delimiter=',')