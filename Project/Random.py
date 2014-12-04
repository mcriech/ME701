class Random() :
 
    def __init__(self, S0 = 19073486328125, stride=150000) :
        self.S0 = S0 # seed
        self.stride = stride 
        self.S  = S0
        self.g = 19073486328125 # g, 5^19
        self.c = 0  
        self.TwoToMMinus1 = 281474976710655        # 2^48 - 1
        self.OneOver2toM  = 1. / 281474976710656.0 # 1/2^48
 
    def rand(self) :
        self.S = (((self.g*self.S) & self.TwoToMMinus1) + self.c) & self.TwoToMMinus1 
        return self.S * self.OneOver2toM 

    def skip_ahead(self, skip) :
        nskip = skip
        nskip = nskip & self.TwoToMMinus1 # modulo(nskip,2^M)
        BigG  = 1           
        tmpg  = self.g
        BigC  = 0
        tmpc  = self.c
        while nskip > 0  :
            if nskip % 2 :  # Checks 0th bit of nskip: 0=even, 1=odd
                BigG = (BigG*tmpg) & self.TwoToMMinus1 
                BigC = (BigC*tmpg) & self.TwoToMMinus1
                BigC = (BigC+tmpc) & self.TwoToMMinus1
            gp    = (tmpg+1)    & self.TwoToMMinus1
            tmpg  = (tmpg*tmpg) & self.TwoToMMinus1
            tmpc  = (gp*tmpc)   & self.TwoToMMinus1
            nskip = nskip >> 1
        rn = (BigG*self.S0) & self.TwoToMMinus1
        rn = (rn + BigC)    & self.TwoToMMinus1 
        return rn

    def initialize_history(self, h) :
        self.S = self.skip_ahead(h*self.stride)
        print self.S

if __name__ == "__main__" :
    import time
    import numpy as np
    R = Random(123)
    R.initialize_history(100)
    n = 1000000
    t0 = time.time()
    for i in range(n) :
        a = R.rand()
        #a = np.random.rand()  <-- np is about 4 times faster  
    t1 = time.time()
    et = t1-t0
    print "Elapsed: ", et
    print "rg's per sec = ", n / et
    
    """
    How to use:
    
    R = Random(123)
    for history in my_range_of_histories :
        R.initialize_history(history)
        do_stuff() 
    """


