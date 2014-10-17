"""
Created on Wed Oct 15 16:01:14 2014

@author: Michael

Find the legendre polynomial of degree l using numpy's legendre function
"""
import numpy as np

def Disc_Fourier(x, l):
    y = np.fft.fft([x])[0]
    return y