# Test of the F2PY hfe_Py module
from f2py_HFE import *
from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

divisions = input('How many division?\n')

heat_eqn_solver.n = divisions
heat_eqn_solver.solve()

temps = heat_eqn_solver.temps

plt.figure(1)
x = np.linspace(0, heat_eqn_solver.l, heat_eqn_solver.n)
print temps
plt.plot(x, temps, '-o')
plt.xlabel('x position')
plt.ylabel('Temp')
plt.show()


heat_eqn_solver.deallocate()