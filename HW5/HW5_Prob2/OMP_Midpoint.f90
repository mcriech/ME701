program OMP_Midpoint

use omp_lib
implicit none

 INTEGER :: points = 200000, threads = 8
 INTEGER :: time_start, time_end, time_rate, clock_max, i = 1, j = 1
 REAL, PARAMETER :: lower_bound = 0.0, upper_bound = 100.0
 DOUBLE PRECISION :: time, dx = 1.0, integral = 0.0, integral_partial = 0.0, x = 0.0, y = 0.0

 Call OMP_set_num_threads(threads)

 !Intitialize the midpoint stuff
 dx = (upper_bound - lower_bound)/(real(points))  

 Call SYSTEM_CLOCK(time_start, time_rate, clock_max)
 !Do the parallel calculation here
 !$omp parallel private (j, y, integral_partial) shared(i, x, points, integral)
 x = 0.0
 !$omp do
 do i = 1, points
  x = x + dx
  y = 0.0
  do j = 1, points
   y = y + dx
   integral_partial = integral_partial + (x + y)*dx*dx
  end do
 end do
 !$omp end do
 !$omp critical
 integral = integral + integral_partial
 !$omp end critical
 !$omp end parallel
 Call SYSTEM_CLOCK(time_end, time_rate, clock_max)
 time = real(time_end - time_start)/real(time_rate) 

 !Print out the solution
 print *, "dx =", dx
 print *, "Solution =", integral
 print *, "Time =", time, "seconds"

end program OMP_Midpoint


