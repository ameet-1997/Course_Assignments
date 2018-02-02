import pandas as pd
import numpy as np
from scipy import sparse
import os
import functions
import time
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import precision_recall_fscore_support, precision_recall_curve
from tabulate import tabulate
import matplotlib.pyplot as plt

# Load the data
data_matrix = functions.load_sparse_csr('data_sparse').todense()
labels_matrix = np.loadtxt('labels.csv', delimiter=',')

# Cross Validation
kf = KFold(n_splits=5)
counter = 0
[avr_prec, avr_rec, avr_fsc] = [.0,.0,.0]

# Getting the most frequent words in each class
spam_words = set()
ham_words = set()

score_for_pr_curve = []
test_labels = []

for train_index, test_index in kf.split(data_matrix):
	counter += 1
	data_train, data_test = data_matrix[train_index], data_matrix[test_index]
	labels_train, labels_test = labels_matrix[train_index], labels_matrix[test_index]

	if counter == 1:
		test_labels = list(labels_test)

	# Estimate the class priors, Dirichlet does not influence this
	spam_prior = float(np.count_nonzero(labels_train == 0))/labels_train.shape[0]
	ham_prior = float(np.count_nonzero(labels_train == 1))/labels_train.shape[0]

	# Estimate the conditional probabilities
	# Get all spam articles and get the column sum
	# Do the same for all ham articles
	# Instead of Add-1 smoothing, use Dirichlet Distribution
	shp = data_train.shape[1]
	alpha0 = functions.get_alpha0_dirichlet(shp)
	alpha1 = functions.get_alpha1_dirichlet(shp)
	alpha0_sum = np.sum(alpha0) - shp 	# sum alpha_i - K
	alpha1_sum = np.sum(alpha1) - shp

	cond_spam = (np.sum(data_train[labels_train == 0], axis=0)+alpha0-1)/(np.sum(data_train[labels_train == 0])+alpha0_sum)
	cond_ham = (np.sum(data_train[labels_train == 1], axis=0)+alpha1-1)/(np.sum(data_train[labels_train == 1])+alpha1_sum)

	# print(type(np.argsort(-cond_spam)[0:10:1]))
	# temp = np.array(np.argsort(-cond_spam)[:,:10])[0]
	# print(temp)
	number_of_words_to_take = 20
	spam_words.update(list(np.array(np.argsort(-cond_spam)[:,:number_of_words_to_take])[0]))
	ham_words.update(list(np.array(np.argsort(-cond_ham)[:,:number_of_words_to_take])[0]))
	# ham_words.update(list(np.argsort(-cond_ham)[0][:,:10]))

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
	avr_prec += prec[0]
	avr_rec += rec[0]
	avr_fsc += fsc[0]
	# print tabulate([prec, rec, fsc], headers=['Spam', 'Ham'])

	# for number in spam_words:
	# 	print(str(cond_spam[0,number])+"::"+str(cond_ham[0,number]))
	# print("One Fold done")

print("Average Scores for Spam Class")
print("Precision: "+str(avr_prec/5))
print("Recall: "+str(avr_rec/5))
print("FScore: "+str(avr_fsc/5))

# print "Spam Words: ",
# print(sorted(list(spam_words.difference(ham_words))))
# print "Ham Words: ",
# print(sorted(list(ham_words.difference(spam_words))))

# print "Spam Words: ",
# print(sorted(list(spam_words)))
# print "Ham Words: ",
# print(sorted(list(ham_words)))

# for number in spam_words.difference(ham_words):
# 	print(str(cond_spam[0,number])+"&"+str(cond_ham[0,number]))

# Plot the PR Curves
# train_data, test_data, train_labels, test_labels = train_test_split(data_matrix, labels_matrix, test_size=0.33, random_state=42)
# m = MultinomialNB()
# m.fit(train_data, train_labels)
# probab = m.predict_proba(test_data)

score_for_pr_curve = np.array(score_for_pr_curve)/1000
# print(score_for_pr_curve)
precision_, recall_, threshold_ = precision_recall_curve(test_labels, score_for_pr_curve)
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