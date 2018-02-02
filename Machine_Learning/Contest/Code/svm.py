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
train_data = pd.read_csv("../Data/train.csv")

# Get the train labels and subset the data
train_labels = train_data.iloc[:,-1]
train_data = train_data.iloc[:,1:-1]
train_data = KNN(k=3).complete(train_data)

# Impute it
i = Imputer(strategy='median')
train_data = i.fit_transform(train_data)
test_data = pd.read_csv("../Data/test.csv")
test_data = test_data.iloc[:,1:]
test_data = i.transform(test_data)

print("Done with imputation")

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=1000, stratify=np.array(train_labels)) 

# Dimensionality Reduction
pca = PCA(n_components=200)
pca.fit(train_data, train_labels)
train_data = pca.transform(train_data)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

# Gaussian Kernel
start_time = time.time()
# lin = SVC(kernel='poly', degree=4)
lin = SVC(kernel='rbf', C=8)
lin.fit(train_data, train_labels)
predicted_labels = lin.predict(validation_data)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
print("Total time: "+str(time.time()-start_time))

test_labels = pd.DataFrame(lin.predict(test_data))
test_labels.to_csv("Submissions/svm_rbf_knnimpute.csv", index=True, index_label=['id','label'])

# # Hyperparameter tuning
# cvalues = [(i+1) for i in range(10)]
# fscores = []
# for c in cvalues:
# 	# Linear Kernel
# 	start_time = time.time()
# 	lin = SVC(kernel='rbf', C=c)
# 	lin.fit(train_data, train_labels)
# 	predicted_labels = lin.predict(validation_data)
# 	print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
# 	print("Total time: "+str(time.time()-start_time))
# 	fscores.append(f1_score(validation_labels, predicted_labels, average='macro'))

# plt.xlabel("C values")
# plt.ylabel("F Scores")
# plt.plot(cvalues, fscores)
# plt.show()

