"""
This file has been used to complete assignment part 5 of PA1
Includes generating datasets and learning Linear Models on them

Author: Ameet Deshpande
RollNo: CS15B001
"""
import os
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Load the data generated in question 4
os.chdir("..")
path = os.getcwd()
os.chdir(path+str('/q4'))
data = read_csv('CandC-generated.csv', header=None)

# Change working directory to current folder
os.chdir("..")
path = os.getcwd()
os.chdir(path+str('/q5'))

test_data = [0 for i in range(5)]
train_data = [0 for i in range(5)]

for i in range(5):
	train_data[i], test_data[i] = train_test_split(data, test_size=0.2, random_state=np.random.randint(1,1000))

classifier = LinearRegression()

average_over_splits = 0.0

for i in range(5):
	classifier.fit(train_data[i].iloc[:,5:126], train_data[i].iloc[:,127])
	predicted_values = classifier.predict(test_data[i].iloc[:,5:126])
	average_over_splits += mean_squared_error(test_data[i].iloc[:,127], predicted_values)

average_over_splits /= 5
print("Mean Squared Error is: "+str(average_over_splits))
average_over_splits *= test_data[0].shape[0]
print("RSS is: "+str(average_over_splits))
# Average value seems close to 0.02
# Total average 0.7

# Write the dataframes to the files
for i in range(5):
	train_data[i].to_csv("CandC-train"+str(i+1)+".csv", header=False, index=False)
	test_data[i].to_csv("CandC-test"+str(i+1)+".csv", header=False, index=False)