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
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.li_imp(0.275)
		self.diameter = 5.08E4
		
	def li_imp(self, percent):
		'''
		Creates a foam with the observed parameters for the lithium impregnated foam sample
		'''
        	self.type = "lithium"
		self.name = "observed Li impregnated"
		self.strut = path_element()
		self.pore = path_element()
		lithium_strut_string = 'self.mat.li_foam(' + str(percent) + ')'
		self.strut.new('Li foam strut', 40.0, 10.0, lithium_strut_string)
		self.pore.new('argon pore', 500.0, 100.0, 'self.mat.lithium_argon()')
		self.layer = None
		
    	def ppi_5(self):
		'''
		Creates a foam with the observed parameters for 5 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "5 ppi RVC"
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.strut.new('carbon strut', 418.33, 117.21, self.mat.carbon())
		self.pore.new('argon pore', 4850.0, 810.0, self.mat.boron_argon())
		self.layer.new('boron carbide layer', 10.25, 2.57, self.mat.enriched_b4c())
    
	def ppi_10(self):
		'''
		Creates a foam with the observed parameters for 10 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "10 ppi RVC"
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.strut.new('carbon strut', 349.06, 83.21, self.mat.carbon())
		self.pore.new('argon pore', 4000.0, 540.0, self.mat.boron_argon())
		self.layer.new('boron carbide layer', 9.33, 1.34, self.mat.enriched_b4c())   
	
	def ppi_20(self):
		'''
		Creates a foam with the observed parameters for 20 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "20 ppi RVC"
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.strut.new('carbon strut', 285.27, 72.48, self.mat.carbon())
		self.pore.new('argon pore', 3260.0, 460.0, self.mat.boron_argon())
		self.layer.new('boron carbide layer',9.97, 1.20, self.mat.enriched_b4c())
		
	def ppi_45(self):
		'''
		Creates a foam with the observed parameters for 45 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "45 ppi RVC"
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.strut.new('carbon strut', 120.48, 39.89, self.mat.carbon())
		self.pore.new('argon pore', 1470.0, 150.0, self.mat.boron_argon())
		self.layer.new('boron carbide layer', 6.85, 1.17, self.mat.enriched_b4c())
		
	def ppi_80(self):
		'''
		Creates a foam with the observed parameters for 80 ppi RVC B4C coated sample
		'''
		self.type = "boron"
		self.name = "80 ppi RVC"
		self.strut = path_element()
		self.pore = path_element()
		self.layer = path_element()
		self.strut.new('carbon strut', 50.45, 11.06, self.mat.carbon())
		self.pore.new('argon pore', 630.0, 120.0, self.mat.boron_argon())
		self.layer.new('boron carbide layer', 7.17, 3.20, self.mat.enriched_b4c())
		
class path_element:
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
		self.mat = material()
		self.new('Li foam strut', 40.0, 10.0, 'self.mat.li_foam(0.275)')
		
	def new(self, name, avg, sd, mat):
		'''
		Creates a new path element with the input parameters 
		'''
		self.name = str(name)
		self.avg = float(avg)
		self.sd = float(sd)
		eval(mat)
		
	def new_thickness(self, random):
		'''
		Generates a thickness for the path element using a uniform distribution centered about an 
		average value and ranging +/- 1 S.D.
		'''
		thickness = (self.avg - self.sd) + random*2*self.sd
		return thickness

from bisect import bisect, bisect_right, bisect_left
		
class material:
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
		Determines the mean free path of a neutron in the foam
		Requires the foam saturation to be provided
		'''
		self.name = 'lithiated foam'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/lithium_alpha_strut.csv', delimiter=','))
		self.ion_ionization = np.transpose(np.loadtxt('./data/lithium_triton_strut.csv', delimiter=','))
		#Calculate the mean free path of a thermal neutron in the lithiated foam
		strut_density = 1.2
		foam_atomic_mass = 18.9934032
		lithium_atomic_mass = 6.941
		lithiated_foam_atomic_mass = (lithium_atomic_mass*0.5 + foam_atomic_mass*0.5)/2.0
		percent_li = percent_lif*lithium_atomic_mass/lithiated_foam_atomic_mass
		li_micro_cs = 940E-24
		li_macro_cs = percent_li*6.022E23*li_micro_cs/lithium_atomic_mass
		self.mfp = 1E4*1/(strut_density*li_macro_cs)
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def lithium_argon(self):
		'''
		Creates the argon material for pores in lithiated foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'argon'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/lithium_alpha_argon.csv', delimiter=','))
		self.ion_ionization = np.transpose(np.loadtxt('./data/lithium_triton_argon.csv', delimiter=','))
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def boron_argon(self):
		'''
		Creates the argon material for pores in b4c coated foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'argon'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/boron_alpha_argon.csv'))
		self.ion_ionization = np.transpose(np.loadtxt('./data/boron_ion_argon.csv'))
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def carbon(self):
		'''
		Creates the carbon material for struts in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Use a mean free path of 1000000000 to prevent neutron interactions from occurring
		'''
		self.name = 'carbon'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/boron_alpha_carbon.csv'))
		self.ion_ionization = np.transpose(np.loadtxt('./data/boron_ion_carbon.csv'))
		self.mfp = 1000000000.0
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def enriched_b4c(self):
		'''
		Creates the enriched boron carbide material for layers in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Determines the mean free path of a neutron in the foam.
		'''
		self.name = 'B4C'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/boron_alpha_b4c.csv'))
		self.ion_ionization = np.transpose(np.loadtxt('./data/boron_ion_b4c.csv'))
		#Calculate the mean free path of a thermal neutron in the enriched b4c	
		b4c_density = 2.52
		percent_boron = 0.7826
		boron_enrichment = 1
		b4c_atomic_mass = 52.0107
		boron_micro_cs = 3842E-24
		self.mfp = 1E4*1/b4c_density*percent_boron*boron_enrichment*6.022E23*boron_micro_cs/b4c_atomic_mass
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def natural_b4c(self):
		'''
		Creates the natural boron carbide material for layers in the RVC foams.
		Reads in ionization and residual energy tables from ./data
		Determines the mean free path of a neutron in the foam.
		'''
		self.name = 'B4C'
		self.alpha_ionization = np.transpose(np.loadtxt('./data/boron_alpha_b4c.csv'))
		self.ion_ionization = np.transpose(np.loadtxt('./data/boron_ion_b4c.csv'))
		#Calculate the mean free path of a thermal neutron in the natural b4c		
		b4c_density = 2.52
		percent_boron = 0.7826
		boron_enrichment = 0.199
		b4c_atomic_mass = 55.255
		boron_micro_cs = 3842E-24
		self.mfp = 1E4*1/b4c_density*percent_boron*boron_enrichment*6.022E23*boron_micro_cs/b4c_atomic_mass
		#Set the length of the ionization tables
		self.set_ionization_table_length()
		
	def get_mfp(self):
		'''
		Returns the mean free path for the material
		'''
		return self.mfp
		
	def set_ionization_table_length(self):
		'''
		'''
		self.alpha_ionization_length = len(self.alpha_ionization[0])
		self.ion_ionization_length = len(self.ion_ionization[0])
		
	def get_x(self, energy, reaction_product):
		'''
		Determines the lead-in distance required for the reaction product to have a given energy.
		Searches through the ionization table for the 2 energies bounding the input energy and
		linearly interpolates the lead-in distance (x) between those points
		'''
		if reaction_product == 'alpha':
			length = self.alpha_ionization_length
			index = self.reverse_bisect(self.alpha_ionization[1], energy)
			if index >= length:
				x = self.alpha_ionization[0][length]
			elif energy == self.alpha_ionization[1][index]:
				x = self.alpha_ionization[0][index]
			elif index == 0:
				x = 0
			else:
				left_index, right_index = index - 1, index
				left_energy = self.alpha_ionization[1][left_index]
				right_energy = self.alpha_ionization[ 1][right_index]
				left_x = self.alpha_ionization[0][left_index]
				right_x = self.alpha_ionization[0][right_index]
				x = (left_energy - energy)/(left_energy - right_energy)*(right_x - left_x) + left_x
		else:
			length = self.ion_ionization_length
			index = self.reverse_bisect(self.ion_ionization[1], energy)
			if index >= length:
				x = self.ion_ionization[0][length - 1]
			elif energy == self.ion_ionization[1][index]:
				x = self.ion_ionization[0][index]
			elif index == 0:
				x = 0
			else:
				left_index, right_index = index - 1, index
				left_energy = self.ion_ionization[1][left_index]
				right_energy = self.ion_ionization[1][right_index]
				left_x = self.ion_ionization[0][left_index]
				right_x = self.ion_ionization[0][right_index]
				x = (left_energy - energy)/(left_energy - right_energy)*(right_x - left_x) + left_x
		#Need to convert from cm to um
		x = x*1E4
		return x
		
	def reverse_bisect(self, a, x):
		length = len(a)
		low = 0
		hi = length
		while low < hi:
			mid = (low + hi)//2
			if x > a[mid]: hi = mid
			else: low = mid + 1
		return low

	def get_res_energy(self, x, reaction_product):
		'''
		Determines the residual energy of the reaction product after traversing a distance (x) into
		the material.
		'''
		res_energy = float
		if reaction_product.name == 'alpha':
			length = self.alpha_ionization_length
			index = bisect_left(self.alpha_ionization[0], x*1E-4)
			if index >= length:
				res_energy = 0
			elif reaction_product.energy == self.alpha_ionization[0][index]:
				res_energy = self.alpha_ionization[0][index]
			else:
				left_index, right_index = index - 1, index
				left_energy = self.alpha_ionization[1][left_index]
				right_energy = self.alpha_ionization[1][right_index]
				left_x = self.alpha_ionization[0][left_index]
				right_x = self.alpha_ionization[0][right_index]
				res_energy = (right_x - x*1E-4)/(right_x - left_x)*(left_energy - right_energy) + right_energy
		else:
			length = self.ion_ionization_length
			index = bisect_left(self.ion_ionization[0], x*1E-4)

			if index >= length:
				res_energy = 0
			elif reaction_product.energy == self.ion_ionization[0][index]:
				res_energy = self.ion_ionization[0][index]
			else:
				left_index, right_index = index - 1, index
				left_energy = self.ion_ionization[1][left_index]
				right_energy = self.ion_ionization[1][right_index]
				left_x = self.ion_ionization[0][left_index]
				right_x = self.ion_ionization[0][right_index]
				res_energy = (right_x - x*1E-4)/(right_x - left_x)*(left_energy - right_energy) + right_energy
		return res_energy
