import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import BaggingRegressor
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils.np_utils import to_categorical
from keras.wrappers.scikit_learn import KerasClassifier
from keras.callbacks import EarlyStopping,ModelCheckpoint

# Read Train Data
print('Reading Train Data..')
train_data_org = np.genfromtxt('../../Data/train_knn_3.csv',skip_header=0,delimiter=',')
# Reading Test Data2
print('Reading Test Data..')
test_data_org = np.genfromtxt('../../Data/test_knn_3.csv',skip_header=0,delimiter=',')

# Perform PCA
#print 'Doing PCA'
#pca = PCA(n_components=784)
#pca.fit(train_data_org[:,:-1])

train_feat, validation_feat, train_labels, validation_labels = train_test_split(train_data_org[:,:-1], train_data_org[:,-1], test_size=1000, stratify=np.array(train_data_org[:,-1]))

'''
train_feat_trans = pca.transform(train_feat)
val_feat_trans = pca.transform(validation_feat)
'''
train_lab_to_cat = to_categorical(train_labels)
val_lab_to_cat = to_categorical(validation_labels)
#train_feat_trans = pca.transform(train_feat).reshape(train_feat.shape[0],28,28,1)
#val_feat_trans = pca.transform(validation_feat).reshape(1000,28,28,1)
#train_cat = to_categorical(train_labels)
# Intialising the neural net
print('Initialising Net')

def create_model():
	model = Sequential()
	
	model.add(Dense(256, activation='relu',input_dim=512))
	
	#model.add(Convolution2D(8, 3, 3, activation='relu', input_shape=(28,28,1)))
#	model.add(Convolution2D(16, 3, 3, activation='relu'))
	#model.add(MaxPooling2D(pool_size=(2,2)))
	#model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dropout(0.2))
	model.add(Dense(64, activation='tanh'))
	model.add(Dropout(0.5))
	model.add(Dense(29, activation='softmax'))
	
	'''
	model.add(Dense(units=150, input_dim=150,activation='relu'))
#	model.add(Dropout(0.5))
	model.add(Dense(units=150, activation='relu'))
	model.add(Dropout(0.25))
	model.add(Dense(units=150, activation='relu'))
	model.add(Dropout(0.25))
	model.add(Dense(units=29,activation='softmax'))
	'''
	model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=['accuracy'])
	return model

callbacks = [
#    EarlyStopping(monitor='val_acc', min_delta=0.001, patience=10,verbose=1),
#    EarlyStopping(monitor='val_loss',min_delta=0.0001, patience=10, verbose=1),
    ModelCheckpoint('../../Data/tmp_mod_k1.hdf5', monitor='val_acc', save_best_only=True, period=1,verbose=1,mode='max'),
]

#model = create_model()
#model.fit(train_feat,train_lab_to_cat,batch_size=256,nb_epoch=256,verbose=1,validation_data=(validation_feat,val_lab_to_cat),callbacks=callbacks)

k_model = KerasClassifier(build_fn=create_model,batch_size=256,nb_epoch=4,verbose=1)
#model.fit(train_feat,train_lab_to_cat,batch_size=256,nb_epoch=1000,verbose=1,validation_data=(validation_feat,val_lab_to_cat),callbacks=callbacks)
# Perform bagging with neural net

# Writing Out bagging Program
mod = []
arr = []
for i in range(4):
	arri = np.random.choice(2600,512,replace=True)
	callbacks = [
#    EarlyStopping(monitor='val_acc', min_delta=0.001, patience=10,verbose=1),
    EarlyStopping(monitor='val_loss',min_delta=0.0001, patience=10, verbose=1),
    ModelCheckpoint('../../Data/tmp_mod_k'+str(i)+'.hdf5', monitor='val_acc', save_best_only=True, period=1,verbose=1,mode='max')]
	model = create_model()
	model.fit(train_feat[:,arri],train_lab_to_cat,nb_epoch=300,validation_data=(validation_feat[:,arri],val_lab_to_cat),callbacks=callbacks)
	mod.append(model)
	arr.append(arri)


# # With different bagging on mlp
# mlp = MLPClassifier(hidden_layer_sizes=(256,128,64,),max_iter=1000,verbose=True)
# bag = BaggingClassifier(base_estimator=mlp, n_estimators=100, max_samples=1.0, max_features=0.2, bootstrap=True, bootstrap_features=True, oob_score=False, warm_start=False, n_jobs=-1, random_state=None, verbose=True)
# bag.fit(train_feat, train_labels)

model = create_model()
model.load_weights('../../Data/tmp_mod1.hdf5')

# Testing
i = 2
predicted_labels = np.argmax(mod[i].predict(validation_feat[:,arr[i]]),axis=1)
# predicted_labels = bag.predict(validation_feat)
print("Validation Score: "+str(f1_score(validation_labels, predicted_labels, average=None)))
print("Net Validation Score: "+str(f1_score(validation_labels, predicted_labels, average='macro')))

# Writing Test Output
pred_test = np.argmax(model.predict(pca.transform(test_data_org)),axis=1)
pred_test_col = np.array([[i] for i in pred_test])

# Merging Cells above
file_lab = np.array([[i] for i in np.arange(len(pred_test))])

to_write = np.hstack((file_lab,pred_test_col))
to_write = to_write.astype(np.int32)

np.set_printoptions(suppress=True)
np.savetxt('../../Data/sub_mlp_keras.csv',to_write,delimiter=',',header='id,label',fmt='%d',comments='')


