PROGRAM MP_Integration
 IMPLICIT NONE

 !Initialize variables 
 INTEGER, PARAMETER :: dimensions = 10, points = 70
 INTEGER :: point, t1, t2, clock_rate, clock_max, runs = 0
 INTEGER :: dimension_1, dimension_2, dimension_3, dimension_4, dimension_5
 INTEGER :: dimension_6, dimension_7, dimension_8, dimension_9, dimension_10
 DOUBLE PRECISION :: I = 0.0
 REAL :: solution = 1.0, error, dx
 REAL :: x_1 = 0.0,x_2 = 0.0,x_3 = 0.0,x_4 = 0.0, x_5 = 0.0, x_6 = 0.0
 REAL :: x_7 = 0.0, x_8 = 0.0, x_9 = 0.0, x_10 = 0.0
 !Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 
 !Get the analytical solution
 DO dimension_1 = 1, dimensions
  solution = solution*(2.0/3.0)
 END DO
 
 dx = 1.0/(points/dimensions) 

 DO dimension_1 = 0, points/dimensions - 1
  x_1 = dx*dimension_1 + dx/2
  DO dimension_2 = 0, points/dimensions - 1
   x_2 = dx*dimension_2 + dx/2
   DO dimension_3 = 0, points/dimensions - 1
    x_3 = dx*dimension_3 + dx/2
    DO dimension_4 = 0, points/dimensions - 1
     x_4 = dx*dimension_4 + dx/2
     DO dimension_5 = 0, points/dimensions - 1
      x_5 = dx*dimension_5 + dx/2
      DO dimension_6 = 0, points/dimensions - 1
       x_6 = dx*dimension_6 + dx/2
       DO dimension_7 = 0, points/dimensions - 1
        x_7 = dx*dimension_7 + dx/2
        DO dimension_8 = 0, points/dimensions - 1
         x_8 = dx*dimension_8 + dx/2
         DO dimension_9 = 0, points/dimensions - 1
          x_9 = dx*dimension_9 + dx/2
          DO dimension_10 = 0, points/dimensions - 1
           x_10 = dx*dimension_10 + dx/2
           I = I + sqrt(x_1*x_2*x_3*x_4*x_5*x_6*x_7*x_8*x_9*x_10)*(dx**dimensions)
           runs = runs + 1
          END DO
         END DO
        END DO
       END DO
      END DO
     END DO
    END DO
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
 print *, "dimensions:", dimensions, "midpionts:", runs
 print *, "Time:", real(t2 - t1)/real(clock_rate), "seconds"
END PROGRAM MP_Integration
