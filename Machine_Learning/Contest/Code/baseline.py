import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import Imputer
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
import time
from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load and impute the data using the mean
train_data = pd.read_csv("train.csv")

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,1:-1]

# Impute it
i = Imputer(strategy='median')
train_data = i.fit_transform(train_data)
test_data = pd.read_csv("test.csv")
test_data = test_data.iloc[:,1:]
test_data = i.transform(test_data)

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=0.4)

sc = StandardScaler()
sc.fit(train_data)
[train_data, validation_data, test_data] = [sc.transform(train_data), sc.transform(validation_data), sc.transform(test_data)]

f_scores = []

# # for comp in [i*100 for i in range(1,11)]:
# # Perform some dimensionality reduction
# # Make sure you scale the data after performing principal component analysis
# pca = PCA(n_components=200)
# pca.fit(train_data, train_labels)
# train_data1 = pca.transform(train_data)
# validation_data1 = pca.transform(validation_data)
# test_data = pca.transform(test_data)

start_time = time.time()

# Train a logistic classifier
log = LogisticRegression(C=0.5)
log.fit(train_data1, train_labels)
predicted_labels = log.predict(validation_data1)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
f_scores.append(f1_score(validation_labels, predicted_labels, average='macro'))
predicted_labels = log.predict(train_data1)
print("Train Score: "+str(f1_score(train_labels, predicted_labels, average='macro')))

print("Total time: "+str(time.time()-start_time))

test_labels = pd.DataFrame(log.predict(test_data))
test_labels.to_csv("submission_logistic2.csv", index_label=['id','label'])

# plt.xlabel("Number of components")
# plt.ylabel("F-Score")
# plt.plot([i*100 for i in range(1,11)], f_scores)
# plt.show()


# start_time = time.time()

# # Train a Random Forest classifier
# rfc = RandomForestClassifier(n_estimators=50, min_samples_leaf=5, max_features='log2')
# rfc.fit(train_data, train_labels)
# predicted_labels = rfc.predict(validation_data)
# print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
# f_scores.append(f1_score(validation_labels, predicted_labels, average='macro'))
# predicted_labels = rfc.predict(train_data)
# print("Train Score: "+str(f1_score(train_labels, predicted_labels, average='macro')))

# print("Total time: "+str(time.time()-start_time))

# test_labels = pd.DataFrame(rfc.predict(test_data))
# test_labels.to_csv("submission_logistic2.csv", index_label=['id','label'])


# # Gradient Boosted Trees
# start_time = time.time()
# clf = GradientBoostingClassifier(n_estimators=100)
# clf.fit(train_data, train_labels)
# predicted_labels = clf.predict(validation_data)
# print(f1_score(validation_labels, predicted_labels, average='macro'))
# print("Total time: "+str(time.time()-start_time))


# # Fit a support vector machine
# clf = SVC()
# clf.fit(train_data, train_labels)
# predicted_labels = clf.predict(validation_data)
# print(f1_score(validation_labels, predicted_labels, average='macro'))