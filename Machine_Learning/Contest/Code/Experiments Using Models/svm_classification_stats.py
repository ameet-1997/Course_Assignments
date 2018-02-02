import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_fscore_support

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

start_time = time.time()

# PCA
pca = pickle.load(open("../Models/pca_150.model", 'rb'))
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

# Retrieve Model
bag = pickle.load(open("../Models/svm_bag_C7_PCA150.model", 'rb'))

print("Done Loading in: "+str(time.time()-start_time))
start_time = time.time()

predicted_labels = bag.predict(validation_data)

[prec, rec, f1, sup] = precision_recall_fscore_support(validation_labels, predicted_labels)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

print(f1)

test_labels = pd.DataFrame(bag.predict(test_data))
test_labels.to_csv("sub1.csv", index_label=['id','label'])

print("Completed in: "+str(time.time()-start_time))

# x = np.array([(i+1) for i in range(len(f1))])
# plt.bar(x, height=f1)
# plt.xticks(x, x-1);
# plt.show()
