#include "cpp_demo.hh"
#include <iostream>
int main()
{
  Vector V(10);
  V.set(1.0);
  std::cout << norm(V) << std::endl;
  return 0;
}