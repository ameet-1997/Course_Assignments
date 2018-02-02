import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
import os

def get_data():
	"""Return the data in matrix form
	after going through the files"""
	[number_of_documents, vocab_size] = [1099, 24747]
	dir = "../Datasets/2_NaiveBayes-20171102T194835Z-001/2_NaiveBayes/part"
	data_matrix = np.zeros(shape=(number_of_documents, vocab_size), dtype=float)
	label_matrix = []
	file_names_return = []

	file_number = 0
	for i in range(1,11):
		cur_dir = dir+str(i)+"/"
		file_names = os.listdir(cur_dir)
		for file in file_names:
			file_names_return.append(file)
			f = open(cur_dir+file,'r')
			if "legit" in file:
				label_matrix.append(1)
			else:
				label_matrix.append(0)
			lines = f.readlines()
			lines[0] = " ".join(lines[0].strip().split()[1:]) 	# Remove subject token
			for line in lines:
				temp = line.strip().split() 		# Get all the lines
				for words in temp:
					data_matrix[file_number, (int(words)-1)] += 1
			file_number += 1 						# Next entry

	return [data_matrix, np.array(label_matrix), file_names_return]	# Return the required matrices

def get_vocab_size():
	nod = 0
	dir = "../Datasets/2_NaiveBayes-20171102T194835Z-001/2_NaiveBayes/part"
	vocabulary = {}
	for i in range(1,11):
		cur_dir = dir+str(i)+"/"
		file_names = os.listdir(cur_dir)
		nod = nod + len(file_names)
		for file in file_names:
			f = open(cur_dir+file,'r')
			lines = f.readlines()
			lines[0] = " ".join(lines[0].strip().split()[1:]) 			# Remove subject token
			for line in lines:
				temp = line.strip().split() 							# Get all the lines					
				for words in temp:
					vocabulary[int(words)] = 1

	return [vocabulary, len(vocabulary), nod]							# Return the vocabulary


def save_sparse_csr(filename,array):
    np.savez(filename,data = array.data ,indices=array.indices,
             indptr =array.indptr, shape=array.shape )

def load_sparse_csr(filename):
    loader = np.load(filename+".npz")
    return csr_matrix((  loader['data'], loader['indices'], loader['indptr']),
                         shape = loader['shape'])

def get_alpha0_dirichlet(num_of_words):
	temp = 2*np.ones(shape=num_of_words, dtype=float)
	prior = 5000
	temp[46] = prior
	temp[54] = prior
	temp[58] = prior
	temp[774] = prior
	temp[6175] = prior
	return temp

def get_alpha1_dirichlet(num_of_words):
	temp = 2*np.ones(shape=num_of_words, dtype=float)
	# # prior = 1000
	# temp[126] = prior
	# temp[649] = prior
	# temp[3787] = prior
	# temp[8624] = prior
	return temp	

def get_alpha_beta():
	return [0, 1000000]