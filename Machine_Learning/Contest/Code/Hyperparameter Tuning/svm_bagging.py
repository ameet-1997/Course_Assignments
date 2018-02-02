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

# Bagging Classifier
bag = BaggingClassifier(base_estimator=SVC(kernel='rbf', C=7, decision_function_shape='ovr'), n_estimators=50, n_jobs=-1)
bag.fit(train_data, train_labels)
train_predicted = bag.predict(train_data)
print("Train Score: "+str(f1_score(train_labels, train_predicted, average='macro')))
predicted_labels = bag.predict(validation_data)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

test_labels = pd.DataFrame(bag.predict(test_data))
test_labels.to_csv("svm_bagging_test.csv", index_label=['id','label'])