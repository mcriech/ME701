from __future__ import division

def SEMF((a1, a2, a3, a4, a5), (Z, A)):
    be = (a1*A + a2*A**(float(2/3)) + a3*(Z**2)/(A**(float(1/3))) + a4*((A - 2*Z)**2)/A + a5/(A**(0.5))*((-1)**(Z%2) + (-1)**((A - Z)%2)))
    return be