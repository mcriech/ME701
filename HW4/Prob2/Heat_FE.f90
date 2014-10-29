module heat_eqn_solver
implicit none

!Define the constants
real :: A = 1.0, B = 0.0, C = 1.0, D = 0.0, aa = 0.0, bb = 0.0, k = 2.05, Q = 5.0
real :: T0 = 100.0, TL = 100.0, dTdx_0 = 0.0, dTdx_L = 0.0
real :: L = 10.0, dx, change = 1.0
real, parameter :: tolerance = 0.0001
!Define some iteration variables
integer :: row, element,  n = 5
real, allocatable, dimension(:) :: Temps, Sol, Old_Temps
real, allocatable, dimension(:,:) :: Coeffs, Ident, Diag, Temp_Coeffs

contains

subroutine solve()
aa = A*T0 + B*dTdx_0
bb = C*TL + D*dTdx_L
dx = L/n
!Create the Temps and solution vectors
	allocate(Temps(n))
	allocate(Sol(n))
	allocate(Old_Temps(n))
	allocate(Coeffs(n,n))
	allocate(Ident(n,n))
	allocate(Diag(n,n))
	allocate(Temp_Coeffs(n,n))
    Temps = 0.0
    dx = L/n
    T0 = aa
    TL = bb
    Sol = Q*dx*dx/k
    !Change the first and last elements of Sol and Temps for
    !the boundary conditions
    Sol(1) = aa
    Temps(1) = T0
    Sol(n) = bb
    Temps(n) = TL
!Create the coeffs array
    Coeffs = 0.0
    !Do the interior rows of the coeffs array
    do row = 2, n - 1, 1
        Coeffs(row, row - 1) = 1.0
        Coeffs(row, row) = -2.0
        Coeffs(row, row + 1) = 1.0
    end do
    !Take care of the first and last rows of the coeffs array
    Coeffs(1, 1) = -A
    Coeffs(1, 2) = B
    Coeffs(n, n) = -C
    Coeffs(n, n - 1) = D
!Create an identity array
    Ident= 0.0
    !Set diagonal elements to 1.0
    do row = 1, n, 1
        Ident(row, row) = 1.0
    end do
!Create the inverse diagonal matrix (based on the coeffs array)
    Diag = 0.0
    !Set diagonal elements to 1/coeff(i,i)
    do row = 1, n, 1
        if(Coeffs(row,row) .ne. 0.0) THEN
            Diag(row, row) = 1/Coeffs(row, row)
        else
            Diag(row,row) = 0.0
        end if
    end do
!Iterate using the Jacobi method to find the solution
    Temp_Coeffs = 0.0
    Old_Temps = 0.0
    do while (change > tolerance .or. change < -tolerance)
        Old_Temps = Temps
        Temp_Coeffs = Ident- MATMUL(Diag, Coeffs)
        Temps = MATMUL(Temp_Coeffs, Temps) + Sol
        change = MAXVAL(Temps - Old_Temps)
    end do
    print *, Temps
	deallocate(Temps, Sol, Old_Temps, Coeffs, Ident, Diag, Temp_Coeffs)
end subroutine solve

end module heat_eqn_solver
