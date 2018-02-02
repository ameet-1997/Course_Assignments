import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
from functions import get_purity

# java -cp weka-3-8-1/weka.jar weka.clusterers.SimpleKMeans -t "/media/ameet/8AD2C89ED2C88FBD/Books and Documents/Academics/IIT/IIT Material/Sem 5/Machine Learning/Lab/Assignment 3/q1/ARFF_Files/R15.arff" -N 5 -c last

# Have to run the KMeans algorithm multiple times with different initializations to get the best score

# Checking the K=8 case
seed_values = [i for i in range(1,101)]

max_purity = 100
max_seed = 0
for seed in seed_values:
	os.system("java -cp weka-3-8-1/weka.jar weka.clusterers.SimpleKMeans -t \"/media/ameet/8AD2C89ED2C88FBD/Books and Documents/Academics/IIT/IIT Material/Sem 5/Machine Learning/Lab/Assignment 3/q1/ARFF_Files/R15.arff\" -N 8 -c last -S "+str(seed)+" >k8r15_log.txt")
	purity = get_purity('k8r15_log.txt')
	if purity < max_purity:
		max_purity = purity
		max_seed = seed
max_purity = 100 - max_purity
print("Purity is: "+str(max_purity))

# Running KMeans for different values of number of clusters
seed_values = [i for i in range(1,101)]
k_values = [i for i in range(1,21)]
purity_values = []

for k in k_values:
	max_purity = 100
	max_seed = 0
	for seed in seed_values:
		os.system("java -cp weka-3-8-1/weka.jar weka.clusterers.SimpleKMeans -t \"/media/ameet/8AD2C89ED2C88FBD/Books and Documents/Academics/IIT/IIT Material/Sem 5/Machine Learning/Lab/Assignment 3/q1/ARFF_Files/R15.arff\" -N "+str(k)+" -c last -S "+str(seed)+" >k8r15_log.txt")
		purity = get_purity('k8r15_log.txt')
		if purity < max_purity:
			max_purity = purity
			max_seed = seed
	max_purity = 100 - max_purity
	purity_values.append(max_purity)
	print("Value of k is: "+str(k))
	print("Max purity is: "+str(max_purity))
	print("Max seed is: "+str(max_seed))
	print("")

# Plot the graph
plt.plot(k_values,purity_values)
plt.show()