from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
import pandas as pd

# Note that the three images represent the 3 permutations of the dimensions
# This thus gives all the views of the data (top left front)

def generate_3d():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	# Load the data and labels
	train_data = read_csv("../../Dataset/DS3/train.csv", header=None)
	train_labels = read_csv("../../Dataset/DS3/train_labels.csv", header=None)
	test_data = read_csv("../../Dataset/DS3/test.csv", header=None)
	test_labels = read_csv("../../Dataset/DS3/test_labels.csv", header=None)

	# Load all the data together
	total_data = pd.concat([train_data, test_data])
	total_labels = np.array(pd.concat([train_labels, test_labels])).flatten()

	class1 = total_data.loc[total_labels==1,:]
	class2 = total_data.loc[total_labels==2,:]

	i=2
	ax.scatter(class1.iloc[:,i], class1.iloc[:,(i+1)%3], class1.iloc[:,(i+2)%3], c='r', marker='o')
	ax.scatter(class2.iloc[:,i], class2.iloc[:,(i+1)%3], class2.iloc[:,(i+2)%3], c='b', marker='^')

	ax.set_xlabel('Dimension 1')
	ax.set_ylabel('Dimension 2')
	ax.set_zlabel('Dimension 3')

	plt.show()