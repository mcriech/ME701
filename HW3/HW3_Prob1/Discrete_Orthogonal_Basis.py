'''
Created on Oct 13, 2014

@author: michael
'''
from Orthogonal_Basis import Orth_Basis

class Discrete_Orth_Basis(Orth_Basis):
    '''
    classdocs
    '''

    def __init__(self, method):
        '''
        Constructor
        '''
        super(Discrete_Orth_Basis, self).__init__("discrete", method)