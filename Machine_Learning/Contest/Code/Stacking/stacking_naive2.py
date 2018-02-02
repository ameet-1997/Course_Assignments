import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
from sklearn.svm import SVC
# import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import precision_recall_fscore_support

# Get the training data for stacking
f1 = pd.read_csv("sub_mlp_bag_validation_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_validation_stacking.csv",index_col=0)
[f1, f2] = [np.array(f1), np.array(f2)]
train_labels = pd.read_csv("validationlabels_stacking.csv", header=None)

print(f1.shape)

# Get validation data
mlpf1train, mlpf1test, svmf1train, svmf1test, train_labels, validation_labels = train_test_split(f1, f2, train_labels, test_size=.2, stratify=np.array(train_labels))

# Calculate Per class precision of the models
precision_mlp = precision_recall_fscore_support(train_labels, mlpf1train)[2]
precision_svm = precision_recall_fscore_support(train_labels, svmf1train)[2]

predicted_labels = []
for i in range(mlpf1test.shape[0]):
	if mlpf1test[i,0] == svmf1test[i,0]:
		predicted_labels.append(mlpf1test[i,0])
	else:
		if precision_mlp[mlpf1test[i,0]] > precision_svm[svmf1test[i,0]]:
			predicted_labels.append(mlpf1test[i,0])
		else:
			predicted_labels.append(svmf1test[i,0])

print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Get the test data
f1 = pd.read_csv("sub_mlp_bag_test_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_bagging_knnimpute_pca150.csv",index_col=0)
[f1, f2] = [np.array(f1), np.array(f2)]

test_labels = []
for i in range(f1.shape[0]):
	if f1[i,0] == f2[i,0]:
		test_labels.append(f1[i,0])
	else:
		if precision_mlp[f1[i,0]] > precision_svm[f2[i,0]]:
			test_labels.append(f1[i,0])
		else:
			test_labels.append(f2[i,0])
test_labels = np.array(test_labels)

# Create Submission File
column1 = np.array([[i] for i in np.arange(len(test_labels))])
to_write1 = np.hstack((column1,test_labels.reshape(-1,1)))
to_write1 = to_write1.astype(np.int32)

np.set_printoptions(suppress=True)
np.savetxt('stacking_naive2.csv',to_write1,delimiter=',',header='id,label',fmt='%d',comments='')