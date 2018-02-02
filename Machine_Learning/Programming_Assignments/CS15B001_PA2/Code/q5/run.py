"""
Python script to execute bash commands to train and test
decision trees using weka classifier and mushroom dataset

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
from functions import get_min_num_obj, get_min_num_obj_accuracy
import matplotlib.pyplot as plt

# Train the classifier and test it on dataset
# Baseline model, the results are stored in output.txt
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -U >output.txt")

# Generate the graphviz code to visualize the tree
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -U -g >Plots/baseline.tex")

# Run the tree for different values of MinNumObj
for i in range(1, 100):
	os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -M "+str(i)+" >logfiles_minnumobj/"+str(i)+".txt")

# Get the variation of Number of leaves with respect to MinNumObj
[xval, yval] = get_min_num_obj()
plt.plot(xval, yval)
plt.show()

# Get the Fscores with respect to MinNumObj
[xval, yval] = get_min_num_obj_accuracy()
plt.plot(xval, yval)
plt.show()

# Build the tree using reduced error pruning
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -R -N 10 >output.txt")

# Generate the graphviz code to visualize the tree
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -R -N 10 -g >Plots/reduced.tex")

# Use -d option to dump the tree and -l option to load the tree
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -t ARFFFiles/mushroom_train.arff -T ARFFFiles/mushroom_test.arff -R -N 10 -d J48.model")

# Load the decision tree and predict on the test set
os.system("java -cp weka-3-8-1/weka.jar weka.classifiers.trees.J48 -l J48.model -T ARFFFiles/mushroom_test.arff >output.txt")