program OMP_Midpoint

use omp_lib
implicit none

 INTEGER, PARAMETER :: points = 10, dimensions = 2, threads = 1
 INTEGER :: time_start, time_end, time_rate, clock_max, i, j
 REAL, PARAMETER :: lower_bound = 0.0, upper_bound = 1.0
 REAL :: time, dx
 REAL :: x_temp, y_temp, temp, integral_partial = 0.0, integral = 0.0


 Call OMP_set_num_threads(threads)

 !Intitialize the midpoint stuff
 dx = (upper_bound - lower_bound)/(real(points))  

 Call SYSTEM_CLOCK(time_start, time_rate, clock_max)
 !Do the parallel calculation here
 !$omp parallel
 !$omp do
 do i = 0, points - 1
  x_temp = dx*i + dx/2.0
  print *, x_temp
  !$omp do
  do j = 0, points - 1
   y_temp = dx*j + dx/2.0
   temp = integrand(x_temp, y_temp)
   integral_partial = integral_partial + temp*dx**2
  end do
  !$omp end do
 end do
 !$omp end do
 !$omp critical
 integral = integral + integral_partial
 !$omp end critical
 !$omp end parallel
 Call SYSTEM_CLOCK(time_end, time_rate, clock_max)
 time = real(time_end - time_start)/real(time_rate) 

 !Print out the solution
 print *, "Solution =", integral
 print *, "Time =", time, "seconds"
 
CONTAINS
  REAL function integrand(x, y)
   implicit none
   REAL, INTENT(IN) :: x, y
    integrand = sqrt(x + y)
  end function integrand

end program OMP_Midpoint


