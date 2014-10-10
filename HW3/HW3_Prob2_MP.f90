PROGRAM MP_Integration
 IMPLICIT NONE

 !Initialize variables 
 INTEGER, PARAMETER :: dimensions = 2, points = 100
 INTEGER :: dimension_1, dimension_2, dimension_3, point, point_2, t1, t2, clock_rate, clock_max
 REAL :: z = 0.0, var = 0.0, zi, I = 0.0, sI = 0.0, x = 0.0, solution = 1.0, error, dx
 !Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 
 !Get the analytical solution
 DO dimension_1 = 1, dimensions
  solution = solution*(2.0/3.0)
 END DO
 
 !Do the MidPoint rule approximation
 !In general, the MidPoint method takes the value at the center point, multiplied by the
 !differential volume about that point
 !dx is the same for each dimension in this case since they all vary from 0 - 1
 dx = 1.0/(points)
 !Need to find the volumes at each midpoint, for each dimension
 DO dimension_1 = 1, dimensions
 !Need to go in each dimensional direction with midpoints
  DO dimension_2 = 1, dimensions
 !Need to find the value at each point of integration  
   DO point = 0, points - 1
    zi = 1.0
    x = point*dx + dx/2
 !Need to calculate the actual value of x1*x2*...*xn
    DO dimension_3 = 1, dimensions
     zi = x*zi
    END DO
    zi = sqrt(zi)*(dx**dimensions)
    I = I + zi
   END DO
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
