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

# Get the training data for stacking
enc = OneHotEncoder(sparse=False)
f1 = pd.read_csv("sub_mlp_bag_validation_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_validation_stacking.csv",index_col=0)
[f1, f2] = [np.array(f1), np.array(f2)]

# print(feature_1)

enc.fit(f1)
[feature_1, feature_2] = [enc.transform(f1), enc.transform(f2)]

train_data = pd.concat([pd.DataFrame(feature_1), pd.DataFrame(feature_2)], axis=1)
# train_data = pd.concat([pd.DataFrame(f1), pd.DataFrame(f2)], axis=1)
train_labels = pd.read_csv("validationlabels_stacking.csv", header=None)


# Get validation data
mlpf1train, mlpf1test, svmf1train, svmf1test, train_data, validation_data, train_labels, validation_labels = train_test_split(f1, f2, train_data, train_labels, test_size=.2, stratify=np.array(train_labels))

# Train a classifier
max_score = 0
c_value = 0
for c in [float(i+1)/10 for i in range(10)]:
	clf = BaggingClassifier(base_estimator=SVC(kernel='linear',C=c), n_estimators=20)
	# clf = SVC(kernel='linear',C=c)
	clf.fit(train_data, np.array(train_labels).ravel())
	predicted_labels = clf.predict(validation_data)
	predicted_labels[mlpf1test.flatten()==svmf1test.flatten()] = mlpf1test.flatten()[mlpf1test.flatten()==svmf1test.flatten()]
	validation_score = f1_score(validation_labels, predicted_labels, average='macro')
	if validation_score > max_score:
		max_score = validation_score
		c_value = c
	print("Validation Score: "+str(validation_score))


# Main Classifier
clf = BaggingClassifier(base_estimator=SVC(kernel='linear',C=c_value), n_estimators=20)
# clf = SVC(kernel='linear',C=c)
clf.fit(train_data, np.array(train_labels).ravel())
predicted_labels = clf.predict(validation_data)
predicted_labels[mlpf1test.flatten()==svmf1test.flatten()] = mlpf1test.flatten()[mlpf1test.flatten()==svmf1test.flatten()]
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Get the test data
f1 = pd.read_csv("sub_mlp_bag_test_stacking.csv",index_col=0)
f2 = pd.read_csv("svm_bagging_knnimpute_pca150.csv",index_col=0)
[f1, f2] = [np.array(f1), np.array(f2)]
[feature_1, feature_2] = [enc.transform(f1), enc.transform(f2)]
test_data = pd.concat([pd.DataFrame(feature_1), pd.DataFrame(feature_2)], axis=1)
# test_data = pd.concat([pd.DataFrame(f1), pd.DataFrame(f2)], axis=1)

# Create Submission File
test_labels = pd.DataFrame(clf.predict(test_data))
test_labels[f1.flatten()==f2.flatten()] = f1[f1.flatten()==f2.flatten()]
test_labels.to_csv("svm_test_stacking_new_1.csv", index_label=['id','label'])