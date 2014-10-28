# Test of the F2PY module
from f2py_demo import *

f90_demo.allocate_a(10)
f90_demo.a[:] = 1.0
print f90_demo.norm(f90_demo.a)
f90_demo.deallocate_a()
