from __future__ import division

def simpson(func, lower, upper, N):
    integral = 0
    dx = (upper - lower)/N
    for n in range(N):
        x = lower + n*dx + dx/2
        a = x - dx/2
        b = x + dx/2
        integral += ((b - a)/6)*(func(a) + 4*func((a + b)/2) + func(b))
    return integral