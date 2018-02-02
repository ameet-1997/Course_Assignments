import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt 
from sklearn.metrics import accuracy_score

def get_purity(filename):
	f = open(filename, "r")
	lines = f.readlines()
	lines = lines[::-1]
	for line in lines:
		temp = line.strip().split()
		try:
			if temp[0] == "Incorrectly":
				return float(temp[-2])
		except:
			continue

def purity_score_stack(y_true, y_pred):
    y_labeled_voted = np.zeros(y_true.shape)
    labels = np.unique(y_true)
    bins = np.concatenate((labels, [np.max(labels)+1]), axis=0)

    for cluster in np.unique(y_pred):
        hist, _ = np.histogram(y_true[y_pred==cluster], bins=bins)
        winner = np.argmax(hist)
        y_labeled_voted[y_pred==cluster] = winner

    return accuracy_score(y_true, y_labeled_voted)