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
from sklearn.cluster import DBSCAN, KMeans, AgglomerativeClustering
from sklearn.metrics import v_measure_score

# Load and impute the data using the mean
train_data = pd.read_csv("../../Data/train_knn_3.csv", header=None)

# Get the train labels and subset the data
train_labels = np.array(train_data.iloc[:,-1])
train_data = np.array(train_data.iloc[:,:-1])
# train_data = train_data.iloc[:,1:-1]

# Get test data
test_data = pd.read_csv("../../Data/test_knn_3.csv", header=None)

# # Get validation data
# train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# Dimensionality Reduction
pca = PCA(n_components=150)
pca.fit(train_data, train_labels)
train_data = pca.transform(train_data)
# validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data) 


# train_labels = train_labels.reshape((-1,1))
# # Write training data
# train_data = np.hstack((train_labels, train_data))
# np.savetxt('train_data.csv',train_data,delimiter=',',header='',fmt='%d',comments='')
# np.savetxt('test_data.csv',test_data,delimiter=',',header='',fmt='%d',comments='')







# clusterer = DBSCAN(eps=0.01, min_samples=100)
# clusterer = KMeans(n_clusters=29)
# clusterer = AgglomerativeClustering(n_clusters=29, linkage='ward')
# clusterer.fit(train_data, train_labels)
# predicted_labels = clusterer.fit_predict(train_data)
# print(v_measure_score(train_labels, predicted_labels))
# print(np.count(clusterer.labels_ == -1))