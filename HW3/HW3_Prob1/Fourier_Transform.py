'''
Created on Oct 13, 2014

@author: michael
'''
from Continuous_Orthogonal_Basis import Cont_Orth_Basis

class Fourier_Trans(Cont_Orth_Basis):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Constructor
        '''
        super(Fourier_Trans, self).__init__("Fourier Transform")
        self.n = n   
    
    def Find_P_Functions(self):
        
        return P