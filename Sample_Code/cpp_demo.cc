#include "cpp_demo.hh"
#include <cmath>

Vector::Vector(int n) 
  : _size(n)
{
  _values = new double[_size];
}
Vector::~Vector()
{
  if (_values) delete [] _values;
  
}
double& Vector::operator[](int n)
{
  return _values[n];
}
int Vector::size()
{
  return _size;
}
void Vector::set(double v)
{
  for (int i = 0; i < _size; ++i)
    _values[i] = v;
}

double norm(Vector &a)
{
  double v = 0;
  for (int i = 0; i < a.size(); ++i)
    v += a[i]*a[i];
  return sqrt(v);
}