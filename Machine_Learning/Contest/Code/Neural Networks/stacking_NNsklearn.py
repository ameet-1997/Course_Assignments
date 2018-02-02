import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
#from fancyimpute import KNN
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
import pickle
from sklearn.svm import SVC
import tensorflow as tf

# Read Train Data
print( 'Reading Train Data..')
train_data_org = np.genfromtxt('../../Data/train_knn_3.csv',skip_header=0,delimiter=',')
# Reading Test Data2
print( 'Reading Test Data..')
test_data_org = np.genfromtxt('../../Data/test_knn_3.csv',skip_header=0,delimiter=',')

# Perform PCA
pca = PCA(n_components=150)
pca.fit(train_data_org[:,:-1])
pickle.dump(pca, open("pca_150.model", 'wb')) 	# Dump the PCA Model

train_feat, validation_feat, train_labels, validation_labels = train_test_split(train_data_org[:,:-1], train_data_org[:,-1], test_size=1000, stratify=np.array(train_data_org[:,-1]))

# Validation Labels file
validation_labels1 = pd.DataFrame(validation_labels)
validation_labels1.to_csv("validationlabels_stacking.csv")

# Intialising the neural net
mlp = MLPClassifier(hidden_layer_sizes=(150,),activation='relu',learning_rate='adaptive',max_iter=1000,verbose=True, validation_fraction=0.1)

# Perform bagging with neural net
bag = BaggingClassifier(base_estimator=mlp, n_estimators=200, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=False, oob_score=False, warm_start=False, n_jobs=-1, random_state=None, verbose=True)
bag.fit(pca.transform(train_feat), train_labels)

pickle.dump(bag, open("mlp_bag200.model", 'wb')) 	# Dump the NN Model

# Testing
predicted_labels = bag.predict(pca.transform(validation_feat))
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average=None)))
print("Net Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Writing Validation Output
# pred_test = bag.predict(pca.transform(test_data_org))
pred_validation_col = np.array([[i] for i in predicted_labels])

# Merging Cells above
file_lab1 = np.array([[i] for i in np.arange(len(predicted_labels))])

to_write1 = np.hstack((file_lab1,pred_validation_col))
to_write1 = to_write1.astype(np.int32)

np.set_printoptions(suppress=True)
np.savetxt('sub_mlp_bag_validation_stacking.csv',to_write1,delimiter=',',header='id,label',fmt='%d',comments='')




# Writing Test Output
pred_test = bag.predict(pca.transform(test_data_org))
pred_test_col = np.array([[i] for i in pred_test])

# Merging Cells above
file_lab = np.array([[i] for i in np.arange(len(pred_test))])

to_write = np.hstack((file_lab,pred_test_col))
to_write = to_write.astype(np.int32)

np.set_printoptions(suppress=True)
np.savetxt('sub_mlp_bag_test_stacking.csv',to_write,delimiter=',',header='id,label',fmt='%d',comments='')


# SVM Model

# Bagging Classifier
bag = BaggingClassifier(base_estimator=SVC(kernel='rbf', C=7), n_estimators=50, n_jobs=-1)
bag.fit(pca.transform(train_feat), train_labels)
# print("Train Score: "+str(f1_score(train_labels, train_predicted, average='macro')))
print("Validation Score: "+str(f1_score(validation_labels, bag.predict(pca.transform(validation_feat)), average='macro')))

pickle.dump(bag, open("svm_bag_C7_PCA150.model", 'wb'))

validation_labels = pd.DataFrame(bag.predict(pca.transform(validation_feat)))
validation_labels.to_csv("svm_validation_stacking.csv", index_label=['id','label'])

test_labels = pd.DataFrame(bag.predict(pca.transform(test_data_org)))
test_labels.to_csv("svm_test_stacking.csv", index_label=['id','label'])