"""
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 
Run Manager
	Variables		
		# Nodes: Int
		# Hist: Int
		foam
		RNG		
		LLD: Float
		Ionization Energies: List
		# escapes: Int
		# interaction: Int
		# detected: Int
	Methods
		Compile Results
		Broadcast RNG
		Broadcast Stride 
		Collect Results
		Set Foam Parameters
		Broadcast Foam Parameters
"""

from history.py import *
from rng.py import *
from particle.py import *
from foam.py import *

class manager:
    def __init__(self, foam):
        '''
        '''
		self.foam = foam
		self.lld = 0.0
		self.phs = []
		self.counts = 0
		self.interactions = 0
		self.escapes = 0
		self.histories = 10
		self.random_vector = [[]]
		self.iteration = 0
		pass
					
	def set_histories(self, n)
		'''
		'''
		self.histories = n
		
	def set_lld(self, lld)
		'''
		'''
		self.lld = lld
				
	def execute_history(self):
		'''
		'''
		#Initialize the history with a vector of random numbers
		history = history(self.random_vector(self.iteration))
		#Set the foam for the history
		history.set_foam(foam)
		#Transport a neutron for this history
		interaction = history.transport_neutron()
		if interaction:
			self.energy_deposition.append(history.ionization)
			self.interaction += 1
			if history.ionization >= self.lld:
				self.phs.append(history.ionization)
				self.counts += 1
		else:
			self.escapes += 1
		self.iteration += 1
	
			
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		