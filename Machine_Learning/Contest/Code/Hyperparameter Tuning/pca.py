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


components = [i for i in range(150, 300, 10)]
cvalues = [(6+float(i)/3) for i in range(12)]

# components = [i for i in range(50, 300, 10)]
fscore = []

for comp in components:
	for c in cvalues:
		# Dimensionality Reduction
		start_time = time.time()
		pca = PCA(n_components=comp)
		pca.fit(train_data, train_labels)
		train_data1 = pca.transform(train_data)
		validation_data1 = pca.transform(validation_data)
		print("Train Data Shape: "+str(train_data.shape))
		print("Here")
		svm = SVC(kernel='rbf', C=7)
		svm.fit(train_data1, train_labels)
		train_predicted = svm.predict(train_data1)
		print("Train Score: "+str(f1_score(train_labels, train_predicted, average='macro')))
		print("Total time: "+str(time.time()-start_time))
		predicted_labels = svm.predict(validation_data1)
		print("C: "+str(c)+"::"+"Components: "+str(comp))
		print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))
		fscore.append(f1_score(validation_labels, predicted_labels, average='macro'))

plt.xlabel('Components')
plt.ylabel('F-Score')
plt.plot(components, fscore)
plt.show()