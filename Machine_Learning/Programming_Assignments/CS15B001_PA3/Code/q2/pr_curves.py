import pandas as pd
import numpy as np
from scipy import sparse
import os
import functions
import time
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support
from tabulate import tabulate
import matplotlib.pyplot as plt

# Load the data
data_matrix = functions.load_sparse_csr('data_sparse').todense()
labels_matrix = np.loadtxt('labels.csv', delimiter=',')

beta=0
prec_graph = []
rec_graph = []
for alpha in [0,10,100,1000,10000,100000,1000000, 10000000000]:
	kf = KFold(n_splits=5)
	counter = 0
	[avr_prec, avr_rec, avr_fsc] = [.0,.0,.0]
	for train_index, test_index in kf.split(data_matrix):
		counter += 1
		data_train, data_test = data_matrix[train_index], data_matrix[test_index]
		labels_train, labels_test = labels_matrix[train_index], labels_matrix[test_index]
		spam_prior = float(np.count_nonzero(labels_train == 0)+alpha-1)/(labels_train.shape[0]+alpha+beta-2)
		ham_prior = float(np.count_nonzero(labels_train == 1)+beta-1)/(labels_train.shape[0]+alpha+beta-2)
		shp = data_train.shape[1]
		cond_spam = (np.sum(data_train[labels_train == 0], axis=0)+np.ones(shape=shp))/(np.sum(data_train[labels_train == 0])+data_train.shape[1])
		cond_ham = (np.sum(data_train[labels_train == 1], axis=0)+np.ones(shape=shp))/(np.sum(data_train[labels_train == 1])+data_train.shape[1])

		# Using log so that there are no underflow problems
		predicted_labels = np.ones(shape=labels_test.shape, dtype=float)
		for i in range(predicted_labels.shape[0]):
			score_ham = np.sum(np.multiply(np.log(cond_ham), data_test[i,:]))+np.log(ham_prior)
			score_spam = np.sum(np.multiply(np.log(cond_spam), data_test[i,:]))+np.log(spam_prior)
			if score_spam > score_ham:
				predicted_labels[i] = 0
			else:
				predicted_labels[i] = 1
		[prec,rec,fsc,sup] = precision_recall_fscore_support(labels_test, predicted_labels)
		avr_prec += prec[0]
		avr_rec += rec[0]
		avr_fsc += fsc[0]

	prec_graph.append(float(avr_prec)/5)
	rec_graph.append(float(avr_rec)/5)

plt.plot(rec_graph, prec_graph)
plt.show()