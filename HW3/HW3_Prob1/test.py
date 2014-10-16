# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:03:15 2014

@author: Michael
"""
import scipy.integrate
import numpy as np
from legendre import Legendre

def f(x):
    y = np.exp(x)
    return y

g = lambda x: f(x)*Legendre(x, 2)
print scipy.integrate.quad(g, -1.0, 1.0)