import os



os.system('java -jar StackNet-master/StackNet.jar train task=classification sparse=false has_head=false model=model \
	pred_file=stacknet_pred.csv train_file=train_data.csv test_file=test_data.csv test_target=false params=params.txt verbose=true threads=7 metric=logloss stackdata=false seed=1 folds=2 bins=3')

