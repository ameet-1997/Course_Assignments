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
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

# Load and impute the data using the mean
train_data = pd.read_csv("train.csv")

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,1:-1]

# Impute it
i = Imputer()
train_data = i.fit_transform(train_data)
test_data = pd.read_csv("test.csv")
test_data = test_data.iloc[:,1:]
test_data = i.transform(test_data)

# train_data, train_labels = shuffle(train_data, train_labels, random_state=20)

# Get validation data 8000:1000
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, random_state=42, shuffle=True)

# # Perform some dimensionality reduction
# # Make sure you scale the data after performing principal component analysis
# pca = PCA(n_components=1000)
# pca.fit(train_data, train_labels)
# train_data = pca.transform(train_data)
# validation_data = pca.transform(validation_data)
# test_data = pca.transform(test_data)
# sc = StandardScaler()
# sc.fit(train_data)
# [train_data, validation_data, test_data] = [sc.transform(train_data), sc.transform(validation_data), sc.transform(test_data)]

# Train a logistic classifier
log = LogisticRegression(C=5)
log.fit(train_data, train_labels)
predicted_labels = log.predict(validation_data)
print(f1_score(validation_labels, predicted_labels, average='macro'))
predicted_train = log.predict(train_data)
print(f1_score(train_labels, predicted_train, average='macro'))

# # Fit the random forest classifier
# clf = RandomForestClassifier(n_estimators=100)
# clf.fit(train_data, train_labels)
# predicted_labels = clf.predict(validation_data)
# print(f1_score(validation_labels, predicted_labels, average='macro'))
# print("Train score "+str(f1_score(train_labels, clf.predict(train_data), average='macro')))


# # # Fit the random forest classifier
# # clf = DecisionTreeClassifier()
# # clf.fit(train_data, train_labels)
# # predicted_labels = clf.predict(validation_data)
# # print(f1_score(validation_labels, predicted_labels, average='macro'))
# # print("Train score "+str(f1_score(train_labels, clf.predict(train_data), average='macro')))


# # # Gradient Boosted Trees
# # start_time = time.time()
# # clf = GradientBoostingClassifier(n_estimators=100)
# # clf.fit(train_data, train_labels)
# # predicted_labels = clf.predict(validation_data)
# # print(f1_score(validation_labels, predicted_labels, average='macro'))
# # print("Total time: "+str(time.time()-start_time))


# # # Fit a support vector machine
# # clf = SVC(kernel='linear')
# # clf.fit(train_data, train_labels)
# # predicted_labels = clf.predict(validation_data)
# # print(f1_score(validation_labels, predicted_labels, average='macro'))


# # test_labels = pd.DataFrame(clf.predict(test_data))
# # test_labels.to_csv("submission1.csv", index_label=['id','label'])
