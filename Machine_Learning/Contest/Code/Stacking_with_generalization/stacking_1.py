from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from vecstack import stacking
from sklearn.svm import SVC
from sklearn.metrics import f1_score
import numpy as np
import pandas as pd
import time
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

# Read Train Data
print( 'Reading Train Data..')
train_data_org = np.genfromtxt('../../Data/train_knn_3.csv',skip_header=0,delimiter=',')
# Reading Test Data2
print( 'Reading Test Data..')
test_data_org = np.genfromtxt('../../Data/test_knn_3.csv',skip_header=0,delimiter=',')

# train_data_org = train_data_org[:200,:]

# Perform PCA
pca = PCA(n_components=150)
pca.fit(train_data_org[:,:-1])

train_feat, validation_feat, train_labels, validation_labels = train_test_split(train_data_org[:,:-1], train_data_org[:,-1], test_size=1000, stratify=np.array(train_data_org[:,-1]))
train_feat = pca.transform(train_feat)
validation_feat = pca.transform(validation_feat)


models = [
    SVC(kernel='rbf', C=7),
        
    RandomForestClassifier(random_state = 0, n_jobs = -1, 
        n_estimators = 100, max_depth = 3)]
    
# Compute stacking features
S_train, S_test = stacking(models, train_feat, train_labels, validation_feat, 
    regression = False, metric = accuracy_score, n_folds = 4, 
    stratified = True, shuffle = True, random_state = 0, verbose = 2)

# Initialize 2-nd level model
model =     RandomForestClassifier(random_state = 0, n_jobs = -1, 
        n_estimators = 100, max_depth = 3)
# model = LogisticRegression()
    
# Fit 2-nd level model
model = model.fit(S_train, train_labels)

# Predict
y_pred = model.predict(S_test)

# Final prediction score
print('Final prediction score: [%.8f]' % f1_score(validation_labels, y_pred, average='macro'))
