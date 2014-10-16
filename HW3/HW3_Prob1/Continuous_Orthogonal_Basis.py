'''
Created on Oct 13, 2014

@author: michael
'''
from Orthogonal_Basis import Orth_Basis

class Cont_Orth_Basis(Orth_Basis):
    '''
    classdocs
    '''


    def __init__(self, method):
        '''
        Constructor
        '''
        super(Cont_Orth_Basis, self).__init__("Continuous", method)
    
    def Transform(self, P, func):
        '''
        Takes in the Orthoganal basis functions (P) and
        function to be transformed (func) and returns 
        coefficients (A)
        '''
        raise NotImplementedError

    def Inverse_Transform(self, P, func):
        '''
        Takes a set of transformed function coefficients and
        finds the approximate function integral given the 
        correct expansion coefficients
        '''
        raise NotImplementedError