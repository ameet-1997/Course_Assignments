import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Construct 2-D plots for all classes based on their class label

# Get all the CSV file names
file_names = os.listdir("CSV_Files/")

# Colours being used for clusters in a cyclic fashion
colors = ['b','g','r','c','m','y','k']

for file in file_names:
	# Get all the unique labels for the classes
	df = np.array(pd.read_csv("CSV_Files/"+file))
	unique_labels = np.unique(np.array(df[:,2]).flatten())

	# Plot the figure
	fig = plt.figure()
	sub = fig.add_subplot(111)

	# Scatter plot
	for i in range(unique_labels.shape[0]):
		temp_df = df[df[:,2]==unique_labels[i]]
		sub.scatter(temp_df[:,0], temp_df[:,1], c=colors[i%len(colors)])

	sub.set_xlabel('Dimension1')
	sub.set_ylabel('Dimension2')
	sub.set_title(file.split('.')[0])
	fig.savefig("PA3_"+file.split('.')[0]+".png")