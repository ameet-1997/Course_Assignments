from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import pandas as pd
from sklearn.metrics import v_measure_score
import numpy as np
from functions import purity_score_stack
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch

df = pd.read_csv("CSV_Files/D31.csv")
colors = ['b','g','r','c','m','y','k']

# # KMeans algorithm
# clusterer = KMeans(n_clusters=45, n_jobs=-1)
# clusterer.fit(df.iloc[:,0:2], df.iloc[:,2:])
# predicted_labels = clusterer.fit_predict(df.iloc[:,0:2])
# print(v_measure_score(np.array(df.iloc[:,2:]).flatten(), predicted_labels))


# df1 = np.array(df)
# unique_labels = np.unique(predicted_labels)

# # Plot the figure
# fig = plt.figure()
# sub = fig.add_subplot(111)

# # Scatter plot
# for i in range(unique_labels.shape[0]):
# 	temp_df = df1[predicted_labels==unique_labels[i]]
# 	sub.scatter(temp_df[:,0], temp_df[:,1], c=colors[i%len(colors)])

# sub.set_xlabel('Dimension1')
# sub.set_ylabel('Dimension2')
# # fig.savefig("PA3_"+file.split('.')[0]+".png")
# plt.show()


# # DBSCAN Algorithm
# clusterer = DBSCAN(eps=1.3, min_samples=66)
# clusterer.fit(df.iloc[:,0:2], df.iloc[:,2:])
# predicted_labels = clusterer.fit_predict(df.iloc[:,0:2])
# print(v_measure_score(np.array(df.iloc[:,2:]).flatten(), predicted_labels))


# df1 = np.array(df)
# unique_labels = np.unique(predicted_labels)

# # Plot the figure
# fig = plt.figure()
# sub = fig.add_subplot(111)

# # Scatter plot
# for i in range(unique_labels.shape[0]):
# 	temp_df = df1[predicted_labels==unique_labels[i]]
# 	sub.scatter(temp_df[:,0], temp_df[:,1], c=colors[i%len(colors)])

# sub.set_xlabel('Dimension1')
# sub.set_ylabel('Dimension2')
# # fig.savefig("PA3_"+file.split('.')[0]+".png")
# plt.show()


# # Parameter Optimization for DBSCAN
# eps = [float(i+1)/10 for i in range(4, 100)]
# minPts = [2*i for i in range(1,100)]
# max_score = 0
# max_ans = [0,0]

# for e in eps:
# 	for m in minPts:
# 		clusterer = DBSCAN(eps=e, min_samples=m)
# 		clusterer.fit(df.iloc[:,0:2], df.iloc[:,2:])
# 		predicted_labels = clusterer.fit_predict(df.iloc[:,0:2])
# 		if v_measure_score(np.array(df.iloc[:,2:]).flatten(), predicted_labels) > max_score:
# 			max_score = v_measure_score(np.array(df.iloc[:,2:]).flatten(), predicted_labels)
# 			max_ans = [e,m]

# print("Max_Score is: "+str(max_score))
# print(max_ans)


# Hierarchical Clustering
clusterer = AgglomerativeClustering(n_clusters=31, linkage='complete')
clusterer.fit(df.iloc[:,0:2], df.iloc[:,2:])
predicted_labels = clusterer.fit_predict(df.iloc[:,0:2])
print(v_measure_score(np.array(df.iloc[:,2:]).flatten(), predicted_labels))


df1 = np.array(df)
unique_labels = np.unique(predicted_labels)

# Plot the figure
fig = plt.figure()
sub = fig.add_subplot(111)

# Scatter plot
for i in range(unique_labels.shape[0]):
	temp_df = df1[predicted_labels==unique_labels[i]]
	sub.scatter(temp_df[:,0], temp_df[:,1], c=colors[i%len(colors)])

sub.set_xlabel('Dimension1')
sub.set_ylabel('Dimension2')
# fig.savefig("PA3_"+file.split('.')[0]+".png")
plt.show()