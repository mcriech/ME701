import numpy as np

def Function_1(x):
    y = x**5
    return y

def Function_2(x):
    y = 1/(x**2 + 1)
    return y

def Function_3(x):
    y = x*np.sin(x)/(1 + np.cos(x)**2)
    return y