// The syntax is %module module_name, i.e., the name
// you want to import.  All of the C++ includes you need
// should be included here.
%module cpp_demo
%{
#include "cpp_demo.hh"
%}

// This is a special
%ignore *::operator[];

%include "cpp_demo.hh"

%extend Vector
{
   double  __getitem__(int n) 
   { 
     return (*self)[n]; 
   }
   void __setitem__(int n, double v) 
   { 
     (*self)[n] = v; 
   }
}