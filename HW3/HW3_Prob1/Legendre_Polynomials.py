'''
Created on Oct 13, 2014

@author: michael
'''
from Continuous_Orthogonal_Basis import Cont_Orth_Basis

class Leg_Polys(Cont_Orth_Basis):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Constructor
        '''
        super(Leg_Polys, self).__init__("Legendre Polynomials")
        self.n = n
        
    def Find_P_Functions(self)    :
        
        return P