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
from sklearn.neighbors import KNeighborsClassifier

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

# KNN
start_time = time.time()
# lin = SVC(kernel='rbf', C=8)
knn = KNeighborsClassifier(n_neighbors=1, n_jobs=-1)
knn.fit(train_data, train_labels)
predicted_labels = knn.predict(validation_data)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
print("Total time: "+str(time.time()-start_time))

# test_labels = pd.DataFrame(knn.predict(test_data))
# test_labels.to_csv("svm_knn.csv", index=True, index_label=['id','label'])

# Hyperparameter tuning
kvalues = [(i+1) for i in range(100)]
fscores = []
for k in kvalues:
	start_time = time.time()
	knn = KNeighborsClassifier(n_neighbors=k, n_jobs=2)
	knn.fit(train_data, train_labels)
	predicted_labels = knn.predict(validation_data)
	print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
	print("Total time: "+str(time.time()-start_time))
	fscores.append(f1_score(validation_labels, predicted_labels, average='macro'))

plt.xlabel("K values")
plt.ylabel("F Scores")
plt.plot(kvalues, fscores)
plt.show()

