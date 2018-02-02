import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
#from fancyimpute import KNN
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier

# Read Train Data
print 'Reading Train Data..'
train_data_org = np.genfromtxt('../Data/train_knn_3.csv',skip_header=0,delimiter=',')
# Reading Test Data2
print 'Reading Test Data..'
test_data_org = np.genfromtxt('../Data/test_knn_3.csv',skip_header=0,delimiter=',')

# Perform PCA
pca = PCA(n_components=150)
pca.fit(train_data_org[:,:-1])

train_feat, validation_feat, train_labels, validation_labels = train_test_split(train_data_org[:,:-1], train_data_org[:,-1], test_size=1000, stratify=np.array(train_data_org[:,-1]))

# Intialising the neural net
mlp = MLPClassifier(hidden_layer_sizes=(150,),activation='relu',learning_rate='adaptive',max_iter=1000,verbose=True, validation_fraction=0.1)

# Perform bagging with neural net
bag = BaggingClassifier(base_estimator=mlp, n_estimators=100, max_samples=1.0, max_features=1.0, bootstrap=True, bootstrap_features=True, oob_score=False, warm_start=False, n_jobs=-1, random_state=None, verbose=True)
bag.fit(pca.transform(train_feat), train_labels)


# Testing
predicted_labels = bag.predict(pca.transform(validation_feat))
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average=None)))
print("Net Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Writing Test Output
pred_test = bag.predict(pca.transform(test_data_org))
pred_test_col = np.array([[i] for i in pred_test])

# Merging Cells above
file_lab = np.array([[i] for i in np.arange(len(pred_test))])

to_write = np.hstack((file_lab,pred_test_col))
to_write = to_write.astype(np.int32)

np.set_printoptions(suppress=True)
np.savetxt('../dataset/sub_mlp_bag.csv',to_write,delimiter=',',header='id,label',fmt='%d',comments='')

 
