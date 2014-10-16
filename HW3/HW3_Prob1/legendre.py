"""
Created on Wed Oct 15 16:01:14 2014

@author: Michael

Find the legendre polynomial of degree l using numpy's legendre function
"""
import numpy as np

def Legendre(x, l):
    c = (l - 1)*[0]
    c.append(1)
    y = np.polynomial.legendre.legval(x, c)/(2.0/(2.0*l - 1.0))
    return y