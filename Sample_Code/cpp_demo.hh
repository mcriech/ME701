class Vector
{
public:
  // constructor
  Vector(int n);
  // destructor
  ~Vector();
  // Overload the operator [] in order 
  // to access/change elements of vector
  int size();
  double& operator[](int n);
  void set(double v);
private:
  int _size;
  double* _values;
};

double norm(Vector &a);