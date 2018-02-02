from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_data(train_data, test_data, train_labels, test_labels, coeffs): 
	total_data = pd.concat([pd.DataFrame(train_data), pd.DataFrame(test_data)])
	total_labels = np.array(pd.concat([train_labels, test_labels])).flatten()

	class1 = total_data.loc[total_labels==1,:]
	class2 = total_data.loc[total_labels==2,:]

	plt.scatter(class1[:], 1*np.ones(class1.shape[0], dtype=np.float), c='r', marker='o')
	plt.scatter(class2[:], 2*np.ones(class2.shape[0], dtype=np.float), c='b', marker='^')
	
	# Plot the line using coefficients obtained
	x,y = [[],[]]	
	for i in range(-8,9):
		x.append(i)
		y.append(coeffs[0] + coeffs[1]*i)
	plt.plot(x, y, 'g-')
	plt.xlabel('Principal Component')
	plt.ylabel('Indicator Variable')
	plt.show()