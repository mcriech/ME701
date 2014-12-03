"""
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 
RNG
	Variables
		Seed: Int
		a: Int
		m: Int
	Methods
		Generate New Random Number
		Generate Random Number Vector
"""
from __future__ import division
class rng:
    '''
    Class Definition
    '''
    def __init__(self):
        '''
        This sets the seed equal to the seed used in 
        Exploring Monte Carlo Methods [Dunn & Shultis] if no seed is provided
        '''
        self.seed = 73907
        self.a = 16807.
        self.m = 2147483647.
        
    def define(self, a, m, seed):
        '''
        Seed the generator with 'seed'
        '''        
        self.a = a
        self.m = m
        self.seed = seed
		
	def seed(self, seed):
		'''
		Sets a new seed for the RNG
		'''
		self.seed = seed
        
    def vector(self, N):
        '''
        Generates a vector of N random numbers from 0 to 1
        '''
        vec = [0 for i in range(N)]
        for j in range(N):
            self.seed = self.a*self.seed%self.m  
            vec[j] = float(int(self.seed)/self.m)
        return vec
    
    def int_vector(self, N):
        '''
        Generates a vector of N random integers from 0 to m
        '''
        vec = [0 for i in range(N)]
        for j in range(N):
            self.seed = self.a*self.seed%self.m  
            vec[j] = self.seed
        return vec
        
    def new(self):
        '''
        Generates a new random number from 0 - 1 based on the seed value
        '''
        self.seed = self.a*self.seed%self.m   
        return float(int(self.seed)/self.m)
     
    def int_new(self):
        '''
        Generates a new random integer from 0 to m based on the seed value
        '''
        self.seed = self.a*self.seed%self.m   
        return self.seed
