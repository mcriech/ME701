'''
created: 2014.11.19
@author: Michael Reichenberger
'''
'''
Import Statements
'''
import sys, getopt
from particle_path.py import *
from PM_RNG.py import PM_RNG
import numpy as np
import matplotlib.pyplot as plt

'''
Look for user input of parameters as options
    Coated RVC vs Li Impregnated
    Strut average
    Strut SD
    Pore Average
    Pore SD
    Layer Average (If Applicable)
    Layer SD (If Applicable)
'''
Foam_type = 'Li_Imp'
Strut_Avg = 0.004
Strut_Sigma = 0.25*Strut_Avg
Pore_Avg = 0.05
Pore_Sigma = 0.25*Pore_Avg
Layer_Avg = None
Layer_Sigma = None    


'''
Create the particle path parameters and broadcast them to the other nodes
'''


'''
Split up the histories for each node
'''


'''
Generate random number vectors for each node
'''


'''
Run the simulation on all nodes
'''


'''
Determine total interactions > LLD for each node
Generate strut and pore histogram data for each node
Generate the PHS histogram data for each node
'''


'''
Sum interactions > LLD from all nodes
Gather strut and pore histogram data from all nodes
Gather the PHS histogram data from all nodes to develop a single PHS
'''


'''
Determine the intrinsic neutron detection efficiency
'''


'''
Plot the PHS
'''


'''
Export PHS to .\Foam_Simulation_Results\"TAG"_PHS.csv
Export other results to .\Foam_Simulation_Results aswell
'''