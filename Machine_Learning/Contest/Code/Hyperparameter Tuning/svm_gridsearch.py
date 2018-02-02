import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.utils import shuffle
import time
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV

# Load and impute the data using the mean
train_data = pd.read_csv("../../Data/train_knn_3.csv", header=None)

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,1:]
# train_data = train_data.iloc[:,1:-1]

# Get test data
test_data = pd.read_csv("../../Data/test_knn_3.csv", header=None)
# test_data = test_data.iloc[:,1:]

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# GridSearch
cvalues = [float(i)/10 for i in range(80, 100)]
clf = GridSearchCV(SVC(kernel='rbf'), param_grid={'C':cvalues}, cv=5)
clf.fit(train_data, train_labels)
print(clf.best_params_) 
