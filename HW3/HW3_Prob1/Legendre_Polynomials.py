'''
Created on Oct 13, 2014

@author: michael
'''
from Continuous_Orthogonal_Basis import Cont_Orth_Basis
from legendre import Legendre
class Leg_Polys(Cont_Orth_Basis):
    '''
    classdocs
    '''


    def __init__(self, n):
        '''
        Build the continuous orthoganal basis from the legendre polynomials.
        Need to specify how many degrees we would like to approximate to (n)
        Then, the list P is returned as the Legendre function which will 
        require an evaluation point and degree at the time of execution.
        '''
        super(Leg_Polys, self).__init__("Legendre Polynomials")
        self.n = n
        self.P = self.Find_P_Functions()
        
    def Find_P_Functions(self):
        n = self.n        
        P = n*[0.0]        
        for l in range(n):
            P[l] = Legendre
        return P