"""
Python Code to load Iris Dataset and perform
different Feature Extraction Techniques
One class is linearly separable from the other 2; 
the latter are NOT linearly separable from each other. 

Author: Ameet Deshpande
RollNo: CS15B001
"""

import pandas as pd
from pandas import read_csv
from sklearn.preprocessing import scale
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tabulate import tabulate
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt
from functions import get_classes, plot_lda, plot_qda, plot_rda
from sklearn.model_selection import cross_val_score
from rda import RegularizedDiscriminantAnalysis

# Load the data and get the attributes and labels
data = read_csv("iris.csv", header=None)
labels = data.iloc[:,4]
labels[labels == "Iris-setosa"] = 0
labels[labels == "Iris-versicolor"] = 1
labels[labels == "Iris-virginica"] = 2
labels = pd.to_numeric(labels)
[class1, class2, class3] = get_classes()

# Only petal width and petal length are used as features
# Normalize the data
data = data.iloc[:,2:4]
data = scale(data)

# Train-Test Split on the data
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.33, random_state=20, shuffle=True)




# Perform LDA on the data
LDA = LinearDiscriminantAnalysis(solver='svd', n_components=None)
LDA.fit(train_data, train_labels)

# Plot the classifier boundaries for LDA
plot_lda(LDA, class1, class2, class3)

# Predict the values in the test data and check metrics
lda_predicted = LDA.predict(test_data)

# Calculate the evaluations metrics
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, lda_predicted)
print("LDA")
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3'])
# print("Cross Validated Score: "+str(cross_val_score(LDA, data, labels, cv=3, scoring='f1_macro')))




# Perform QDA on the data
QDA = QuadraticDiscriminantAnalysis() 	# Default values are suitable
QDA.fit(train_data, train_labels)

# Plot the classifier boundaries for QDA
plot_qda(QDA, class1, class2, class3)

# Predict the values in the test data and check metrics
qda_predicted = QDA.predict(test_data)

# Calculate the evaluations metrics
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, qda_predicted)
print("QDA")
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3'])
# print("Cross Validated Score: "+str(cross_val_score(QDA, data, labels, cv=3, scoring='f1_macro')))



# Perform RDA on the data

alpha = [float(i)/10 for i in range(7)]
gamma = [float(i)/10 for i in range(11)]
best_alpha = 0
best_gamma = 0
best_score = 0

for a in alpha:
	for g in gamma:
		RDA = RegularizedDiscriminantAnalysis(alpha=a, gamma=g)
		RDA.fit(train_data, train_labels)
		rda_predicted = RDA.predict(test_data)
		[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, rda_predicted)
		if sum(fsc) > best_score:
			best_alpha = a
			best_gamma = g

# Use the best model to train the data
RDA = RegularizedDiscriminantAnalysis(alpha=best_alpha, gamma=best_gamma)
RDA.fit(train_data, train_labels)

# Predict the labels
rda_predicted = RDA.predict(test_data)
[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, rda_predicted)
print("RDA")
print tabulate([prec, rec, fsc], headers=['Class1', 'Class2', 'Class3'])

# Plot the classifier boundaries for RDA
plot_qda(RDA, class1, class2, class3)