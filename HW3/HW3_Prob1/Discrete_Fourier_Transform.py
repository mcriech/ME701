'''
Created on Oct 13, 2014

@author: michael
'''
from Discrete_Orthogonal_Basis import Discrete_Orth_Basis
from disc_fourier import Disc_Fourier
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
        self.P = self.Find_P_Functions()
        
    def Find_P_Functions(self):
        n = self.n        
        P = n*[0.0]        
        for l in range(n):
            P[l] = Disc_Fourier
        return P