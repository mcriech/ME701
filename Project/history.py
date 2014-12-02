"""
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 
History
	Variables
		RN Vector: List
		RN iterator: Int
		Neutron
		Device Diameter : Float
		Ionization: Float
	Methods
		Set foam parameters for neutron
		Get a random number from the random number vector
		Transport Neutron
		Get the first path length for reaction products
		Transport Reaction Products
		Send Result 
"""

from foam.py import *
import numpy as np

class history:
    def __init__(self, random_vector):
        '''
        Initialize a new history
        '''
		self.rn = 0
		self.random_vector = random_vector
		self.neutron = neutron()
		self.device_diam = 0.0
		self.ionization = 0.0
		self.foam = foam()
		
	def set_foam(self, foam):
		self.foam = foam
		self.neutron.foam = foam
		
	def random(self):
		'''
		Returns the the next random number from the random number vector and then adds 1 to the
		random number counter
		'''
		random = self.random_vector(self.rn)
		self.rn += 1
		return random
		
	def transport_neutron(self):
		'''
		All neutron paths begin with a pore
		'''
		while self.neutron.interaction == False & self.neutron.location < self.device_diam:
			#Generate a new path element
			#First determine if there are 2 or 3 path elements
			if self.foam.type == "lithium":
				#Determine which path element to make
				if self.neutron.path_index % 2 == 1:
					path_element = 'strut'
					thickness = self.foam.strut.new_thickness(self.random())
				else:
					#Pore
					path_element = 'pore'
					thickness = self.foam.pore.new_thickness(self.random())					
			else:
				#Determine which path element to make
				if self.neutron.path_index % 4 == 2:
					#Strut
					path_element = 'strut'
					thickness = self.foam.strut.new_thickness(self.random())
				if self.neutron.path_index % 4 == 1 | 3:
					#Layer
					path_element = 'layer'
					thickness = self.foam.layer.new_thickness(self.random())
				else:
					#Pore
					path_element = 'pore'
					thickness = self.foam.pore.new_thickness(self.random())
			#Determine where the neutron hits the element
			#Some distance between the center and the outer edge of the path element
			position = self.random()
			if path_element == 'strut':
				if self.foam.type == 'lithium':
					#Lithiated strut
					#Find the chord through the strut
					#interaction_y is the perpendicular distance to the intersection point (radius * random)
					position = self.random()
					interaction_y = thickness/2*position
					#Find chord length given perpendicular distance
					path_length = 2*np.sqrt((thickness/2)**2 - interaction_y**2)
					#Adjust path length for strut tilt (theta)
					omega = self.random()
					path_length = path_length/omega
					strut_length = self.foam.pore.new_thickness(self.random())
					#If the particle is travelling through the top of the strut, the path length
					#needs to be relative to the strut length rather than the diameter
					if path_length > strut_length:
						path_length = strut_length/(1 - omega)
				else:
					#Carbon Strut
					pass
			elif path_element == 'layer':
				#B4C layer on a carbon strut
				pass
			else:
				#Pore
				#Find the horizontal chord through the pore
				#interaction_y is the perpendicular distance to the intersection point (radius * random)
				position = self.random()
				interaction_y = thickness/2*position
				#Find chord length given perpendicular distance
				path_length = 2*np.sqrt((thickness/2)**2 - interaction_y**2)
				#Adjust path length for the vertical position hitting the pore
				#Basically doing the same thing, but with a smaller circle
				position = self.random()
				interaction_y = path_length/2*position
				path_length = 2*np.sqrt((path_length/2)**2 - interaction_y**2)
			#Add the new path element to the neutron path
			self.neutron.path.append((path_length, path_element))
			self.neutron.location += path_length
			#Test for a neutron interaction
			interaction_x = self.neutron.interaction_test(self.random())			
			#Increase the neutron path index by 1
			self.neutron.path_index += 1
		if self.neutron.interaction == True:
			self.reaction_products_first_path_length(interaction_x, interaction_y, thickness, strut_length)
			self.ionization = self.transport_reaction_products()
		else:
			pass
		return self.neutron.interaction
			
	def reaction_products_first_path_length(self, x, y, thickness, length):
		'''
		'''
		for particle in (self.neutron.alpha, self.neutron.ion):
			if self.neutron.foam.type == 'lithium':
				path_element = 'strut'
				#Interaction took place in a lithiated strut
				#Thickness is the diameter of the strut
				#Strut_length is the height of the strut
				x0 = interaction_x
				y0 = interaction_y
				z0 = 0.0
				#alpha, beta, and gamma are direction cosines for the emission angle (0 to 1)
				alpha = self.random()
				beta = self.random()
				gamma = self.random()
				#See how long the ray is to the edge of the cylinder
				a = alpha**2 + beta**2
				b = 2*(x0*alpha + y0*beta)
				c = x0**2 + y0**2 - thickness
				path_length = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
				if path_length < 0:
					path_length = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
				if (z0 + gamma*path_length) > length:
					path_length = (length - z0)/gamma
				#Add the path length to the particle path
				particle.path.append((path_length, path_element))
			else:
				#Interaction took place in a b4c layer
				pass
			#Find the ionization in the first path length
			#Find the lead-in x
			lead_in_x = 0
			#Find the res energy
			res_energy = particle.retrieve_res_energy(path_length)
			particle.energy = res_energy
		
	def transport_reaction_products(self):
		'''
		'''
		history_ionization = 0.0
		for particle in (self.neutron.alpha, self.neutron.ion):
			particle.path_index = 0
			while particle.energy > 0:
				if self.foam.type == "lithium":
					#Determine which path element to make
					if self.neutron.path_index % 2 == 0:
						path_element = 'strut'
						thickness = self.foam.strut.new_thickness(self.random())
						#Find the chord through the strut
						#d is the perpendicular distance to the intersection point (radius * random)
						position = self.random()
						d = thickness/2*position
						#Find chord length given perpendicular distance
						path_length = 2*np.sqrt((thickness/2)**2 - d**2)
						#Adjust path length for strut tilt (theta)
						omega = self.random()
						path_length = path_length/omega
						strut_length = self.foam.pore.new_thickness(self.random())
						#If the particle is travelling through the top of the strut, the path length
						#needs to be relative to the strut length rather than the diameter
						if path_length > strut_length:
							path_length = strut_length/(1 - omega)
					else:
						#Pore
						path_element = 'pore'
						thickness = self.foam.pore.new_thickness(self.random())
						#Find the horizontal chord through the pore
						#d is the perpendicular distance to the intersection point (radius * random)
						position = self.random()
						d = thickness/2*position
						#Find chord length given perpendicular distance
						path_length = 2*np.sqrt((thickness/2)**2 - d**2)
						#Adjust path length for the vertical position hitting the pore
						#Basically doing the same thing, but with a smaller circle
						position = self.random()
						d = path_length/2*position
						path_length = 2*np.sqrt((path_length/2)**2 - d**2)
				else:
					#Determine which path element to make
					if self.neutron.path_index % 4 == 1:
						#Strut
						path_element = 'strut'
						thickness = self.foam.strut.new_thickness(self.random())
					if self.neutron.path_index % 4 == 0 | 2
						#Layer
						path_element = 'layer'
						thickness = self.foam.layer.new_thickness(self.random())
					else:
						#Pore
						path_element = 'pore'
						thickness = self.foam.pore.new_thickness(self.random())
				#Add the path length to the particle path
				particle.path.append((path_length, path_element))
				#Find the energy lost through the path element
				#Find the lead-in x
				lead_in_x = particle.retrieve_x()
				#Find the res energy
				dx = lead_in_x + path_length
				res_energy = particle.retrieve_res_energy(dx)
				#Add ionization if in a pore
				if path_element == 'pore':
					ionization = particle.energy - res_energy
					particle.add_ionization(ionization)
				particle.energy = res_energy
			ionization += particle.report_ionization()
			return ionization			