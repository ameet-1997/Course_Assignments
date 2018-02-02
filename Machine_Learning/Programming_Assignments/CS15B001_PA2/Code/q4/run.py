"""
Code to learn SVM with different kernels
Cross Validation to tune hyperparameters of the model
Dataset is the same one used for Question 8 (PA1)
The last 4 columns contain One-Hot Encoding of the 4 classes

Note that since there is an explicit Test data, we do 
not have to use Nested Cross Validation. We instead
use only one round of validation to tune parameters and
then test on the test data

1000 training examples. Thus, 5 fold cross validation, as
more than 5 will cross validate on a very small held
out set

Author: Ameet Deshpande
RollNo: CS15B001
"""

import pandas as pd
from sklearn.utils import shuffle
import numpy as np
from sklearn.preprocessing import scale
from sklearn.metrics import precision_recall_fscore_support
from tabulate import tabulate
import time
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import cPickle

# Load the csv files into dataframes
train = pd.read_csv("DS2-train.csv", header=None)
test = pd.read_csv("DS2-test.csv", header=None)

[train_data, train_labels] = [train.iloc[:,0:-1], train.iloc[:,-1:]]
[test_data, test_labels] = [test.iloc[:,0:-1], test.iloc[:,-1:]]
train_labels = np.array(train_labels).flatten()
test_labels = np.array(test_labels).flatten()

# Shuffle the dataframes
train_data, train_labels = shuffle(train_data, train_labels, random_state=42)
test_data, test_labels = shuffle(test_data, test_labels, random_state=42)

# Normalize the data
train_size = train_data.shape[0]
total_data = pd.concat([train_data, test_data])
total_data = pd.DataFrame(scale(total_data, copy=True))
train_data = total_data.iloc[0:train_size,:]
test_data = total_data.iloc[train_size:, :]

# SVM gives both One vs Rest and One vs One classifiers
# One vs Rest will be used as the complexity is much lesser





# Linear Kernel
linear = SVC(kernel='linear')

# Using GridSearchCV to get best fit parameters
clf = GridSearchCV(linear, param_grid={'C':[float(i)/10 for i in range(2,10)]}, cv=5, scoring='f1_macro')
clf.fit(train_data, train_labels)
print(clf.best_params_)

# Predict the labels
linear_predicted = clf.predict(test_data)

# Store the model
with open('svm_model1.model', 'wb') as f:
    cPickle.dump(clf, f)

# Print the score
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, linear_predicted)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])





# Polynomial Kernel
poly = SVC(kernel='poly')
c_values = [float(i)/10 for i in range(2,10)]
coef0_values = [float(i)/2 for i in range(4,13)]

# Using GridSearchCV to get best fit parameters
clf = GridSearchCV(poly, param_grid={'degree':range(1,8), 'C':c_values, 'gamma':[0.1, 0.3, 0.6, 0.9], 'coef0':coef0_values}, scoring='f1_macro', cv=5)
clf.fit(train_data, train_labels)
print(clf.best_params_)

# Predict the labels
poly_predicted = clf.predict(test_data)

# Store the model
with open('svm_model2.model', 'wb') as f:
    cPickle.dump(clf, f)

[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, poly_predicted)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])




# Gaussian Kernel
gaus = SVC(kernel='rbf')
c_values = [float(i)/2 for i in range(40,80)]
gamma_values = [float(i)/100 for i in range(1,10)]

# Using GridSearchCV to get best fit parameters
clf = GridSearchCV(gaus, param_grid={'C':c_values, 'gamma':gamma_values}, scoring='f1_macro', cv=5)
clf.fit(train_data, train_labels)
print(clf.best_params_)

# Store the model
with open('svm_model3.model', 'wb') as f:
    cPickle.dump(clf, f)

# Predict the labels
gaus_predicted = clf.predict(test_data)

[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, gaus_predicted)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])




# Sigmoid Kernel
sig = SVC(kernel='sigmoid')
c_values = [float(i)/10 for i in range(1,10)]
gamma_values = [float(i)/100 for i in range(1,3)]
coef0_values = [float(i)/10 for i in range(0,10)]

# Using GridSearchCV to get best fit parameters
clf = GridSearchCV(sig, param_grid={'C':c_values, 'gamma':gamma_values, 'coef0':coef0_values}, scoring='f1_macro')
clf.fit(train_data, train_labels)
print(clf.best_params_)

# Store the model
with open('svm_model4.model', 'wb') as f:
    cPickle.dump(clf, f)

sig_predicted = clf.predict(test_data)
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, sig_predicted)
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3', 'Class4'])


"""Command to load the model
with open('svm_model1.model', 'rb') as f:
    clf = cPickle.load(f)
"""