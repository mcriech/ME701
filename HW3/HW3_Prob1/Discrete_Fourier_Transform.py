'''
Created on Oct 13, 2014

@author: michael
'''
from Discrete_Orthogonal_Basis import Discrete_Orth_Basis

class Disc_Fourier_Trans(Discrete_Orth_Basis):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Constructor
        '''
        super(Disc_Fourier_Trans, self).__init__("Discrete Fourier Transform")
        self.n = n        
        
    def Find_P_Functions(self):
        
        return P