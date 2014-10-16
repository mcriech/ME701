# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 16:03:15 2014

@author: Michael
"""
from Legendre_Polynomials import Leg_Polys

import scipy.integrate as integrate
from scipy.special import jn as bessel

def Test_1(x):
    y = x**2 + x + 1
    return y

def Test_2(x):
    y = 1/(1 + x**2)
    return y
    
def Test_3(x):
    y = bessel(0,x)
    return y

#Use Continuous Legendre Polynomials to approximate the 3 test functions    
#Generate the test basis as a legendre polynomial basis
test = Leg_Polys(10)
#Perform each test by transforming the function and then inverse transforming it
#Compare the inverse transform approximation to the numerical quadriture built
#into scipy
test_1_Transform = test.Transform(Test_1, 0, 10)
test_1_Inverse_Transform = test.Inverse_Transform(test_1_Transform)
test_1_Numerical_Integration = integrate.quad(Test_1, 0, 10)[0]
#Save the inverse transform approximation and numerical quadriture values in
#a tuple to be referenced later for comparison
TEST_1 = (test_1_Inverse_Transform, test_1_Numerical_Integration)
#Repeat for test_2
test_2_Transform = test.Transform(Test_2, -1, 1)
test_2_Inverse_Transform = test.Inverse_Transform(test_2_Transform)
test_2_Numerical_Integration = integrate.quad(Test_2, -1, 1)[0]
TEST_2 = (test_2_Inverse_Transform, test_2_Numerical_Integration)
#Repeat for test_3
test_3_Transform = test.Transform(Test_3, -1, 1)
test_3_Inverse_Transform = test.Inverse_Transform(test_3_Transform)
test_3_Numerical_Integration = integrate.quad(Test_3, -1, 1)[0]
TEST_3 = (test_3_Inverse_Transform, test_3_Numerical_Integration)
#Print out the results
print TEST_1, '\n', TEST_2, '\n', TEST_3
