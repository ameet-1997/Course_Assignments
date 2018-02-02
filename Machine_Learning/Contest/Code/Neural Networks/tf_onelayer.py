import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
import pickle
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
from functions import fscore
from sklearn.preprocessing import OneHotEncoder

# Read Train Data
print( 'Reading Train Data..')
train_data_org = np.genfromtxt('../../Data/train_knn_3.csv',skip_header=0,delimiter=',')
# Reading Test Data2
print( 'Reading Test Data..')
test_data_org = np.genfromtxt('../../Data/test_knn_3.csv',skip_header=0,delimiter=',')

# Perform PCA
pca = PCA(n_components=150)
pca.fit(train_data_org[:,:-1])

# Test Train Split
train_feat, validation_feat, train_labels, validation_labels = train_test_split(train_data_org[:,:-1], train_data_org[:,-1], test_size=1000, stratify=np.array(train_data_org[:,-1]))

# One hot Encoding
enc = OneHotEncoder(sparse=False)
enc.fit(train_labels)
train_labels = enc.transform(train_labels)
validation_labels = enc.transform(validation_labels)

# Build model
model = Sequential()
model.add(Dense(units=100, input_dim=150))
model.add(Activation('relu'))
model.add(Dense(units=29))
model.add(Activation('softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
model.fit(pca.transform(train_feat), train_labels, epochs=10, batch_size=256, verbose=2)

#Testing
predicted_labels = model.predict(pca.transform(validation_feat))

# # Testing
# predicted_labels = bag.predict(pca.transform(validation_feat))
# print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average=None)))
# print("Net Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# # Writing Validation Output
# # pred_test = bag.predict(pca.transform(test_data_org))
# pred_validation_col = np.array([[i] for i in predicted_labels])

# # Merging Cells above
# file_lab1 = np.array([[i] for i in np.arange(len(predicted_labels))])

# to_write1 = np.hstack((file_lab1,pred_validation_col))
# to_write1 = to_write1.astype(np.int32)

# np.set_printoptions(suppress=True)
# np.savetxt('sub_mlp_bag_validation_stacking.csv',to_write1,delimiter=',',header='id,label',fmt='%d',comments='')