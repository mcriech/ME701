PROGRAM MC_Integration
 IMPLICIT NONE

 !Initialize variables 
 !n = number of dimensions for the integral
 !N = number of MC iterations
 INTEGER, PARAMETER :: dimensions = 10, iterations = 1000000
 INTEGER :: dimension = 0, iteration = 0, t1, t2, clock_rate, clock_max
 REAL :: z = 0.0, var = 0.0, zi = 1.0, I = 0.0, sI = 0.0, x = 0.0, solution = 1.0
 !Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 !Get the analytical solution
 DO dimension = 1, dimensions
  solution = solution*(2.0/3.0)
 END DO
 !Get all of the random numbers
 CALL RANDOM_SEED()
 !Begin the MC loop
 DO iteration = 1, iterations
  zi = 1.0
  DO dimension = 1, dimensions
   CALL RANDOM_NUMBER(x)
   zi = zi*x
  END DO
  var = var + zi/iterations
  zi = sqrt(zi)
  z = z + zi/iterations  
 END DO
 !Find the expected value and standard deviation
 I = z
 var = var
 sI = sqrt((var - I*I)/iterations)
 !Print out the answers
 print *, "    Monte Carlo Sol:", I, "+/-", sI
 print *, "Analytical Solution:", solution
 print *, "Relative Error:", sI/solution
 !End the timer
 CALL system_clock(t2, clock_rate, clock_max)
 print *, "dimensions:", dimensions, "iterations:", iterations
 print *, "Time:", real(t2 - t1)/real(clock_rate), "seconds"
END PROGRAM MC_Integration
