import pandas as pd
import numpy as np
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
from sklearn.model_selection import GridSearchCV

# Load and impute the data using the mean
total_data = pd.read_csv("train.csv")

# Get the train labels and subset the data
total_labels = total_data.iloc[:,-1]
total_data = total_data.iloc[:,1:-1]

# Impute it
i = Imputer()
total_data = i.fit_transform(total_data)
test_data = pd.read_csv("test.csv")
test_data = test_data.iloc[:,1:]
test_data = i.transform(test_data)

# Get validation data 8000:1000
train_data, validation_data, train_labels, validation_labels = train_test_split(total_data, total_labels, test_size=1000, random_state=42, shuffle=True)

print(train_data.shape)
print(test_data.shape)

# Perform some dimensionality reduction
# Make sure you scale the data after performing principal component analysis
pca = PCA(n_components=200)
pca.fit(total_data, total_labels)
total_data = pca.transform(total_data)
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)
# sc = StandardScaler()
# sc.fit(train_data)
# [train_data, validation_data, test_data] = [sc.transform(train_data), sc.transform(validation_data), sc.transform(test_data)]

print("Started Training")
print(total_data.shape)

# Train a logistic classifier
log = LogisticRegression()


log.fit(total_data, total_labels)
predicted_labels = log.predict(validation_data)
print(f1_score(validation_labels, predicted_labels, average='macro'))
predicted_train = log.predict(train_data)
print(f1_score(train_labels, predicted_train, average='macro'))
