# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:03:15 2014

@author: Michael
"""
from Legendre_Polynomials import Leg_Polys
from Fourier_Transform import Fourier_Trans
from Discrete_Fourier_Transform import Disc_Fourier_Trans
import scipy.integrate as integrate
from scipy.special import jn as bessel

def Test_1(x):
    return x**2 + x + 1.0

def Test_2(x):
    return 1.0/(1.0 + x**2)
    
def Test_3(x):
    return bessel(0,x)
#TESTS is an array of the functions we want to test
TESTS = [Test_1, Test_2, Test_3]
#Test_Res is an array of the test results
Leg_Test_Res = []
Four_Test_Res = []
Disc_Test_Res = []
#Use Continuous Legendre Polynomials to approximate the 3 test functions    
#Generate the test basis as a legendre polynomial basis
Leg = Leg_Polys(2)
Four = Fourier_Trans(1)
Disc = Disc_Fourier_Trans(10)
#Perform each test by transforming the function and then inverse transforming it
#Compare the inverse transform approximation to the numerical quadriture built
#into scipy
for test in TESTS:
    Leg_trans = Leg.Transform(test, -1, 1)
    Four_trans = Four.Transform(test, -1, 1)
    Disc_trans = Four.Transform(test, -1, 1)
    Leg_inv_trans = Leg.Inverse_Transform(Leg_trans)
    Four_inv_trans = Four.Inverse_Transform(Four_trans)
    Disc_inv_trans = Four.Inverse_Transform(Disc_trans)
    Leg_comp = integrate.quad(test, -1, 1)
    Four_comp = Leg_comp
    Disc_comp = Leg_comp
    Leg_Test_Res.append((Leg_inv_trans, Leg_comp))
    Four_Test_Res.append((Four_inv_trans, Four_comp))
    Disc_Test_Res.append((Disc_inv_trans, Disc_comp))
    print (Leg_inv_trans, Leg_comp[0])
    print (Four_inv_trans, Four_comp[0])
    print (Disc_inv_trans, Disc_comp[0])
    
