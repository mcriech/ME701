# ==================================================================================
#   Author: Michael Reichenberger
#   Date: 5/9/2014
#   File: Path_Rect.py
#   Uses: PM_RNG.py
#         math
#   Description:
#       Generates random path for a particle through a foam with rectangular struts
#		and circular pockets. The paths are generated randomly for each particle.
#		
#		A uniform distribution is used for strut thickness and pocket diameter
#		about some average value (from inspection of SEM images) and the strut width
#		varies uniformly between a max and min value (also from inspection with SEM)
#
#          Observed: Strut Mean - 0.0055 +- 0.00055
#                    Pocket Mean - 0.0600 +- 0.0200
# ==================================================================================
from __future__ import division

class Path:
	def __init__(self):
		self.path = []          
		#set the global max path length to the max range of the triton in Ar
		#This is set to restrict particles from traveling near omega = 0 for
		#infinate path lengths... resulting in a memory overload in the path
		#I chose 10 because it is greatter than the triton range in 4psig Ar
		self.global_maximum = 50
		#sets strut material properties and pocket properties
		#Maximum path length (cm)
		#5.0800 is the width (in cm) of a He3 tube
		self.maximum_length = 2#5.08
		#Strut properties
		self.strut_thick_mean =  0.004
		self.strut_thick_sigma = 0.25*self.strut_thick_mean
		self.strut_width_min =   0.0200
		self.strut_width_max =   0.0600
		#Pocket properties
		self.pocket_mean =       0.05
		self.pocket_sigma =      0.01
		#Initialize the path list
		self.path = []
		
	def create_strut(self, random):
		#Determine strut thickness (uniform from avg + sig to avg - sig)
		T = random.New()*2 - 1
		T = T*self.strut_thick_sigma + self.strut_thick_mean
		#Determine strut width (uniform from min to max)
		W = random.New()*(self.strut_width_max - self.strut_width_min) + self.strut_width_min
		return (T, W)
		
	def create_pocket(self, random):
		#Determine the pocket diameter (uniform from avg + sig to avg - sig)
		D = random.New()*2 - 1
		D = D*self.pocket_sigma + self.pocket_mean
		return D