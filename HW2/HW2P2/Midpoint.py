from __future__ import division

def midpoint(func, lower, upper, N):
    integral = 0
    dx = (upper - lower)/N
    for n in range(N):
        x = lower + n*dx + dx/2
        integral += func(x)*dx
    return integral