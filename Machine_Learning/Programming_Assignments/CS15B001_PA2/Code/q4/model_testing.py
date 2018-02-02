"""
File used to test different models
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
from sklearn.metrics import f1_score


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

c_values = [float(i)/10 for i in range(2,50)]
to_plot = []

for c in c_values:
	linear = SVC(kernel='linear', C=c)
	linear.fit(train_data, train_labels)
	predicted_labels = linear.predict(test_data)
	[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
	# print(fsc)
	to_plot.append(float(sum(fsc))/float(4))

plt.plot(c_values, to_plot)
plt.show()






# gamma_values = [float(i)/100 for i in range(1,10)]
# coef0_values = [float(i)/10 for i in range(1,1000)]
degree_values = [i for i in range(2,4)]
to_plot = []

for deg in degree_values:
	poly = SVC(kernel='poly', C=0.2, coef0=2, degree=deg, gamma=0.1)
	poly.fit(train_data, train_labels)
	predicted_labels = poly.predict(test_data)
	[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
	# print(fsc)
	to_plot.append(float(sum(fsc))/float(4))
	print(f1_score(test_labels, predicted_labels, average='macro'))


plt.plot(degree_values, to_plot)
plt.xlabel("Degree")
plt.ylabel("F-Score")
plt.show()





gamma_values = [float(i)/100 for i in range(1,50)]
# coef0_values = [float(i)/10 for i in range(1,1000)]
# degree_values = [i for i in range(2,4)]
# c_values = [float(i)/2 for i in range(1,100)]
to_plot = []

for g in gamma_values:
	poly = SVC(kernel='rbf', C=20, gamma=g)
	poly.fit(train_data, train_labels)
	predicted_labels = poly.predict(test_data)
	[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
	# to_plot.append(float(sum(fsc))/float(4))
	to_plot.append(f1_score(test_labels, predicted_labels, average='macro'))
	# print(f1_score(test_labels, predicted_labels, average='macro'))


plt.plot(gamma_values, to_plot)
plt.xlabel("Gamma")
plt.ylabel("F-Score")
plt.show()





# gamma_values = [float(i)/100 for i in range(1,50)]
# coef0_values = [float(i)/10 for i in range(1,200)]
# degree_values = [i for i in range(2,4)]
c_values = [float(i)/10 for i in range(1,30)]
to_plot = []

for c in c_values:
	sig = SVC(kernel='sigmoid', C=c)
	sig.fit(train_data, train_labels)
	predicted_labels = sig.predict(test_data)
	[prec, rec, fsc, sup] = precision_recall_fscore_support(test_labels, predicted_labels)
	# to_plot.append(float(sum(fsc))/float(4))
	to_plot.append(f1_score(test_labels, predicted_labels, average='macro'))
	# print(f1_score(test_labels, predicted_labels, average='macro'))


plt.plot(c_values, to_plot)
plt.xlabel("C")
plt.ylabel("F-Score")
plt.show()