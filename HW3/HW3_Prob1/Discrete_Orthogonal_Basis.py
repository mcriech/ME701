'''
Created on Oct 13, 2014

@author: michael
'''
from Orthogonal_Basis import Orth_Basis

class Discrete_Orth_Basis(Orth_Basis):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        The weights for a discrete orthoganol basis are discrete values
        '''
        self.weights = []
        self.P = []
        