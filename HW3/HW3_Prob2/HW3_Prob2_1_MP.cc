#include <cmath>
#include <ctime>
#include <cstdio>
#include <iostream>
#include <stdlib.h>

int main()
{
//Initialzie Variables
const int dimensions = 3, points = 100;
int dimension_1 = 0, dimension_2 = 0, dimension_3 = 0, its = 0, t1, t2;
double I = 0.0, x = 0.0, solution = 1.0, duration, x_1, x_2, x_3, dx;

//Start Timer
std::clock_t start;
start = std::clock();

//Get the analytical solution
for (dimension_1 = 0; dimension_1 < dimensions; ++dimension_1)
{
 solution = solution *(2.0/3.0);
}

dx = 1.0/(points/dimensions);

//Do the MP loop
for (dimension_1 = 0; dimension_1 < points/dimensions; ++dimension_1)
{
 x_1 = dx*dimension_1 + dx/2;
 for (dimension_2 = 0; dimension_2 < points/dimensions; ++dimension_2)
 {
  x_2 = dx*dimension_2 + dx/2;
  for (dimension_3 = 0; dimension_3 < points/dimensions; ++dimension_3)
  {
   x_3 = dx*dimension_3 + dx/2;
   I = I + sqrt(x_1*x_2*x_3)*pow(dx, dimensions);
   ++its;
  }
 }
}


//Print out the answers
std::cout<<"Dimensions: "<<dimensions<<" Iterations: "<<its<<'\n';
std::cout<<"MidPoint Sol: "<<I<<'\n';
std::cout<<"Analytical Sol: "<<solution<<'\n';
std::cout<<"Relateive Error: "<<fabs(I - solution)/solution<<'\n';
//End timer
duration = (std::clock() - start)/ (double) CLOCKS_PER_SEC;
std::cout<<"Time: "<< duration <<'\n';
return 0;
}
