import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import precision_recall_fscore_support

# Get the training data for stacking
f1 = pd.read_csv("sub_mlp_bag_validation_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_validation_stacking.csv",index_col=0)
f3 = pd.read_csv("xgboost_validation.csv", index_col=0)
[f1, f2, f3] = [np.array(f1), np.array(f2), np.array(f3)]
train_labels_old = pd.read_csv("validationlabels_stacking_old.csv", header=None)
train_labels_new = pd.read_csv("validationlabels_stacking.csv", header=None)

print(f1.shape)

# Get validation data
mlpf1train, mlpf1test, svmf1train, svmf1test, train_labels_old, validation_labels_old = train_test_split(f1, f2, train_labels_old, test_size=.2, stratify=np.array(train_labels_old))

unique, counts = np.unique(train_labels_new, return_counts=True)
# print(dict(zip(unique, counts)))
print(train_labels_new.shape)


#Get validation data for XGBoost
xgtrain, xgtest, train_labels_new, validation_labels_new = train_test_split(f3, train_labels_new, test_size=.2, stratify=np.array(train_labels_new))

# Calculate Per class precision of the models
precision_mlp = precision_recall_fscore_support(train_labels_old, mlpf1train)[0]
precision_svm = precision_recall_fscore_support(train_labels_old, svmf1train)[0]
precision_xg = precision_recall_fscore_support(train_labels_new, xgtrain)[0]

predicted_labels = []
for i in range(xgtest.shape[0]):
	temp = max(mlpf1test[i,0], svmf1test[i,0], xgtest[i,0])
	if temp == mlpf1test[i,0]:
		predicted_labels.append(mlpf1test[i,0])
	elif temp == svmf1test[i,0]:
		predicted_labels.append(svmf1test[i,0])
	else:
		predicted_labels.append(xgtest[i,0])

print("Validation Score: "+str(f1_score(validation_labels_new, predicted_labels, average='macro')))

# Get the test data
f1 = pd.read_csv("sub_mlp_bag_test_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_bagging_knnimpute_pca150.csv",index_col=0)
f3 = pd.read_csv("xgboost_test.csv", index_col=0)
[f1, f2, f3] = [np.array(f1), np.array(f2), np.array(f3)]

test_labels = []
for i in range(f1.shape[0]):
	[p1, p2, p3] = [precision_mlp[f1[i,0]], precision_svm[f2[i,0]], precision_xg[f3[i,0]]]
	temp = max(p1, p2, p3)
	if f1[i,0] == f2[i,0]:
		test_labels.append(f1[i,0])
	elif f2[i,0] == f3[i,0]:
		test_labels.append(f1[i,0])
	elif f3[i,0] == f1[i,0]:
		test_labels.append(f1[i,0])
	elif temp == p1:
		test_labels.append(f1[i,0])
	elif temp == p2:
		test_labels.append(f2[i,0])
	else:
		test_labels.append(f3[i,0])

test_labels = np.array(test_labels)

# Create Submission File
column1 = np.array([[i] for i in np.arange(len(test_labels))])
to_write1 = np.hstack((column1,test_labels.reshape(-1,1)))
to_write1 = to_write1.astype(np.int32)

np.set_printoptions(suppress=True)
# np.savetxt('stacking_naive2.csv',to_write1,delimiter=',',header='id,label',fmt='%d',comments='')

x = np.array([(i+1) for i in range(len(precision_xg))])
plt.bar(x, height=precision_xg)
plt.xticks(x, x-1);
plt.show()