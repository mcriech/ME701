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
from __future__ import division
from history import *
from rng import *
from particle import *
from foam import *

class run_manager:
	def __init__(self, foam):
		'''
		'''
		self.foam = foam
		self.lld = 0.0
		self.phs = []
		self.energy_deposition = []
		self.counts = 0
		self.interactions = 0
		self.escapes = 0
		self.histories = 10
		self.random_vector = []
		self.iteration = 0
					
	def set_histories(self, n):
		'''
		'''
		self.histories = n
		
	def set_lld(self, lld):
		'''
		'''
		self.lld = lld
				
	def execute_history(self):
		'''
		'''
		#Initialize the history with a vector of random numbers
		hist = history(self.random_vector[self.iteration], self.foam)
		#Transport a neutron for this history
		interaction = hist.transport_neutron()
		if interaction:
			self.energy_deposition.append(hist.ionization)
			self.interactions += 1
			if hist.ionization >= self.lld:
				self.phs.append(hist.ionization*1E-6)
				self.counts += 1
		else:
			self.escapes += 1
		self.iteration += 1
	
			
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
