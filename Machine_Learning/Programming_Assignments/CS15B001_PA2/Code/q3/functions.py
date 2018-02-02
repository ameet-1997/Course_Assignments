"""
Auxillary functions to be used for Q3

Author: Ameet Deshpande
RollNo: CS15B001
"""

import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import colors


def get_classes():
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

	return [class1, class2, class3]


def plot_lda(lda, class1, class2, class3):
	# Plot the classifier boundaries along with data
	fig1 = plt.figure()
	sub = fig1.add_subplot(111)
	c1 = sub.scatter(class1[:,0], class1[:,1], s=50, c='red')
	c2 = sub.scatter(class2[:,0], class2[:,1], s=50, c='blue')
	c3 = sub.scatter(class3[:,0], class3[:,1], s=50, c='green')
	sub.hold(True)
	# sub.ylim(-2, 2)
	sub.set_xlim(-3,3)
	sub.set_ylim(-2,2)
	# sub.set_autoscale_on(False)

	# Plot the line using coefficients obtained
	x,y = [  [[],[],[]], [[],[],[]]  ] 	# For the three classes
	colors = ['r', 'b', 'g']

	for j in range(3):	
		for l in range(-30000,30000):
			i = float(l)/10000
			if abs(float(-lda.coef_[j][0]*float(i)-lda.intercept_[j])/lda.coef_[j][1]) < 2:
				x[j].append(float(i))
				y[j].append(float(-lda.coef_[j][0]*float(i)-lda.intercept_[j])/lda.coef_[j][1])
		sub.plot(x[j], y[j], colors[j]+'-')

	sub.set_xlabel('Petal length (cm)')
	sub.set_ylabel('Petal width (cm)')
	plt.show()


def plot_qda(qda, class1, class2, class3):
	# Plot the classifier boundaries along with data
	fig1 = plt.figure()
	sub = fig1.add_subplot(111)
	c1 = sub.scatter(class1[:,0], class1[:,1], s=50, c='red')
	c2 = sub.scatter(class2[:,0], class2[:,1], s=50, c='blue')
	c3 = sub.scatter(class3[:,0], class3[:,1], s=50, c='green')
	sub.hold(True)
	sub.set_xlim(-3,3)
	sub.set_ylim(-2,2)

	# Create a mesh of points in the grid
	x_mesh, y_mesh = [np.arange(-3,3,0.1), np.arange(-2,2,0.1)]
	x_mesh, y_mesh = np.meshgrid(x_mesh, y_mesh, sparse=False, indexing='xy')

	# Predict the probabilities on mesh of points
	predicted = qda.predict_proba(np.c_[x_mesh.ravel(), y_mesh.ravel()])

	# Get the points that were classified in respective classes
	class_cond_0 = np.logical_and(predicted[:,0] > predicted[:,1], predicted[:,0] > predicted[:,2]).reshape(x_mesh.shape)
	class_cond_1 = np.logical_and(predicted[:,1] >= predicted[:,0], predicted[:,1] > predicted[:,2]).reshape(x_mesh.shape)
	class_cond_2 = np.logical_and(predicted[:,2] >= predicted[:,0], predicted[:,2] >= predicted[:,1]).reshape(x_mesh.shape)

	# Plot the contours
	sub.contourf(x_mesh, y_mesh, class_cond_0, alpha=0.5)
	sub.contourf(x_mesh, y_mesh, class_cond_1, alpha=0.1)
	sub.contourf(x_mesh, y_mesh, class_cond_2, alpha=0.1)
	plt.show()


def plot_rda(rda, class1, class2, class3):
	# Plot the classifier boundaries along with data
	fig1 = plt.figure()
	sub = fig1.add_subplot(111)
	c1 = sub.scatter(class1[:,0], class1[:,1], s=50, c='red')
	c2 = sub.scatter(class2[:,0], class2[:,1], s=50, c='blue')
	c3 = sub.scatter(class3[:,0], class3[:,1], s=50, c='green')
	sub.hold(True)
	sub.set_xlim(-3,3)
	sub.set_ylim(-2,2)

	# Create a mesh of points in the grid
	x_mesh, y_mesh = [np.arange(-3,3,0.1), np.arange(-2,2,0.1)]
	x_mesh, y_mesh = np.meshgrid(x_mesh, y_mesh, sparse=False, indexing='xy')

	# Predict the probabilities on mesh of points
	predicted = rda.predict_proba(np.c_[x_mesh.ravel(), y_mesh.ravel()])

	# Get the points that were classified in respective classes
	class_cond_0 = np.logical_and(predicted[:,0] > predicted[:,1], predicted[:,0] > predicted[:,2]).reshape(x_mesh.shape)
	class_cond_1 = np.logical_and(predicted[:,1] >= predicted[:,0], predicted[:,1] > predicted[:,2]).reshape(x_mesh.shape)
	class_cond_2 = np.logical_and(predicted[:,2] >= predicted[:,0], predicted[:,2] >= predicted[:,1]).reshape(x_mesh.shape)

	# Plot the contours
	sub.contourf(x_mesh, y_mesh, class_cond_0, alpha=0.5)
	sub.contourf(x_mesh, y_mesh, class_cond_1, alpha=0.1)
	sub.contourf(x_mesh, y_mesh, class_cond_2, alpha=0.1)
	plt.show()