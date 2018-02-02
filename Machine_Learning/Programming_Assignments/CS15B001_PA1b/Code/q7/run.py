"""
Code to run logistic regression on the dataset generated

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from sklearn.metrics import precision_recall_fscore_support
from sklearn.preprocessing import scale
from tabulate import tabulate
import matplotlib.pyplot as plt

# Read from the csv files
train = pd.read_csv("DS2-train.csv", header=None)
test = pd.read_csv("DS2-test.csv", header=None)

# Split the dataframe into labels and features and shuffle the data
[train_data, train_labels] = [train.iloc[:,0:-1], train.iloc[:,-1]]
train_data, train_labels = shuffle(train_data, train_labels, random_state=42)

[test_data, test_labels] = [train.iloc[:,0:-1], train.iloc[:,-1]]
test_data, test_labels = shuffle(test_data, test_labels, random_state=42)

# Normalize the data
train_size = train_data.shape[0]
total_data = pd.concat([train_data, test_data])
total_data = pd.DataFrame(scale(total_data, copy=True))
train_data = total_data.iloc[0:train_size,:]
test_data = total_data.iloc[train_size:, :]

# Set a very small Regularization parameter
classifier = LogisticRegression(C=1e42, max_iter=100)

# Train the model
classifier.fit(train_data, train_labels)
predicted_labels = classifier.predict(test_data)

# Store and print the accuracy scores
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
print("Logistic Regression without regularization")
print("Printing in order::Precision, Recall, FScore")
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2'])
print("")

# Using Professor Boyd's code for L1 regularization
# Running the commands in quiet mode, flag -q
# Run using different Lambdas and plot a graph
os.system("./l1_logreg-0.8.2-i686-pc-linux-gnu/l1_logreg_train -q -s Train_features Train_labels 0.01 model")
os.system("./l1_logreg-0.8.2-i686-pc-linux-gnu/l1_logreg_classify -q model Test_features result")

# The results are now stored in a file called result and answers are stored in Test_features

# Get the labels from the file
boyd_test_labels = []
boyd_predicted_labels = []

f = open('Test_labels','r')
tests = f.readlines()
for dt in tests:
	temp = dt.strip(" ").split()
	# If there is only one element and it is not %, then it is a label
	if len(temp) == 1 and temp[0] <> "%":
		boyd_test_labels.append(int(temp[0]))


f = open('result','r')
tests = f.readlines()
for dt in tests:
	temp = dt.strip(" ").split()
	# If there is only one element and it is not %, then it is a label
	if len(temp) == 1 and temp[0] <> "%":
		boyd_predicted_labels.append(int(temp[0]))

# Store and print the accuracy scores
[prec1, rec1, fsc1, sup1] = precision_recall_fscore_support(boyd_test_labels, boyd_predicted_labels)
print("Logistic Regression with L1 regularization")
print("Printing in order::Precision, Recall, FScore")
print tabulate([prec1, rec1, fsc1], headers=['Class1', 'Class2'])


# The code below was used to find the optimal regularization parameter

# lambdas = [i/1000.0 for i in range(1,100,2)]
# precisions = []
# final_answer = 0
# [max_prec, max_rec, max_fsc, max_sup] = [prec1, rec1, fsc1, sup1]
# print("Initial max value is: "+str(max_prec[0]))
# for lam in lambdas:
# 	os.system("./l1_logreg-0.8.2-i686-pc-linux-gnu/l1_logreg_train -q -s Train_features Train_labels "+str(lam)+" model")
# 	os.system("./l1_logreg-0.8.2-i686-pc-linux-gnu/l1_logreg_classify -q model Test_features result")

# 	# The results are now stored in a file called result and answers are stored in Test_features

# 	# Get the labels from the file
# 	boyd_test_labels = []
# 	boyd_predicted_labels = []

# 	f = open('Test_labels','r')
# 	tests = f.readlines()
# 	for dt in tests:
# 		temp = dt.strip(" ").split()
# 		# If there is only one element and it is not %, then it is a label
# 		if len(temp) == 1 and temp[0] <> "%":
# 			boyd_test_labels.append(int(temp[0]))


# 	f = open('result','r')
# 	tests = f.readlines()
# 	for dt in tests:
# 		temp = dt.strip(" ").split()
# 		# If there is only one element and it is not %, then it is a label
# 		if len(temp) == 1 and temp[0] <> "%":
# 			boyd_predicted_labels.append(int(temp[0]))
# 	[t1,t2,t3,t4] = precision_recall_fscore_support(boyd_test_labels, boyd_predicted_labels)
# 	if t1[0] + t1[1] >= max_prec[0] + max_prec[1]:
# 		[max_prec, max_rec, max_fsc, max_sup] = [t1, t2, t3, t4]
# 		final_answer = lam
# 	precisions.append((t1[0]+t1[1])/2)

# print("Logistic Regression with L1 regularization - Best Value of lambda")
# print("Printing in order::Precision, Recall, FScore")
# print tabulate([max_prec, max_rec, max_fsc], headers=['Class1', 'Class2'])
# print("Optimal Value of lambda is: "+str(final_answer))

# plt.plot(lambdas, precisions)
# plt.show()
