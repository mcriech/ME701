all: f2py_HFE Fortran

# Fortran
Fortran:
	gfortran Heat_FE.f90 test_HFE.f90 -o TEST

# F2PY 
f2py_HFE:
	f2py2.7 -c -m $@ Heat_FE.f90

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
