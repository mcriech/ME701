all: test_f90_demo test_cpp_demo f2py_demo swig_demo 

# Fortran demonstration
test_f90_demo:
	gfortran f90_demo.f90 test_f90_demo.f90 -o $@ 

# C++ demonstration
test_cpp_demo:
	g++ cpp_demo.cc test_cpp_demo.cc -o $@ 

# F2PY demonstration
f2py_demo:
	f2py2.7 -c -m $@ f90_demo.f90

# F2PY demonstration
swig_demo:
	swig2.0 -python -c++ cpp_demo.i
	g++ -fPIC -c cpp_demo.cc cpp_demo_wrap.cxx -I/usr/include/python2.7/
	g++ -shared cpp_demo.o cpp_demo_wrap.o -o _cpp_demo.so 

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
