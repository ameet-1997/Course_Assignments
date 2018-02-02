import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from functions import modelfit

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

# GridSearch
# param_test = {'max_depth':range(4,9,1)}
param_test = {'n_estimators':range(100,201,100)}
clf = GridSearchCV(estimator = XGBClassifier(learning_rate =0.1, n_estimators=700, max_depth=6, min_child_weight=1, gamma=0, subsample=0.8, colsample_bytree=0.8, objective= 'multi:softmax', nthread=4, scale_pos_weight=1, seed=27, silent=True), 
param_grid = param_test, scoring='f1_macro',n_jobs=-1,iid=False, cv=5)
clf.fit(train_data, train_labels)
print(clf.best_params_)
print("Validation Score: "+str(f1_score(validation_labels, clf.predict(validation_data), average='macro')))