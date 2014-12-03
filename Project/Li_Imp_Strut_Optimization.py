'''
Created: Monday Dec 1st, 2014

@author: Michael Reichenberger

Purpose: 

'''
from __future__ import division
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

#Set foam
foam = foam()
foam.diameter = 2.0E4
foam.li_imp(0.045)
#foam.strut.new('Li foam strut', 13.0, 1.0, 'self.mat.li_foam(0.275)') 

#Set # histories and stride
n = 1000
stride = 1500

#Determine histories per node
n_per_node = int(n/size)

#Generate a run manager for each node 
run = run_manager(foam)
#Set the LLD for the simulation (eV)
run.set_lld(954000.0)
#Set the number of histories for each node
run.set_histories(n_per_node)

#Generate the random numbers for all the nodes
random_vector = []
if rank == 0:
	rng = rng()
	for r in range(1, size):
		random_vector = []
		for i in range(n_per_node):
			random_vector.append(rng.vector(stride))
		comm.send(random_vector, dest=r, tag=111)
	for i in range(n_per_node):
		run.random_vector.append(rng.vector(stride))
else:
	run.random_vector = comm.recv(source=0, tag=111)

#All nodes run histories
for i in range(n_per_node):
	run.execute_history()
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























