import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
from functions import get_purity 

# Single Link Hierarchical
num_Clusters = [i for i in range(1,20)]
max_purity = 100
max_cluster = 0
distance_measure = ['SINGLE', 'COMPLETE', 'ADJCOMPLETE', 'AVERAGE', 'MEAN', 'CENTROID', 'WARD', 'NEIGHBOR_JOINING']

for d in distance_measure:
	for n in num_Clusters:
		os.system("java -cp weka-3-8-1/weka.jar weka.clusterers.HierarchicalClusterer -N "+str(n)+" -L "+d+" -P -A \"weka.core.EuclideanDistance -R first-last\" -t \"/media/ameet/8AD2C89ED2C88FBD/Books and Documents/Academics/IIT/IIT Material/Sem 5/Machine Learning/Lab/Assignment 3/q1/ARFF_Files/Flames.arff\" -c last >k8r15_log.txt")
		purity = get_purity('k8r15_log.txt')
		if purity < max_purity:
			max_purity = purity
			max_cluster = n
	max_purity = 100 - max_purity
	print("Purity is: "+str(max_purity)+"::Max Cluster::"+str(max_cluster)+"::"+d)