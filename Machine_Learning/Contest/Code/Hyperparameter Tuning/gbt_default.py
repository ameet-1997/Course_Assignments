import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

# Load and impute the data using the mean
train_data = pd.read_csv("../../Data/train_knn_3.csv", header=None)

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,:-1]
# train_data = train_data.iloc[:,1:-1]

# Get test data
test_data = pd.read_csv("../../Data/test_knn_3.csv", header=None)
# test_data = test_data.iloc[:,1:]

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# Dimensionality Reduction
pca = PCA(n_components=150)
pca.fit(train_data, train_labels)
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels))

# # Default Values
# start_time = time.time()
# gbm = GradientBoostingClassifier(n_estimators=50, verbose=2, learning_rate=0.1, min_samples_leaf=50)
# gbm.fit(train_data, train_labels)
# print("Validation Score: "+str(f1_score(validation_labels, gbm.predict(validation_data), average='macro')))
# print("Train Score: "+str(f1_score(train_labels, gbm.predict(train_data), average='macro')))
# print("Total time: "+str(time.time()-start_time))

# GridSearch
param_test = {'max_depth':range(1,8,1), 'min_samples_leaf':range(1,500,10)}
clf = GridSearchCV(estimator = GradientBoostingClassifier(min_samples_leaf=50,max_depth=8,max_features='sqrt',subsample=0.8,random_state=10, verbose=2), 
param_grid = param_test, scoring='f1_macro',n_jobs=4,iid=False, cv=5)
clf.fit(train_data, train_labels)
print(clf.best_params_)
print("Validation Score: "+str(f1_score(validation_labels, clf.predict(validation_data), average='macro')))