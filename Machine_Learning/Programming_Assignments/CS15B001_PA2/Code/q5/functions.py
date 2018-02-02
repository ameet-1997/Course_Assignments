"""
Auxillary functions to be used for Q3

Author: Ameet Deshpande
RollNo: CS15B001
"""

import os
from os import walk


def get_min_num_obj():
	current_directory = os.getcwd()
	all_files = []
	for (dirpath, dirnames, filenames) in walk(current_directory+"/logfiles_minnumobj"):
		all_files.extend(filenames)

	min_values = []
	number_of_leaves = []

	for filename in all_files:
		min_values.append(float(filename.strip().split('.')[0]))
		f = open("logfiles_minnumobj/"+filename, "r")
		lines = f.readlines()
		for line in lines:
			temp = line.strip().split()
			try:
				if temp[0] == "Number":
					number_of_leaves.append(float(temp[-1]))
					break
			except:
				pass

	min_values, number_of_leaves = zip(*sorted(zip(min_values, number_of_leaves)))
	min_values = list(min_values)
	number_of_leaves = list(number_of_leaves)
	return [min_values, number_of_leaves]


def get_min_num_obj_accuracy():
	current_directory = os.getcwd()
	all_files = []
	for (dirpath, dirnames, filenames) in walk(current_directory+"/logfiles_minnumobj"):
		all_files.extend(filenames)

	min_values = []
	fscores = []

	for filename in all_files:
		min_values.append(float(filename.strip().split('.')[0]))
		f = open("logfiles_minnumobj/"+filename, "r")
		lines = f.readlines()
		for line in lines:
			temp = line.strip().split()
			try:
				if temp[0] == "Weighted":
					fscores.append(float(temp[6]))
			except:
				pass

	# Choose only the odd indices for test fscore
	fscores = fscores[1::2]
	min_values, fscores = zip(*sorted(zip(min_values, fscores)))
	min_values = list(min_values)
	fscores = list(fscores)
	return [min_values, fscores]