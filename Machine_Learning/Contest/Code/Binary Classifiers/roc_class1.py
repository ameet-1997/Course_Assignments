import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
import time
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier

# Load and impute the data using the mean
train_data = pd.read_csv("../../Data/train_knn_3.csv", header=None)

# Get the train labels and subset the data
train_labels = np.array(train_data.iloc[:,-1])

# Binarize the labels
train_labels[train_labels != 1] = 2
train_labels[train_labels == 1] = 1
train_labels[train_labels == 2] = 0

train_data = np.array(train_data.iloc[:,:-1])


# DownSample the majority classes to get a more balanced dataset
train_reduce_to = 200
new_dataset1 = train_data[train_labels == 1]
new_dataset2 = train_data[train_labels == 0]
np.random.shuffle(new_dataset2)
new_dataset2 = new_dataset2[:train_reduce_to,:]
train_data1 = np.vstack((new_dataset1, new_dataset2))
train_labels1 = np.hstack((np.ones(new_dataset1.shape[0]), np.zeros(new_dataset2.shape[0])))


# Get test data
test_data = pd.read_csv("../../Data/test_knn_3.csv", header=None)

# Get validation data
train_data, validation_data, train_labels, validation_labels = train_test_split(train_data, train_labels, test_size=.33, stratify=np.array(train_labels), random_state=42) 

# Dimensionality Reduction
pca = PCA(n_components=150)
pca.fit(train_data1, train_labels1)
train_data1 = pca.transform(train_data1)
validation_data = pca.transform(validation_data)
test_data = pca.transform(test_data)

n_classes = 2

# Learn to predict each class against the other
classifier = SVC(kernel='rbf', probability=True, random_state=42, C=1)
y_score = classifier.fit(train_data1, train_labels1).decision_function(validation_data)

predicted_labels = classifier.predict(validation_data)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Check the decision function results
p = np.argsort(y_score)
# print(y_score[p])
# print(validation_labels[p])
# print(np.count_nonzero(validation_labels))

# Higher values of decision function represent the class which is labeled as 1

# Using y_score to get the Operating point of the ROC Curve
# Decision Function represents the distance of the points from 

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
fpr[0], tpr[0], _ = roc_curve(validation_labels, y_score, pos_label=1)
roc_auc[0] = auc(fpr[0], tpr[0])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(validation_labels.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])


##############################################################################
# Plot of a ROC curve for a specific class
plt.figure()
lw = 2
plt.plot(fpr[0], tpr[0], color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc[0])
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()