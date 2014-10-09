PROGRAM MP_Integration
 IMPLICIT NONE

 !Initialize variables 
 INTEGER, PARAMETER :: dimensions = 3, points = 100
 INTEGER :: dimension_1, dimension_2, point, point_2, t1, t2, clock_rate, clock_max
 REAL :: z = 0.0, var = 0.0, zi, I = 0.0, sI = 0.0, x = 0.0, solution = 1.0, error, dx
 l!Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 
 !Get the analytical solution
 DO dimension_1 = 1, dimensions
  solution = solution*(2.0/3.0)
 END DO
 
 !Do the MidPoint rule approximation
 dx = 1.0/(points)
 DO dimension_1 = 1, dimensions
  
  DO point = 0, points - 1
   zi = 1.0
   x = point*dx + dx/2
   DO dimension_2 = 1, dimensions
    zi = x*zi
   END DO
   zi = sqrt(zi)*dx
   I = I + zi
  END DO
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
