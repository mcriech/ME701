PROGRAM MP_Integration
 IMPLICIT NONE

 !Initialize variables 
 INTEGER, PARAMETER :: dimensions = 1, points = 10000
 INTEGER :: point, t1, t2, clock_rate, clock_max 
 INTEGER :: dimension_1, dimension_2, dimension_3
 REAL :: I = 0.0, solution = 1.0, error, dx
 REAL :: x_1 = 0.0
 !Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 
 !Get the analytical solution
 DO dimension_1 = 1, dimensions
  solution = solution*(2.0/3.0)
 END DO
 
 
 dx = 1.0/(points/dimensions) 

 DO dimension_1 = 0, points/dimensions - 1
  x_1 = dx*dimension_1 + dx/2
  I = I + sqrt(x_1)*(dx**dimensions)
 END DO

 error = abs(I - solution)
 !Print out the answers
 print *, "      Mid Point Sol:", I
 print *, "Analytical Solution:", solution
 print *, "Absolute Error:", error
 print *, "Relative Error:", error/solution
 !End the timer
 CALL system_clock(t2, clock_rate, clock_max)
 print *, "dimensions:", dimensions, "midpionts:", points
 print *, "Time:", real(t2 - t1)/real(clock_rate), "seconds"
END PROGRAM MP_Integration
