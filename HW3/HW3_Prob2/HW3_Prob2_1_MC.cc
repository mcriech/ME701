#include <cmath>
#include <ctime>
#include <cstdio>
#include <iostream>
#include <stdlib.h>

int main()
{
//Initialzie Variables
const int dimensions = 10, iterations = 1000000;
int dimension = 0, iteration = 0, t1, t2;
double z = 0.0, var = 0.0, zi = 1.0, I = 0.0, sI = 0.0, x = 0.0, solution = 1.0, duration;

//Start Timer
std::clock_t start;
start = std::clock();

//Get the analytical solution
for (dimension = 0; dimension < dimensions; dimension += 1)
{
 solution = solution *(2.0/3.0);
}
//Do the MC loop
for (iteration = 0; iteration < iterations; iteration += 1)
{
 zi = 1.0;
 for (dimension = 0; dimension < dimensions; dimension += 1)
 {
  x = (double) rand()/RAND_MAX;
  zi = zi*x;
 }
 zi = sqrt(zi);
 z = z + zi/iterations;
 var = var + zi*zi/iterations;
}
//Find the expected value and the standard deviation
I = z;
sI = sqrt((var - I*I)/iteration);
//Print out the answers
std::cout<<"Dimensions: "<<dimensions<<" Iterations: "<<iterations<<'\n';
std::cout<<"Monte Carlo Sol: "<<I<<" +/- "<<sI<<'\n';
std::cout<<"Analytical Sol: "<<solution<<'\n';
std::cout<<"Relateive Error: "<<sI/solution<<'\n';
//End timer
duration = (std::clock() - start)/ (double) CLOCKS_PER_SEC;
std::cout<<"Time: "<< duration <<'\n';
return 0;
}
