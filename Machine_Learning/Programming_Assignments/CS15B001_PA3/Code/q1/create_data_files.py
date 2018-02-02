import os
import pandas as pd
from pandas import read_csv

# Get a list of all filenames in Data Folder
file_names = os.listdir("../Datasets/1_Clustering-20171102T194854Z-001/1_Clustering/")

for file in file_names:
	df = pd.read_csv("../Datasets/1_Clustering-20171102T194854Z-001/1_Clustering/"+file, header=None, index_col=None, sep='\t')
	new_file_name = "CSV_Files/"+file.split('.')[0]+".csv"
	arff_file_name = "ARFF_Files/"+file.split('.')[0]+".arff"
	df.to_csv(new_file_name, header=["Column1","Column2", "ClassLabel"], index=False)
	os.system("java -cp weka-3-8-1/weka.jar weka.core.converters.CSVLoader "+new_file_name+" >"+arff_file_name+" -B 1000")