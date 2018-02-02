"""
This file has been used to do regression after removing a few features

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.linear_model import Ridge, LinearRegression, Lasso
from sklearn.metrics import mean_squared_error

path = os.getcwd()
os.chdir("..")
os.chdir("..")

train_data = []
test_data = []

for i in range(5):
	train_data.append(pd.read_csv(os.getcwd()+"/Dataset/CandC-train"+str(i+1)+str(".csv"), header=None))
	test_data.append(pd.read_csv(os.getcwd()+"/Dataset/CandC-test"+str(i+1)+str(".csv"), header=None))

# Change the working directory back to q6 folder
os.chdir(path)

best_lambda = 1.35

linear_regressor = LinearRegression()
ridge_regressor = Ridge(alpha=best_lambda)

ridge_regressor.fit(train_data[0].iloc[:,5:126], train_data[0].iloc[:,127])
linear_regressor.fit(train_data[0].iloc[:,5:126], train_data[0].iloc[:,127])

print("Coefficients for Ridge Regressor are: "+str(ridge_regressor.coef_))
print("Coefficients for Linear Regressor are: "+str(linear_regressor.coef_))

accuracies_list = []

threshold = 0.01
for i in range(10):
	threshold = 0.01*(i+1)
	boolean_array = (np.absolute(ridge_regressor.coef_) >= threshold)
	append_front = np.zeros(5, dtype=bool)
	append_back = np.zeros(1, dtype=bool)
	boolean_array = np.append(append_front, boolean_array)
	boolean_array = np.append(boolean_array, append_back)

	avr = 0.0
	for i in range(5):
		linear_regressor.fit(train_data[i].loc[:,boolean_array], train_data[i].iloc[:,127])
		predicted_values = linear_regressor.predict(test_data[i].loc[:,boolean_array])
		avr += mean_squared_error(test_data[i].iloc[:,127], predicted_values)
	accuracies_list.append(avr/5)

accuracies_list = np.array(accuracies_list)
accuracies_list *= test_data[0].shape[0]

print("Errors for different values of threshold: "+str(accuracies_list))