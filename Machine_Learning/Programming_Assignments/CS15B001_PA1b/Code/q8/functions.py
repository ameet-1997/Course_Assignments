import numpy as np

class nnmodel1:
	W1 = None 	# For the hidden layer
	W2 = None 	# For the output layer
	W1dash = None
	W2dash = None
	b1 = None 	# Bias for hidden layer
	b2 = None 	# Bias for output layer
	b1dash = None
	b2dash = None
	for_bias = None 	# Used for multiplication with bias
	s1 = None 	# Input to layer 1
	s2 = None 	# Input to layer 2
	s0 = None 	# Input data
	z1 = None 	# Output of first layer
	z2 = None 	# Output of final layer
	# Derivatives
	s1dash = None
	s2dash = None
	z1dash = None
	target = None 		# Target for input data
	training_examples = None 	# The number of training examples
	current_loss = None 		# The loss after each step
	learning_rate = None
	one_hot = None

	def __init__(self,d1,d2,d3,data,target,learning_rate):
		# Create empty matrices with the correct dimensions
		# Initialize with values between [-0.05,0.05]
		self.W1 = (np.random.rand(d1,d2)-0.5)/10
		self.W2 = (np.random.rand(d2,d3)-0.5)/10
		self.W1dash = (np.random.rand(d1,d2)-0.5)/10
		self.W2dash = (np.random.rand(d2,d3)-0.5)/10
		self.b1 = np.matrix(np.random.rand(d2)-0.5)
		self.b2 = np.matrix(np.random.rand(d3)-0.5)
		# Not initializing b1dash and b2dash
		self.training_examples = data.shape[0]
		self.for_bias = np.ones((1,self.training_examples), dtype=float)
		self.s1 = np.random.rand(self.training_examples, d2) 	# n X d2
		self.s1dash = np.random.rand(self.training_examples, d2) 	# n X d2
		self.s2 = np.random.rand(self.training_examples, d3) 	# n X d3
		self.s2dash = np.random.rand(self.training_examples, d3) 	# n X d3
		self.s0 = data 											# n X d1
		self.z1 = np.random.rand(self.training_examples, d2) 	# n X d2
		self.z1dash = np.random.rand(self.training_examples, d2) 	# n X d2
		self.z2 = np.random.rand(self.training_examples, d3) 	# n X d3
		self.target = target
		self.learning_rate = learning_rate

	# Does a forward propagation and calculates the final output
	def forward_propagation(self):
		# print("Shapes are::"+str(self.s0.shape)+str("::")+str(self.W1.shape)+str("::")+str(self.s1.shape)+str("::"))
		self.s1 = np.matmul(self.s0, self.W1) 	# s0 X W1 = s1  -  n X d2
		self.s1 = np.add(self.s1, self.b1) 			# Add the bias term to all rows
		self.z1 = np.tanh(self.s1) 				# z1 = tanh(s1)  -  Take tanh function
		self.s2 = np.matmul(self.z1, self.W2) 	# z1 X W2 = s2
		self.s2 = np.add(self.s2, self.b2) 			# Bias term
		self.z2 = np.exp(self.s2) 				# z2 = e^(s2)
		temp_sum = np.sum(self.z2, axis=1) 			# Calculate columnwise sum n X 1
		for i in range(self.training_examples):
			self.z2[i,:] = np.divide(self.z2[i,:], temp_sum[i]) 	# Softmax function

	# Calculates the cross entropy loss using the calculated parameters
	def cross_entropy(self):
		self.current_loss = 0
		for i in range(self.training_examples):
			# self.current_loss -= np.dot(self.target[i], np.log(self.z2[i]))
			self.current_loss -= np.sum(np.multiply(self.target[i], np.log(self.z2[i])))

	# Backpropagation algorithm using cross entropy function
	def backprop(self):
		# Derivatives with output layer activations
		self.s2dash = -(self.target - self.z2)
		# Derivatives wrt output of hidden layer
		self.z1dash = np.matmul(self.s2dash, np.transpose(self.W2))
		# Derivatives with respect to W2
		self.W2dash = np.matmul(np.transpose(self.z1), self.s2dash)
		# Derivatives wrt bias
		self.b2dash = np.matmul(self.for_bias, self.s2dash)
		# Derivatives wrt s1
		self.s1dash = np.multiply(self.z1dash, (1 - np.multiply(self.z1, self.z1)))
		# Derivates with respect to W1
		self.W1dash = np.matmul(np.transpose(self.s0), self.s1dash)
		# Derivatives wrt bias term
		self.b1dash = np.matmul(self.for_bias, self.s1dash)

	def train_model(self, iteration):
		for i in range(iteration):
			self.forward_propagation()
			self.backprop()
			self.W1 = self.W1 - self.learning_rate*self.W1dash
			self.W2 = self.W2 - self.learning_rate*self.W2dash
			self.b1 = self.b1 - self.learning_rate*self.b1dash
			self.b2 = self.b2 - self.learning_rate*self.b2dash
			# self.cross_entropy()
			# if i%100 == 0:
			# 	print("The cross entropy loss is: "+str(self.current_loss))

	def one_hot_encoding(self, z2, training_examples):
		self.one_hot = np.copy(z2)
		for i in range(training_examples):
			self.one_hot[i][self.one_hot[i] < np.amax(self.one_hot[i])] = 0
			self.one_hot[i][self.one_hot[i] > 0] = 1

	# Function used for getting the target values
	# Forward propagate and then one-hot-encode
	def predict_values(self, data):
		s0 = data
		training_examples = data.shape[0]
		s1 = np.matmul(s0, self.W1) 	# s0 X W1 = s1  -  n X d2
		s1 = np.add(s1, self.b1) 			# Add the bias term to all rows
		z1 = np.tanh(s1) 				# z1 = tanh(s1)  -  Take tanh function
		s2 = np.matmul(z1, self.W2) 	# z1 X W2 = s2
		s2 = np.add(s2, self.b2) 			# Bias term
		z2 = np.exp(s2) 				# z2 = e^(s2)
		temp_sum = np.sum(z2, axis=1) 			# Calculate columnwise sum n X 1
		for i in range(training_examples):
			z2[i,:] = np.divide(z2[i,:], temp_sum[i]) 	# Softmax function
		self.one_hot_encoding(z2, training_examples)
		return self.one_hot

	def weight_square(self):
		return [np.sum(np.multiply(self.W1, self.W1)), np.sum(np.multiply(self.W2, self.W2))]




class nnmodel2:
	W1 = None 	# For the hidden layer
	W2 = None 	# For the output layer
	W1dash = None
	W2dash = None
	b1 = None 	# Bias for hidden layer
	b2 = None 	# Bias for output layer
	b1dash = None
	b2dash = None
	for_bias = None 	# Used for multiplication with bias
	s1 = None 	# Input to layer 1
	s2 = None 	# Input to layer 2
	s0 = None 	# Input data
	z1 = None 	# Output of first layer
	z2 = None 	# Output of final layer
	# Derivatives
	s1dash = None
	s2dash = None
	z1dash = None
	target = None 		# Target for input data
	training_examples = None 	# The number of training examples
	current_loss = None 		# The loss after each step
	learning_rate = None
	regularization = None
	one_hot = None

	def __init__(self,d1,d2,d3,data,target,learning_rate,reg):
		# Create empty matrices with the correct dimensions
		# Initialize with values between [-0.05,0.05]
		self.W1 = (np.random.rand(d1,d2)-0.5)/100
		self.W2 = (np.random.rand(d2,d3)-0.5)/100
		self.W1dash = (np.random.rand(d1,d2)-0.5)/100
		self.W2dash = (np.random.rand(d2,d3)-0.5)/100
		self.b1 = np.matrix(np.random.rand(d2)-0.5)/10
		self.b2 = np.matrix(np.random.rand(d3)-0.5)/10
		# Not initializing b1dash and b2dash
		self.training_examples = data.shape[0]
		self.for_bias = np.ones((1,self.training_examples), dtype=float)
		self.s1 = np.random.rand(self.training_examples, d2) 	# n X d2
		self.s1dash = np.random.rand(self.training_examples, d2) 	# n X d2
		self.s2 = np.random.rand(self.training_examples, d3) 	# n X d3
		self.s2dash = np.random.rand(self.training_examples, d3) 	# n X d3
		self.s0 = data 											# n X d1
		self.z1 = np.random.rand(self.training_examples, d2) 	# n X d2
		self.z1dash = np.random.rand(self.training_examples, d2) 	# n X d2
		self.z2 = np.random.rand(self.training_examples, d3) 	# n X d3
		self.target = target
		self.learning_rate = learning_rate
		self.regularization = reg

	# Does a forward propagation and calculates the final output
	def forward_propagation(self):
		# print("Shapes are::"+str(self.s0.shape)+str("::")+str(self.W1.shape)+str("::")+str(self.s1.shape)+str("::"))
		self.s1 = np.matmul(self.s0, self.W1) 	# s0 X W1 = s1  -  n X d2
		self.s1 = np.add(self.s1, self.b1) 			# Add the bias term to all rows
		self.z1 = np.tanh(self.s1) 				# z1 = tanh(s1)  -  Take tanh function
		self.s2 = np.matmul(self.z1, self.W2) 	# z1 X W2 = s2
		self.s2 = np.add(self.s2, self.b2) 			# Bias term
		# print("The maximum element is: "+str(np.amax(self.s2)))
		self.z2 = np.exp(self.s2 - np.amax(self.s2)) 				# z2 = e^(s2)
		temp_sum = np.sum(self.z2, axis=1) 			# Calculate columnwise sum n X 1
		for i in range(self.training_examples):
			self.z2[i,:] = np.divide(self.z2[i,:], temp_sum[i]) 	# Softmax function

	# Calculates the cross entropy loss using the calculated parameters
	def regularization_loss(self):
		self.current_loss = 0
		temp_matrix = (self.target - self.z2)
		self.current_loss += np.sum(np.multiply(temp_matrix, temp_matrix))/2
		self.current_loss += self.regularization*np.sum(np.multiply(self.W1, self.W1))
		self.current_loss += self.regularization*np.sum(np.multiply(self.W2, self.W2))

	# Backpropagation algorithm using cross entropy function
	def backprop(self):
		# Derivatives with output layer activations
		self.s2dash = np.multiply(self.z2, np.sum(np.multiply((self.target - self.z2), self.z2), axis=1) + (self.z2 - self.target))
		# Derivatives wrt output of hidden layer
		self.z1dash = np.matmul(self.s2dash, np.transpose(self.W2))
		# Derivatives with respect to W2
		self.W2dash = np.matmul(np.transpose(self.z1), self.s2dash) + 2*self.regularization*self.W2
		# Derivatives wrt bias
		self.b2dash = np.matmul(self.for_bias, self.s2dash)
		# Derivatives wrt s1
		self.s1dash = np.multiply(self.z1dash, (1 - np.multiply(self.z1, self.z1)))
		# Derivates with respect to W1
		self.W1dash = np.matmul(np.transpose(self.s0), self.s1dash) + 2*self.regularization*self.W1
		# Derivatives wrt bias term
		self.b1dash = np.matmul(self.for_bias, self.s1dash)

	def train_model(self, iteration):
		for i in range(iteration):
			self.forward_propagation()
			self.backprop()
			self.W1 = self.W1 - self.learning_rate*self.W1dash
			self.W2 = self.W2 - self.learning_rate*self.W2dash
			self.b1 = self.b1 - self.learning_rate*self.b1dash
			self.b2 = self.b2 - self.learning_rate*self.b2dash
			# self.regularization_loss()
			# if i%100 == 0:
			# 	print("The regularization loss is: "+str(self.current_loss))
		# print(self.W2)


	def one_hot_encoding(self, z2, training_examples):
		self.one_hot = np.copy(z2)
		for i in range(training_examples):
			self.one_hot[i][self.one_hot[i] < np.amax(self.one_hot[i])] = 0
			self.one_hot[i][self.one_hot[i] > 0] = 1

	# Function used for getting the target values
	# Forward propagate and then one-hot-encode
	def predict_values(self, data):
		s0 = data
		training_examples = data.shape[0]
		s1 = np.matmul(s0, self.W1) 	# s0 X W1 = s1  -  n X d2
		s1 = np.add(s1, self.b1) 			# Add the bias term to all rows
		z1 = np.tanh(s1) 				# z1 = tanh(s1)  -  Take tanh function
		s2 = np.matmul(z1, self.W2) 	# z1 X W2 = s2
		s2 = np.add(s2, self.b2) 			# Bias term
		z2 = np.exp(s2) 				# z2 = e^(s2)
		temp_sum = np.sum(z2, axis=1) 			# Calculate columnwise sum n X 1
		for i in range(training_examples):
			z2[i,:] = np.divide(z2[i,:], temp_sum[i]) 	# Softmax function
		self.one_hot_encoding(z2, training_examples)
		return self.one_hot

	def weight_square(self):
		return [np.sum(np.multiply(self.W1, self.W1)), np.sum(np.multiply(self.W2, self.W2))]