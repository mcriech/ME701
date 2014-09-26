#HW2_Problem2.py
#Michael Reichenberger
#Due: 2014.9.29
#Deliverables:
#1. Compute and plot the relative, absolute error of your integration, for each quadrature, and for each
#integral as a function of N for N = 1, 2, . . . , 10. Use a log scale for the y -axis. You should have three
#three plots: one per function, with three curves per plot.
#2. Comment on any strange or unexpected results.
#3. Your very well-documented, very clean code. By the way, if you can make use of, e.g., scipy , for
#expediting some of this, that is acceptable and encouraged (though knowing how to set up your
#own integrator can be useful in the field...)
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
import Functions
from Midpoint import midpoint
from Simpson import simpson
from Legendre_Gauss import leg_gauss

plt.xkcd()
#============================================================================================================#
#Define the functions that I want to integrate
F1 = Functions.Function_1
F2 = Functions.Function_2
F3 = Functions.Function_3
#Initialize the analytical answers and estimates list
Ans = (0.0, float(2*np.arctan(float(1/5)) - np.pi), float(np.pi**2/4))
Est = [[]]
#Do the 3 integrations for 1 - 10 intervals
maxN = 10
for N in range(maxN):
    Est.append([])
#For each method, save the aproximation for each function as a list in the Est list
#============================================================================================================#
#MIDPOINT Method
    Est[N].append([])
    Est[N][0].append(midpoint(F1, 1, -1, N + 1))
    Est[N][0].append(midpoint(F2, 5, -5, N + 1))
    Est[N][0].append(midpoint(F3, 0, np.pi, N + 1))
#============================================================================================================#
#SIMPOSONS Method
    Est[N].append([])
    Est[N][1].append(simpson(F1, 1, -1, N + 1))
    Est[N][1].append(simpson(F2, 5, -5, N + 1))
    Est[N][1].append(simpson(F3, 0, np.pi, N + 1))
#============================================================================================================#
#GAUSS_LEGENDRE Method
    Est[N].append([])
    Est[N][2].append(leg_gauss(F1, 1, -1, N + 1))
    Est[N][2].append(leg_gauss(F2, 5, -5, N + 1))
    Est[N][2].append(leg_gauss(F3, 0, np.pi, N + 1))
#============================================================================================================#
#Plot everything
#Figure 1 is for Function 1
fig1 = plt.figure()
plt.title('Function 1')
plt.xlabel('N')
plt.ylabel('Normalized, Absolute Error (log)')
midpoint_error = []
simps_error = []
gl_error = []
#Find the errors for each method by comparing the anser for the first function to the estimates for each N
for N in range(maxN):
    midpoint_error.append(np.abs((Ans[0] - Est[N][0][0])))
    simps_error.append(np.abs((Ans[0] - Est[N][1][0])))
    gl_error.append(np.abs((Ans[0] - Est[N][2][0])))
x = np.linspace(1, 10, num=10)
plt.semilogy(x, midpoint_error, c='b', label='midpoint')
plt.semilogy(x, simps_error, c='r', label='simpson')
plt.semilogy(x, gl_error, c='g', label='Leg. Gauss')
plt.legend()
#Figure 2 is for Function 2
fig2 = plt.figure()
plt.title('Function 2')
plt.xlabel('N')
plt.ylabel('Normalized, Absolute Error (log)')
midpoint_error = []
simps_error = []
gl_error = []
#Find the errors for each method by comparing the anser for the second function to the estimates for each N
for N in range(maxN):
    midpoint_error.append(np.abs((Ans[1] - Est[N][0][1])/Ans[1]))
    simps_error.append(np.abs((Ans[1] - Est[N][1][1])/Ans[1]))
    gl_error.append(np.abs((Ans[1] - Est[N][2][1])/Ans[1]))
x = np.linspace(1, 10, num=10)
plt.semilogy(x, midpoint_error, c='b', label='midpoint')
plt.semilogy(x, simps_error, c='r', label='simpson')
plt.semilogy(x, gl_error, c='g', label='Leg. Gauss')
plt.legend()
#Figure 3 is for Function 3
fig3 = plt.figure()
plt.title('Function 3')
plt.xlabel('N')
plt.ylabel('Normalized, Absolute Error (log)')
midpoint_error = []
simps_error = []
gl_error = []
#Find the errors for each method by comparing the anser for the third function to the estimates for each N
for N in range(maxN):
    midpoint_error.append(np.abs((Ans[2] - Est[N][0][2])/Ans[2]))
    simps_error.append(np.abs((Ans[2] - Est[N][1][2])/Ans[2]))
    gl_error.append(np.abs((Ans[2] - Est[N][2][2])/Ans[2]))
x = np.linspace(1, 10, num=10)
plt.semilogy(x, midpoint_error, c='b', label='midpoint')
plt.semilogy(x, simps_error, c='r', label='simpson')
plt.semilogy(x, gl_error, c='g', label='Leg. Gauss')
plt.legend()
plt.show()