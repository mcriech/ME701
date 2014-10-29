# Test of the F2PY hfe_Py module
from f2py_HFE import *
from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

divisions = input('How many division?\n')

heat_eqn_solver.n = divisions
heat_eqn_solver.Solve()

temps = heat_eqn_solver.Temps

heat_eqn_solver.Deallocate_Matrices()

plt.figure(1)
x = np.linspace(0, hfe.L, hfe.n)
plt.scatter(x, temps, '-o')
xlabel('x position')
ylabel('Temp')
plt.show()