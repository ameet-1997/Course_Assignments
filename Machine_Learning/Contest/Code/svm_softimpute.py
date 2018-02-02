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
from fancyimpute import KNN

# Load and impute the data using the mean
train_data = pd.read_csv("../Data/train_softimpute.csv", header=None)
train_labels = pd.read_csv("../Data/train.csv").iloc[:,-1]

# Get test data
test_data = pd.read_csv("../Data/test_softimpute.csv", header=None)

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# Dimensionality Reduction
pca = PCA(n_components=200)
pca.fit(train_data, train_labels)
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

# Bagging Classifier
# Validation can be used to test, but eventually bag with the entire data for better results
start_time = time.time()
bag = BaggingClassifier(base_estimator=SVC(kernel='rbf', C=8), n_estimators=50, n_jobs=-1)
bag.fit(train_data, train_labels)
train_predicted = bag.predict(train_data)
print("Train Score: "+str(f1_score(train_labels, train_predicted, average='macro')))
predicted_labels = bag.predict(validation_data)
print("Validation Score: "+str(f1_score(train_labels, train_predicted, average='macro')))
print("Total time: "+str(time.time()-start_time))



test_labels = pd.DataFrame(bag.predict(test_data))
test_labels.to_csv("Submissions/svm_bagging_softimpute.csv", index_label=['id','label'])

# # Gaussian Kernel
# start_time = time.time()
# # lin = SVC(kernel='poly', degree=4)
# lin = SVC(kernel='rbf', C=8)
# lin.fit(train_data, train_labels)
# predicted_labels = lin.predict(validation_data)
# print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
# print("Total time: "+str(time.time()-start_time))

# test_labels = pd.DataFrame(lin.predict(test_data))
# test_labels.to_csv("Submissions/svm_rbf_knnimpute.csv", index=True, index_label=['id','label'])