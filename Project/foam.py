"""
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose:
Foam 
	Variables
		Type: Str (Lithium or Boron)
		Name: Str
		Max_Diameter: Float
		Strut: Path Element
		Pore: Path Element
		Layer: Path Element
	Methods
		li impregnated foam
		5_PPI
		10_PPI
		20_PPI
		45_PPI
		80_PPI
	
Path Element
	Variables
		Name: Str
		Avg: Float
		SD: Float
		Material: Material
	Methods
		New Path Element
		New Path Element thickness

Material
	Variables
		Name: Str
		Ionization: List
		MFP: Float
	Methods
		li_foam
		lithium_argon
		boron_argon
		carbon
		enriched_b4c
		natural_b4c
		get mfp
		set ionization table length
		get lead-in x
		get residual energy
"""
import numpy as np

class foam:
    '''
    Class Definition
    '''
    def __init__(self):
        '''
		Initializes the foam to a Lithium impregnated foam with observed strut and pore dimensions
        '''
        self.li_imp(0.275)
		self.diameter = 5.08E4
		
	def li_imp(self, percent):
		'''
		Creates a foam with the observed parameters for the lithium impregnated foam sample
		'''
        self.type = "lithium"
		self.name = "observed Li impregnated"
		self.strut = path_element.new('Li foam strut', 40.0, 10.0, material.li_foam(percent))
		self.pore = path_element.new('argon pore', 500.0, 100.0, material.lithium_argon())
		self.layer = None
		
    def 5_ppi(self):
		'''
		Creates a foam with the observed parameters for 5 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "5 ppi RVC"
		self.strut = path_element.new('carbon strut', 418.33, 117.21, material.carbon())
		self.pore = path_element.new('argon pore', 4850.0, 810.0, material.boron_argon())
		self.layer = path_element.new('boron carbide layer', 10.25, 2.57, material.enriched_b4c())
    
	def 10_ppi(self):
		'''
		Creates a foam with the observed parameters for 10 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "10 ppi RVC"
		self.strut = path_element.new('carbon strut', 349.06, 83.21, material.carbon())
		self.pore = path_element.new('argon pore', 4000.0, 540.0, material.boron_argon())
		self.layer = path_element.new('boron carbide layer', 9.33, 1.34, material.enriched_b4c())   
	
	def 20_ppi(self):
		'''
		Creates a foam with the observed parameters for 20 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "20 ppi RVC"
		self.strut = path_element.new('carbon strut', 285.27, 72.48, material.carbon())
		self.pore = path_element.new('argon pore', 3260.0, 460.0, material.boron_argon())
		self.layer = path_element.new('boron carbide layer',9.97, 1.20, material.enriched_b4c())
		
	def 45_ppi(self):
		'''
		Creates a foam with the observed parameters for 45 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "45 ppi RVC"
		self.strut = path_element.new('carbon strut', 120.48, 39.89, material.carbon())
		self.pore = path_element.new('argon pore', 1470.0, 150.0, material.boron_argon())
		self.layer = path_element.new('boron carbide layer', 6.85, 1.17, material.enriched_b4c())
		
	def 80_ppi(self):
		'''
		Creates a foam with the observed parameters for 80 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "80 ppi RVC"
		self.strut = path_element.new('carbon strut', 50.45, 11.06, material.carbon())
		self.pore = path_element.new('argon pore', 630.0, 120.0, material.boron_argon())
		self.layer = path_element.new('boron carbide layer', 7.17, 3.20, material.enriched_b4c())
		
class path_element
	'''
	Path elements are the constituents that make up a foam (struts, pores, and layers).
	Each element will have a name, average value, standard deviation, and material assigned to it.
	The only method of a path element is to create new element dimensions for the particles to 
	pass through.
	'''
	def __init__(self):
		'''
		Initializes the path element as a lithium impregnated strut
		'''
		self.new('Li foam strut', 40.0, 10.0, material.li_foam(0.275))
		
	def new(self, name, avg, sd, mat):
		'''
		Creates a new path element with the input parameters 
		'''
		self.name = str(name)
		self.avg = float(avg)
		self.sd = float(sd)
		self.mat = mat
		
	def new_thickness(self, random):
		'''
		Generates a thickness for the path element using a uniform distribution centered about an 
		average value and ranging +/- 1 S.D.
		'''
		if self.type == 'boron':
			
		else:
			
		return thickness

from bisect import bisect, bisect_right, bisect_left
		
class material
	'''
	Every path element will have a material.
	Materials contain ionization and residual energy lists as well as the neutron 
	mean free path (mfp)
	for the material.
	'''
	def __init__(self):
		'''
		Initializes a new path element as a 27.5% saturated lithiated foam strut
		'''
		self.li_foam(0.275)
		
	def li_foam(self, percent_lif):
		'''
		Creates the lithiated foam material for struts in the lithiated foams.
		Reads in ionization and residual energy tables from ./data
		Determines the mean free path of a neutron in the foam.
		Requires the foam saturation to be provided
		'''
		self.name = 'lithiated foam'
		self.alpha_ionization = np.loadtxt('./data/lithium_alpha_strut.csv')
		self.ion_ionization = np.loadtxt('./data/lithium_triton_strut.csv')
		#Calculate the mean free path of a thermal neutron in the lithiated foam
		strut_density = 1.2
		foam_atomic_mass = 18.9934032
		lithium_atomic_mass = 6.941
		lithiated_foam_atomic_mass = (lithium_atomic_mass*0.5 + foam_atomic_mass*0.5)/2.0
		percent_li = percent_lif*lithium_atomic_mass*lithiated_foam_atomic_mass
		li_micro_cs = 940E-24
		li_macro_cs = percent_li*6.022E23*li_micro_cs/lithium_atomic_mass
		self.mfp = 1/(strut_density*li_macro_cs)
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def lithium_argon(self):
		'''
		Creates the argon material for pores in lithiated foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'argon'
		self.alpha_ionization = np.loadtxt('./data/lithium_alpha_argon.csv')
		self.ion_ionization = np.loadtxt('./data/lithium_triton_argon.csv')
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def boron_argon(self):
		'''
		Creates the argon material for pores in b4c coated foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'argon'
		self.alpha_ionization = np.loadtxt('./data/boron_alpha_argon.csv')
		self.ion_ionization = np.loadtxt('./data/boron_ion_argon.csv')
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def carbon(self):
		'''
		Creates the carbon material for struts in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'carbon'
		self.alpha_ionization = np.loadtxt('./data/boron_alpha_carbon.csv')
		self.ion_ionization = np.loadtxt('./data/boron_ion_carbon.csv') 
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def enriched_b4c(self):
		'''
		Creates the enriched boron carbide material for layers in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Determines the mean free path of a neutron in the foam.
		'''
		self.name = 'B4C'
		self.alpha_ionization = np.loadtxt('./data/boron_alpha_b4c.csv')
		self.ion_ionization = np.loadtxt('./data/boron_ion_b4c.csv')
		#Calculate the mean free path of a thermal neutron in the enriched b4c	
		b4c_density = 2.52
		percent_boron = 0.7826
		boron_enrichment = 1
		b4c_atomic_mass = 52.0107
		boron_micro_cs = 3842E-24
		self.mfp = 1/b4c_density*percent_boron*boron_enrichment*6.022E23*boron_micro_cs/b4c_atomic_mass
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def natural_b4c(self):
		'''
		Creates the natural boron carbide material for layers in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Determines the mean free path of a neutron in the foam.
		'''
		self.name = 'B4C'
		self.alpha_ionization = np.loadtxt('./data/boron_alpha_b4c.csv')
		self.ion_ionization = np.loadtxt('./data/boron_ion_b4c.csv') 
		#Calculate the mean free path of a thermal neutron in the natural b4c		
		b4c_density = 2.52
		percent_boron = 0.7826
		boron_enrichment = 0.199
		b4c_atomic_mass = 55.255
		boron_micro_cs = 3842E-24
		self.mfp = 1/b4c_density*percent_boron*boron_enrichment*6.022E23*boron_micro_cs/b4c_atomic_mass
		#Set the length of the ionization tables
		self.set_ionization_table_length
		
	def get_mfp(self):
		'''
		Returns the mean free path for the material
		'''
		return self.mfp
		
	def set_ionization_table_length(self):
		'''
		'''
		self.alpha_ionization_length = len(alpha_ionization)
		self.ion_ionization_length = len(ion_ionization)
		
	def get_x(self, energy, reaction_product):
		'''
		Determines the lead-in distance required for the reaction product to have a given energy.
		Searches through the ionization table for the 2 energies bounding the input energy and
		linearly interpolates the lead-in distance (x) between those points
		'''
		if reaction_product == 'alpha':
			length = self.alpha_ionization_length
			index = bisect_left(self.alpha_ionization[:,1], energy)
			if index >= length:
				left_index, right_index = -1, None
			elif energy == self.alpha_ionization[index,1]:
				left_index right_index = index, index
			elif index == 0:
				left_index, right_index = none, 0
			else:
				left_index, right_index = index - 1, index
			
			left_energy = self.alpha_ionization[left_index, 1]
			right_energy = self.alpha_ionization[right_index, 1]
			left_x = self.alpha_ionization[left_index, 0]
			right_x = self.alpha_ionization[right_index, 0]
			x = (right_energy - energy)/(right_energy - left_energy)*(right_x - left_x) + left_x
		else:
			length = self.ion_ionization_length
			index = bisect_left(self.ion_ionization[:,1], energy)
			if index >= length:
				left_index, right_index = -1, None
			elif energy == self.ion_ionization[index,1]:
				left_index right_index = index, index
			elif index == 0:
				left_index, right_index = none, 0
			else:
				left_index, right_index = index - 1, index
			
			left_energy = self.ion_ionization[left_index, 1]
			right_energy = self.ion_ionization[right_index, 1]
			left_x = self.ion_ionization[left_index, 0]
			right_x = self.ion_ionization[right_index, 0]
			x = (right_energy - energy)/(right_energy - left_energy)*(right_x - left_x) + left_x
		
		return x
		
	def get_res_energy(self, x, reaction_product):
		'''
		Determines the residual energy of the reaction product after traversing a distance (x) into
		the material.
		'''
		if reaction_product == 'alpha':
			length = self.alpha_ionization_length
			index = bisect_left(self.alpha_ionization[:,0], x)
			if index >= length:
				left_index, right_index = -1, None
			elif energy == self.alpha_ionization[index,0]:
				left_index right_index = index, index
			elif index == 0:
				left_index, right_index = none, 0
			else:
				left_index, right_index = index - 1, index
			
			left_energy = self.alpha_ionization[left_index, 1]
			right_energy = self.alpha_ionization[right_index, 1]
			left_x = self.alpha_ionization[left_index, 0]
			right_x = self.alpha_ionization[right_index, 0]
			res_energy = (right_x - x)/(right_x - left_x)*(right_energy - left_energy) + left_energy
		else:
			length = self.ion_ionization_length
			index = bisect_left(self.ion_ionization[:,0], x)
			if index >= length:
				left_index, right_index = -1, None
			elif energy == self.ion_ionization[index,0]:
				left_index right_index = index, index
			elif index == 0:
				left_index, right_index = none, 0
			else:
				left_index, right_index = index - 1, index
			
			left_energy = self.ion_ionization[left_index, 1]
			right_energy = self.ion_ionization[right_index, 1]
			left_x = self.ion_ionization[left_index, 0]
			right_x = self.ion_ionization[right_index, 0]
			res_energy = (right_x - x)/(right_x - left_x)*(right_energy - left_energy) + left_energy
		return res_energy