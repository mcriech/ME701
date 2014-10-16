# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:01:14 2014

@author: Michael
"""
import numpy as np

def Legendre(x, l):
    c = (l)*[0]
    c.append(1)
    y = np.polynomial.legendre.legval(x, c)
    return y