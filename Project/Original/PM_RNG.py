# ==================================================================================
#   Author: Michael Reichenberger
#   Date: 3/5/2014
#   File: PM_RNG.py
#   Uses: math
#   Description:
#       Class which generate a random number using a Parks and Miller RNG algorithm
#       modified from Exploring Monte Carlo Methods [Dunn & Shultis]
#       METHODS:
#           .__init__: sets the seed to a default value if no seed is given
#           .Seed    : changes the seed variable
#           .New     : generates a new random number
# ==================================================================================
class PM_RNG:
    def __init__(self):
    #This sets the seed equal to the seed used in 
    #Exploring Monte Carlo Methods [Dunn & Shultis] if no seed is provided
        self.seed = 73907
        self.a = 16807.
        self.m = 2147483647.
        
    def Define(self, a, m, seed):
    #Seed the generator with 'seed'
        self.a = a
        self.m = m
        self.seed = seed
        
    def Vector(self, N):
    #Generates a vector of N random numbers
    #Based on Parks and Miller RNG algorithm
        vec = [0 for i in range(N)]
        for j in range(N):
            self.seed = self.a*self.seed%self.m  
            #values 0 - 1
            vec[j] = float(int(self.seed)/self.m)
            #integer values
            #vec[j] = self.seed
        return vec
    
    def New(self):
    #Generates a new random number based on the seed value
    #Based on Parks and Miller RNG algorithm
        self.seed = self.a*self.seed%self.m   
        
        #Return the 0-1 value
        return float(int(self.seed)/self.m)
        
        #Return the value
        #return self.seed
