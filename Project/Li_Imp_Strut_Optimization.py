'''
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 

'''

from mpi4py import MPI
from history.py import *
from rng.py import *
from particle.py import *
from foam.py import *
from run_manager.py import *

#Set up MPI
comm = MPI.COMM_WORLD
rank = comm.get_rank()
size = comm.Get_size()

#Set foam
foam = foam()
foam.li_imp(0.275)

#Set # histories and stride
n = 10000
stride = 1000

#Determine histories per node
n_per_node = int(n/size)

#Generate a generic history class 
run = run_manager(foam)
run.set_histories(n_per_node)
run.set_stride(stride)

#Determine which seed to start at for this node
if rank == 0:
	for r in range(1, size):
		for i in range(n_per_node):
			random_number_vector(i) = rng.vector(stride)
		comm.send(random_number_vector, dest=r, tag=111)
	random_number_vector = rng.vector(node_stride)
else:
	random_number_vector = comm.recv(source=0, tag=111)

run.random_vector = random_number_vector		

#All nodes run histories
for i in range(n_per_node):
	run.execute_history()

#Collect counts, interactions, escapes, and phs from all nodes
if rank == 0:
	counts = comm.reduce(run.counts, root=0, op=MPI.SUM)
	escapes = comm.reduce(run.escapes, root=0, op=MPI.SUM)
	interactions = comm.reduce(run.interactions, root=0, op=MPI.SUM)
	histories = comm.reduce(run.iteration, root=0, op=MPI.SUM)
#Output results
	efficiency = float(counts / histories)
	print "Intrinsic Thermal Neutron Efficiency for a", foam.name, "foam in a", foam.diameter*1E-4, "cm cylindrical device:", efficiency
























