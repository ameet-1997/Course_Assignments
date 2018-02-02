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
from sklearn.ensemble import AdaBoostClassifier

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
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# Dimensionality Reduction
pca = PCA(n_components=200)
pca.fit(train_data, train_labels)
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

svm = SVC(probability=True, kernel='rbf', C=8)
ada = AdaBoostClassifier(svm, n_estimators=10)

start_time = time.time()
ada.fit(train_data, train_labels)
predicted_labels = ada.predict(validation_data)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
predicted_labels = ada.predict(train_data)
print("Train Score: "+str(f1_score(train_labels, predicted_labels, average='macro')))
print("Total time: "+str(time.time()-start_time))

test_labels = pd.DataFrame(ada.predict(test_data))
test_labels.to_csv("svm_boosting_10.csv", index=True, index_label=['id','label'])