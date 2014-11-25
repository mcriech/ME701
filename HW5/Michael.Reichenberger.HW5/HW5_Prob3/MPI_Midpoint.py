from mpi4py import MPI
import numpy as np
import time

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()	

upper_bound = 100.0
lower_bound = 0.0
points = 20000.0
dx = (upper_bound - lower_bound)/points
a = int(1 + (points / size)*rank)
b = int((points / size)*(rank + 1))

partial_integral = 0.0

while a <= b:
 x = dx*a - dx/2
 a += 1
 for j in range(int(points)):
  y = dx*j + dx/2
  partial_integral += (x + y)*dx**2

if rank == 0:
 integral = partial_integral
 for r in range(1, size):
  integral += comm.recv(source=r, tag=111)

else:
 comm.send(partial_integral, dest=0, tag=111)

end = time.time()
time = end - start

if rank == 0:
 print "Integral:", integral, "Time:", time, "seconds"