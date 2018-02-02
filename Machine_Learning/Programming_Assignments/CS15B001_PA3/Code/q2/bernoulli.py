import pandas as pd
import numpy as np
from scipy import sparse
import os
import functions
import time
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_fscore_support
from tabulate import tabulate
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
data_matrix = functions.load_sparse_csr('data_sparse').todense()
labels_matrix = np.loadtxt('labels.csv', delimiter=',')

# Cross Validation
kf = KFold(n_splits=5)
counter = 0
[avr_prec, avr_rec, avr_fsc] = [.0,.0,.0]
for train_index, test_index in kf.split(data_matrix):
	counter += 1
	data_train, data_test = data_matrix[train_index], data_matrix[test_index]
	labels_train, labels_test = labels_matrix[train_index], labels_matrix[test_index]

	b = BernoulliNB()
	b.fit(data_train, labels_train)
	predicted_labels = b.predict(data_test)

	# # Estimate the class priors
	# spam_prior = float(np.count_nonzero(labels_train == 0))/labels_train.shape[0]
	# ham_prior = float(np.count_nonzero(labels_train == 1))/labels_train.shape[0]

	# # Estimate the conditional probabilities
	# # Get all spam articles and get the column sum
	# # Do the same for all ham articles
	# # Add-1 smoothing is performed here
	# cond_ham = ((np.count_nonzero(data_train[labels_train==1], axis=0)+1).astype(dtype=float))/(data_train[labels_train==1].shape[0]+2)
	# cond_spam = ((np.count_nonzero(data_train[labels_train==0], axis=0)+1).astype(dtype=float))/(data_train[labels_train==0].shape[0]+2)

	# # Using log so that there are no underflow problems
	# predicted_labels = np.ones(shape=labels_test.shape, dtype=float)
	# for i in range(predicted_labels.shape[0]):
	# 	score_ham = np.sum(np.multiply(np.log(cond_ham), data_test[i,:]))+np.log(ham_prior)
	# 	score_spam = np.sum(np.multiply(np.log(cond_spam), data_test[i,:]))+np.log(spam_prior)
	# 	if score_spam > score_ham:
	# 		predicted_labels[i] = 0
	# 	else:
	# 		predicted_labels[i] = 1

	# print("Fold Number "+str(counter))
	[prec,rec,fsc,sup] = precision_recall_fscore_support(labels_test, predicted_labels)
	avr_prec += prec[1]
	avr_rec += rec[1]
	avr_fsc += fsc[1]
	# print tabulate([prec, rec, fsc], headers=['Spam', 'Ham'])
	# print("")

print("")
print("Average Scores for Spam Class")
print("Precision: "+str(avr_prec/5))
print("Recall: "+str(avr_rec/5))
print("FScore: "+str(avr_fsc/5)) 

# Plot the PR Curves
train_data, test_data, train_labels, test_labels = train_test_split(data_matrix, labels_matrix, test_size=0.33, random_state=42)
m = BernoulliNB()
m.fit(train_data, train_labels)
probab = m.predict_proba(test_data)
precision_, recall_, threshold_ = precision_recall_curve(test_labels, probab[:,1])
fig = plt.figure()
fig.suptitle('Precision Recall Curve')
ax = fig.add_subplot(111)
ax.set_xlabel('Precision')
ax.set_ylabel('Recall')
# ax.fill(precision_,np.zeros(shape=precision_.shape),'b')
p = [0]
r = [1]
p.extend(list(precision_))
r.extend(list(recall_))
ax.fill(p, r,'b', zorder=5)
plt.plot(p, r)
plt.show()