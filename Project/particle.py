"""
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 
Particle
	Variables
		Name: Str
		Path: List
		Path Index: Int
		Foam: Foam
	Methods
		Get Current Material

Neutron
	Variables
		Location: Float
	Methods
		Interaction Test
		Generate Reaction Products
		Escaped

Reaction Product
	Variables
		Energy: Float
		Name: Str
		Omega: Float
		Phi: Float
	Methods
		Calculate First Path Length
		Get lead-in x
		Get residual energy
		Add Ionization
		Report Ionization		
"""
from __future__ import division
from foam import *
import numpy as np

class particle(object):
	def __init__(self, foam):
		'''
		The path is composed of tuples (path_length, 'element') where the path_length is the actual
		particle path length of travel, and the element is either strut, pore, or layer for that 
		path length.
		'''
		self.name = None
		self.path = []
		self.path_index = 0
		self.foam = foam

	def set_foam(self, foam):
		'''
		'''
		self.foam = foam
		
	def get_material(self):
		element = self.path[self.path_index][1]
		if element == 'strut':
			material = self.foam.strut
		elif element == 'pore':
			material = self.foam.pore
		else:
			material = self.foam.layer
		return material
		
class neutron(particle):
	def __init__(self, foam):
		'''
		Neutron is a daughter of particle, and will be initialized in lithium impregnated foam
		'''
		super(particle, self).__init__()
		self.name = 'neutron'
		self.location = 0.0
		self.interaction = False
		self.foam = foam
		self.path = []
		self.path_index = 0
		
	def interaction_test(self, random):
		'''
		Determines if a neutron interaction occurs.
		Checks that the neutron is in a (Strut for lithium foams, layer for boron foams)
		and then determines an interaction distance from an exponential distribution using the
		inverse CDF method. If the interaction distance is less than the current path length, the
		interaction variable is changed to True.
		'''
		path_element = self.path[self.path_index]
		#Only need to check for an interaction if the neutron is a an absorbing material
		#Struts for the lithiated foams
		interaction_distance = 0.0
		if path_element[1] == "strut" and self.foam.type == "lithium":
			material = self.get_material()
			mfp = self.foam.strut.mat.get_mfp()
			interaction_distance = -mfp*np.log(random)
			#print mfp, interaction_distance
			if interaction_distance <= path_element[0]:
				self.interaction = True
				(self.alpha, self.ion) = self.create_reaction_products()
		#Layers for the RVC foams		
		if path_element[1] == "layer" and self.foam.type == "boron":
			material = self.get_material()
			mfp = self.foam.layer.mat.get_mfp()
			interaction_distance = -mfp*np.log(random)
			if interaction_distance <= path_element[0]:
				self.interaction = True
				(self.alpha, self.ion) = self.create_reaction_products()
		return interaction_distance
			
	def create_reaction_products(self):
		'''
		Generates 2 reaction products after a neutron interaction occurs.
		Sets the omega and phi for both reaction products
		'''
		#Need to pass the foam into the reaction products
		alpha = reaction_product(self.foam)
		ion = reaction_product(self.foam)
		if self.foam.type == "lithium":
			alpha.lithium_alpha()
			ion.lithium_ion()
		else:
			alpha.boron_alpha()
			ion.boron_ion()
		return (alpha, ion)

class reaction_product(particle):
	def __init__(self, foam):
		'''
		'''
		super(particle, self).__init__()
		self.name = None
		self.ionization = 0.0
		self.energy = 0.0
		self.omega = 0.0
		self.phi = 0.0
		self.path = []
		self.path_index = 0
		self.set_foam(foam)
		
	def lithium_alpha(self):
		'''
		'''
		self.energy = 2.0553E6
		self.name = 'alpha'
		
	def lithium_ion(self):
		'''
		'''
		self.energy = 2.7276E6
		self.name = 'ion'
		
	def boron_alpha(self):
		'''
		'''
		self.energy = 1.47E6
		self.name = 'alpha'
		
	def boron_ion(self):
		'''
		'''
		self.energy = 0.840E6
		self.name = 'ion'
		
	def get_omega(self, random):
		'''	
		'''
		omega = random*2 - 1
		return omega
		
	def get_phi(self, random):
		'''
		'''
		phi = random
		return phi
					
	def retrieve_x(self):
		'''
		'''
		element = self.get_material()
		x = element.mat.get_x(self.energy, self)
		return x
		
	def retrieve_res_energy(self, x):
		'''
		'''
		element = self.get_material()
		res_energy = element.mat.get_res_energy(x, self)
		return res_energy
		
	def set_energy(self, energy):
		'''
		'''
		self.energy = energy
		
	def add_ionization(self, added_ionization):
		'''
		'''
		self.ionization += added_ionization
		
	def report_ionization(self):
		'''
		'''
		return self.ionization
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
