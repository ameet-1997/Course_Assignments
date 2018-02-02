import pandas as pd
import numpy as np
from scipy import sparse
import os
import functions
import time
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve
from tabulate import tabulate
import matplotlib.pyplot as plt

# Load the data
data_matrix = functions.load_sparse_csr('data_sparse').todense()
labels_matrix = np.loadtxt('labels.csv', delimiter=',')

score_for_pr_curve = []
test_labels = []

# Cross Validation
kf = KFold(n_splits=5)
counter = 0
[avr_prec, avr_rec, avr_fsc] = [.0,.0,.0]
for train_index, test_index in kf.split(data_matrix):
	counter += 1
	data_train, data_test = data_matrix[train_index], data_matrix[test_index]
	labels_train, labels_test = labels_matrix[train_index], labels_matrix[test_index]

	if counter == 1:
		test_labels = list(labels_test)

	# Estimate the class priors
	# Use the beta function to get the class priors
	[alpha, beta] = functions.get_alpha_beta()
	spam_prior = float(np.count_nonzero(labels_train == 0)+alpha-1)/(labels_train.shape[0]+alpha+beta-2)
	ham_prior = float(np.count_nonzero(labels_train == 1)+beta-1)/(labels_train.shape[0]+alpha+beta-2)

	# Estimate the conditional probabilities
	# Get all spam articles and get the column sum
	# Do the same for all ham articles
	# Add-1 smoothing is performed here
	shp = data_train.shape[1]
	cond_spam = (np.sum(data_train[labels_train == 0], axis=0)+np.ones(shape=shp))/(np.sum(data_train[labels_train == 0])+data_train.shape[1])
	cond_ham = (np.sum(data_train[labels_train == 1], axis=0)+np.ones(shape=shp))/(np.sum(data_train[labels_train == 1])+data_train.shape[1])

	# Using log so that there are no underflow problems
	predicted_labels = np.ones(shape=labels_test.shape, dtype=float)
	for i in range(predicted_labels.shape[0]):
		score_ham = np.sum(np.multiply(np.log(cond_ham), data_test[i,:]))+np.log(ham_prior)
		score_spam = np.sum(np.multiply(np.log(cond_spam), data_test[i,:]))+np.log(spam_prior)
		if counter == 1:
			score_for_pr_curve.append(score_spam/(score_spam+score_ham))
		if score_spam > score_ham:
			predicted_labels[i] = 0
		else:
			predicted_labels[i] = 1

	# print("Fold Number "+str(counter))
	[prec,rec,fsc,sup] = precision_recall_fscore_support(labels_test, predicted_labels)
	class_ = 0
	avr_prec += prec[class_]
	avr_rec += rec[class_]
	avr_fsc += fsc[class_]
	# print tabulate([prec, rec, fsc], headers=['Spam', 'Ham'])

print("Average Scores for Spam Class")
print("Precision: "+str(avr_prec/5))
print("Recall: "+str(avr_rec/5))
print("FScore: "+str(avr_fsc/5)) 

score_for_pr_curve = np.array(score_for_pr_curve)/1000
# print(score_for_pr_curve)
precision_, recall_, threshold_ = precision_recall_curve(test_labels, score_for_pr_curve)
fig = plt.figure()
fig.suptitle('Precision Recall Curve')
ax = fig.add_subplot(111)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
ax.fill(precision_,np.zeros(shape=precision_.shape),'b')
p = [0]
r = [1]
p.extend(list(precision_))
r.extend(list(recall_))
ax.fill(p, r,'b', zorder=5)
plt.plot(p, r)
plt.show()