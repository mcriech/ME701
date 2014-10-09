PROGRAM PRIME_FINDER
 IMPLICIT NONE
 INTEGER, PARAMETER :: n = 100000
 INTEGER :: test, numb, i, k, np = 1, j, t1, t2, clock_rate, clock_max
 INTEGER, DIMENSION(n/2) :: temp_primes
 INTEGER, DIMENSION(:), ALLOCATABLE :: primes
 
 !Start the timer
 CALL system_clock(t1, clock_rate, clock_max)
 !Make a list of all of the odd numbers less than n
 j = 1
 temp_primes(j) = 2
 DO k = 2, n/2
  temp_primes(k) = (k*2 - 1) 
 END DO

 !Find the primes in the list
 !For each number in the temp_primes list, check to see if it is divisible by any of the 
 !other numbers in the list
 DO i = 2, n/2 - 1
  j = 2
  numb = temp_primes(i)
  test = temp_primes(j)
  DO while (i /= j .and. MOD(numb, test) /= 0 .and. j < n/2)
   j = j + 1
   test = temp_primes(j)
  END DO
  IF (i == j .or. MOD(numb, test) /= 0) THEN
   np = np + 1
   temp_primes(np) = numb
  END IF
 END DO

 !Make a new primes list that is only as long as the number of primes found
 ALLOCATE(primes(np))
 DO i = 1, np
  primes(i) = temp_primes(i)
 END DO

 !End the timer
 CALL system_clock(t2, clock_rate, clock_max)
 
 !Print out the results
 print *, "Found", np, "primes in", real(t2 - t1)/real(clock_rate), "seconds"
 print *, "My python script Found 9592 primes in 1E5 in 74.125 seconds..."
 print *, "FORTRAN can do that in a meer 0.74 seconds, 10,000 times faster!!!"
END PROGRAM PRIME_FINDER
