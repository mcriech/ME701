all: HFE HFE_Py

# Fortran demonstration
HFE:
	gfortran HFE.f90 test_HFE.f90 -o $@ 

# F2PY demonstration
HFE_Py:
	f2py2.7 -c -m $@ HFE.f90

# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x *wrap.cxx *.so

# Same, but leave the shared objects
neat:
	@rm -f *.o *.mod *-x *wrap.cxx

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .f90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<
