'''
created: 2014.11.19
@author: Michael Reichenberger
'''
'''
Import Statements
'''
import numpy as np

'''
Class Definition
'''
class particle_path(object) :
    '''
    Particle Path Class Description
    '''
    
    def __init__(self) :
        '''
        Inititialize 
        '''
        pass

    def set_strut_material(self) :
        '''
        Set Strut Material
        '''
        pass

    def get_strut_material(self) :
        '''
        Get Strut Material
        '''
    
    def set_strut_parameters(self) :
        '''
        Set Strut Parameter
        '''
        pass
    
    def set_layer_material(self) :
        '''
        Set Layer Material
        '''
        pass
    
    def get_layer_material(self) :
        '''
        Get Layer Material
        '''
        pass
    
    def set_layer_parameters(self) :
        '''
        Set Layer Parameters
        '''
        pass
    
    def get_layer_parameters(self) :
        '''
        Get Layer Parameters
        '''
        pass
    
    def generate_strut(self) :
        '''
        Strut Generation
        '''
        pass
    
    def generate_pore(self) :
        '''
        Pore Generation
        '''
        pass
    
    def generate_theta(self) :
        '''
        Generates Theta
        '''
        pass
    
    def generate_psi(self) :
        '''
        Generate Psi
        '''
        pass
     
    def get_strut_length(self) :
        '''
        Strut Path Length
        '''
        pass
        
    def get_pore_length(self) :
        '''
        Strut Path Length
        '''
        pass

    def get_current_material(self) :
        '''
        Get Current Material
        '''
        pass
    
    def get_strut_stats(self) :
        '''
        Report statistics about the struts
        '''
        pass
    
    def get_pore_stats(self) :
        '''
        Report statistics about the pores
        '''
        pass
    
    def get_path(self) :
        '''
        Report the path
        '''
        pass
    
class neutron_path(particle_path) :
    '''
    Neutron Path Class Description
    '''
    
    def __init__(self) :
        '''
        Init Description
        '''
        super(particle_path, self).__init__()
        pass
    
    def set_lamnda(self) :
        '''
        Set the Interaction Coefficient
        '''
        pass
    
    def get_interaction_location(self) :
        '''
        Get Neutron Interaction Location
        '''
        pass

    def transport_neutron(self) :
        '''
        Neutron Transport
        '''
        pass    
    
    def set_neutron_escape(self) :
        '''
        Set Neutron Escaped Status
        '''
        pass
    
    def get_neutron_escape(self) :
        '''
        Get Neutron Escaped Status
        '''
        pass
    
class reaction_product_path(particle_path) :
    '''
    Reaction Product Path Class Description
    '''
    
    def __init__(self) :
        '''
        Init Description
        '''
        super(particle_path, self).__init__()
        pass
    
    def set_particle_type(self) :
        '''
        Set Particle Teyp
        '''
        pass
    
    def get_particle_type(self) :
        '''
        Get Particle Type
        '''
        pass
    
    def read_ionization_data(self) :
        '''
        Read in the Ionization Data
        '''
        pass
    
    def transport_reaction_product(self) :
        '''
        Transport Reaction Product
        '''
        pass
    
    def add_ionization_energy(self) :
        '''
        Add Ionization Energy
        '''
        pass
    
    def find_total_ionization(self) :
        '''
        Find Total Ionization
        '''
        pass
    
    def find_previous_x(self) :
        '''
        Find x
        '''
        pass
    
    def find_residual_energy(self) :
        '''
        Find Residual Energy
        '''
        pass