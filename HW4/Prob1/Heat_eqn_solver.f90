program Heat_eqn_solver
implicit none

!Define the constants
real :: A = 1.0, B = 1.0, C = 1.0, D = 1.0, aa = 0.0, bb = 0.0, k = 1.0, Q = 5.0
real :: T0 = 100.00, TL = 100.00, dTdx_0 = 0.0, dTdx_L = 0.0
real :: L = 10.0, dx, change = 1.0
real, parameter :: tolerance = 0.0001
!Define some iteration variables
integer :: row, element,  n = 5
!Define the problem arrays
real, allocatable, dimension(:) :: Temps, Old_Temps, Sol
real, allocatable, dimension(:,:) :: Coeffs, I, Diag, Temp_Coeffs


Allocate (Temps(n), Old_Temps(n), Sol(n), Coeffs(n,n),I(n,n), Diag(n,n), Temp_Coeffs(n,n))
aa = A*T0 + B*dTdx_0
bb = C*TL + D*dTdx_L

dx = L/n

!Create the Temps and solution vectors
!The Temps vector will be all zeros to start
do element = 2, n - 1, 1
    Sol(element) = Q*dx*dx/k
    Temps(element) = 0.0
end do
Sol(1) = aa
Temps(1) = T0
Sol(n) = bb
Temps(n) = TL
!Create the coeffs array
do row = 2, n - 1, 1
    do element = 1, n, 1
        Coeffs(row, element) = 0.0
    end do
    Coeffs(row, row - 1) = 1.0
    Coeffs(row, row) = -2.0
    Coeffs(row, row + 1) = 1.0
end do
!Take care of the first and last rows of the coeffs array
do element = 1, n, 1
    Coeffs(1, element) = 0.0
    Coeffs(n, element) = 0.0
end do
Coeffs(1, 1) = 1.0
Coeffs(n, n) = 1.0
!Create an identity array
do row = 1, n, 1
    do element = 1, n, 1
        I(row, element) = 0.0
    end do
    I(row, row) = 1.0
end do
!Create the inverse diagonal matrix (based on the coeffs array)
do row = 1, n, 1
    do element = 1, n, 1
        Diag(row, element) = 0.0
    end do
    Diag(row, row) = 1/Coeffs(row, row)
end do
!Iterate using the Jacobi method to find the solution
do while (change > tolerance .or. change < -tolerance)
    Old_Temps = Temps
    Temp_Coeffs = I - MATMUL(Diag, Coeffs)
    Temps = MATMUL(Temp_Coeffs, Temps) + sol
    change = MAXVAL(Temps - Old_Temps)
end do
!Print out the solution
print *, Temps
Deallocate (Temps, Old_Temps, Sol, Coeffs, I, Diag, Temp_Coeffs)
end program Heat_eqn_solver
