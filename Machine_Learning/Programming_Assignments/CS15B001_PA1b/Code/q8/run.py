"""
Code to perform Multi-Class classification using 
Neural Networks

Author: Ameet Deshpande
RollNo: CS15B001
""" 

"""
The last 4 columns of the training and test sets indicate
the class of that data sample.
Columns in order are: mountain, forest, insidecity, coast
"""

import pandas as pd
from sklearn.utils import shuffle
import functions
import numpy as np
from sklearn.preprocessing import scale
from sklearn.metrics import precision_recall_fscore_support
from tabulate import tabulate
import time
import matplotlib.pyplot as plt

# Load the csv files into dataframes
train = pd.read_csv("DS2-train.csv", header=None)
test = pd.read_csv("DS2-test.csv", header=None)

[train_data, train_labels] = [train.iloc[:,0:-4], train.iloc[:,-4:]]
[test_data, test_labels] = [test.iloc[:,0:-4], test.iloc[:,-4:]]

# Shuffle the dataframes
train_data, train_labels = shuffle(train_data, train_labels, random_state=42)
test_data, test_labels = shuffle(test_data, test_labels, random_state=42)

# Normalize the data
train_size = train_data.shape[0]
total_data = pd.concat([train_data, test_data])
total_data = pd.DataFrame(scale(total_data, copy=True))
train_data = total_data.iloc[0:train_size,:]
test_data = total_data.iloc[train_size:, :]

"""
Part-1
Using the Cross-Entropy loss function
"""
num_of_iterations = 1000
num_hidden_layers = 45
learning_rate = 0.01
model1 = functions.nnmodel1(train_data.shape[1],num_hidden_layers,4,np.array(train_data),np.array(train_labels), learning_rate)
model1.train_model(num_of_iterations)
predicted_labels = model1.predict_values(test_data)
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
print("Using Cross Entropy Loss Function")
print("Printing in order Precision, Recall, F-score")
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])
# print(model1.weight_square())


"""
Part-2
Using modified Loss Function
"""
lambdas = [0, 0.01, 0.1, 1, 10, 100]
fscores = []

for lam in lambdas:
	num_of_iterations = 1000
	num_hidden_layers = 45
	regularization = lam
	learning_rate = 0.01
	model2 = functions.nnmodel2(train_data.shape[1],num_hidden_layers,4,np.array(train_data),np.array(train_labels), learning_rate, regularization)
	model2.train_model(num_of_iterations)
	predicted_labels = model2.predict_values(test_data)
	[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
	print("Using Loss Function defined in the problem statement")
	print("Printing in order Precision, Recall, F-score")
	print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])
	# print(model2.weight_square())
	fscores.append((fsc[1]+fsc[2]+fsc[3])/3)

# Plot the values

# plt.plot(lambdas, fscores)
# plt.show()