import numpy as np

def madx_out(lat, file):
	"""Reads in the lattice to madx and runs the file in madx. Returns a matrix of info about the trial"""
	
	results = np.zeros((2,2))
	
	return results

class learn(object):
	"""Takes in madx results and begins the process of finding a model to predict them"""
	def __init__(self, results, init):
		self.results = results
		self.init = init
	
	def model(self, init):
		"""The model takes initial condition and predicts results based on the learning"""

		new_results = np.zeros((2,2))
		
		return new_results
