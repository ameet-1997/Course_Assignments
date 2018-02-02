"""
This file has been used to complete assignment part 6 of PA1
Includes running Ridge regression for different
values of lambda

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
import pandas as pd
import numpy as np
from pandas import read_csv
from sklearn.linear_model import Ridge
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

lambda_values = [0.05*i for i in range(40)]
average_values = []

lambda_best_fit = 0
best_fit = 10000

for lam in lambda_values:
	classifier = Ridge(alpha=lam)
	avr = 0.0
	for i in range(5):
		classifier.fit(train_data[i].iloc[:,5:126], train_data[i].iloc[:,127])
		predicted_values = classifier.predict(test_data[i].iloc[:,5:126])
		# print("The error is: "+str(mean_squared_error(test_data[i].iloc[:,127], predicted_values)))
		avr += mean_squared_error(test_data[i].iloc[:,127], predicted_values)
		np.savetxt("coeffs_"+str(lam)+"_"+str(i+1)+".csv", classifier.coef_,delimiter=',')
	average_values.append(avr/5)
	if avr/5 < best_fit:
		best_fit = avr/5
		lambda_best_fit = lam

print("The Best fit error is: "+str(best_fit*test_data[0].shape[0]))
print("Value of lambda for corresponding fit: "+str(lambda_best_fit))

np.savetxt("error_lambda.csv", np.array(average_values), delimiter=',')