import pandas as pd
import numpy as np
from scipy import sparse
import os
import functions

"""
Spam is represented by a 0
Ham is represented by a 1
"""

# Get the vocabulary size, useful for smoothing
[vocab, vocab_size, number_of_documents] = functions.get_vocab_size()
[data_matrix, label_matrix, file_names_return] = functions.get_data()

# Write the matrices to the file
# Note that the order in which the files are read is maintained based on directories
np.savetxt("data.csv", X=data_matrix,delimiter=',')
np.savetxt("labels.csv", X=label_matrix, delimiter=',')
functions.save_sparse_csr("data_sparse", sparse.csr_matrix(data_matrix))
# sparse_mat = functions.load_sparse_csr("data_sparse") 						# Save Sparse matrix as a model