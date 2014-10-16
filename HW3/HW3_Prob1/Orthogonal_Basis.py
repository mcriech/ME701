'''
Created on Oct 13, 2014

@author: michael
'''
import numpy as np
import scipy.integrate as integrate

class Orth_Basis(object):
    '''
    classdocs
    '''

    def __init__(self, type_of_basis, method):
        '''
        Constructor
        '''
        self.type_of_basis = type_of_basis
        self.method = method
        self.n = None
        
    def Transform(self, P, func, a, b):
        '''
        Takes in the Orthoganal basis functions (P) and
        function to be transformed (func) and returns 
        coefficients (A)
        '''
        self.a = a
        self.b = b
        F = self.n*[0]
        #If continuous basis, work with functions
        if self.type_of_basis == "continuous" :
            for l in range(self.n):
                #We need to combine the continuous basis function and the input
                #function to feed into the integrate function
                self.g = lambda x: P[l]*func(x)
                #The coefficient is the integral from a to b of the product of
                #the basis function and the input function
                F[l] = integrate.quad(self.g, self.a, self.b)
        #If discrete basis, work with vectors 
        elif self.type_of_basis == 'discrete' :
            for l in range(self.n):
                #The coefficient is the dot product of the basis function vector
                #and the function vector                
                F[l] = np.dot(P[l], func)
        else:
            print "You have selected an invalid basis type... sucks for you"
        return F

    def Inverse_Transform(self, P, F):
        '''
        Takes a set of transformed function coefficients and
        finds the approximate function integral given the 
        correct expansion coefficients
        '''
        f_approx = 0.0        
        #If continuous basis, work with functions
        if self.type_of_basis == "continuous" :
            for l in range(self.n):
                #We need to combine the continuous basis function and the input
                #function to feed into the integrate function
                self.g = lambda x: F[l]*P[l]
                #The coefficient is the integral from a to b of the product of
                #the basis function and the input function
                f_approx = f_approx + self.g
            #Integrate the sum of the coefficients with the basis functions
            f_approx = integrate.quad(f_approx, self.a, self.b)
        #If discrete basis, work with vectors 
        elif self.type_of_basis == 'discrete' :       
            for l in range(self.n):
                #The approximate integral is the sum of all of the f~ and the basis
                #function coefficients
                f_approx = f_approx + np.dot(F[l], P[l])
        return f_approx
            