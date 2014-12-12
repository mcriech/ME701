'''
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 

'''
from __future__ import division
import time
import sys
from mpi4py import MPI
from history import *
from rng import *
from particle import *
from foam import *
from run_manager import *

#Set up MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
	start_time = time.time()

#Set foam
foam = foam()
foam.diameter = 2.0E4
foam.li_imp(1)
#foam.strut.new('Li foam strut', 13.0, 1.0, 'self.mat.li_foam(0.045)') 

#Set # histories and stride
n = 1E5

#Determine histories per node
n_per_node = int(n/size)

#Generate a run manager for each node 
run = run_manager(foam)
#Set the LLD for the simulation (eV)
run.set_lld(954000.0)
#Set the number of histories for each node
run.set_histories(n_per_node)

#All nodes run histories
for i in range(n_per_node):
	iteration = n_per_node*rank + i
	run.execute_history(iteration)
#Collect counts, interactions, escapes, and phs from all nodes
if rank != 0:
	comm.send(run.counts, dest=0, tag=221)
	comm.send(run.escapes, dest=0, tag=222)
	comm.send(run.interactions, dest=0, tag=223)
	comm.send(run.iteration, dest=0, tag=224)
else:
	counts = run.counts
	escapes = run.escapes
	interactions = run.interactions
	histories = run.iteration
	for r in range(1, size):
		counts += comm.recv(source=r, tag=221)
		escapes += comm.recv(source=r, tag=222)
		interactions += comm.recv(source=r, tag=223)
		histories += comm.recv(source=r, tag=224)
#Output results
	efficiency = float(counts) / float(histories) * 100.0
	print "Intrinsic Thermal Neutron Efficiency:\n", foam.name, "foam\n", foam.diameter*1E-4, "cm cylindrical device:\n", efficiency, "%"
	print "histories:", histories
	print "interaction:", interactions
	print "escapes:", escapes
	print "counts:", counts

	end_time = time.time()
	time = end_time - start_time
	print "Execution Time:", time
























