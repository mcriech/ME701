module hfe

real, allocatable, dimension(:) :: Temps, Sol
real, allocatable, dimension(:,:) :: Coeffs, Ident, Diag
real :: A = 1.0, B = 0.0, C = 1.0, D = 0.0, aa = 100.0, bb = 100.0
real :: T0, TL, L = 10.0, dx, change = 1.0
real :: k = 1.0, Q = 5.0
real, parameter :: tolerance = 0.0001
integer :: row, element, n = 5

contains

subroutine Create_Matrices()
    !Create the temperatures and solution arrays
    allocate(Temps(n))
    allocate(Sol(n))
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
    !Create the Identity Matrix
    allocate(Ident(n,n))
    Ident= 0.0
    !Set diagonal elements to 1.0
    do row = 1, n, 1
        Ident(row, row) = 1.0
    end do
    !Create the coefficient arrays
    allocate(Coeffs(n,n))
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
    Coeffs(n, n) = D
    Coeffs(n, n - 1) = -C
    !Create the inverse diagonal for the jacobi method
    allocate(Diag(n,n))
    Diag = 0.0
    !Set diagonal elements to 1/coeff(i,i)
    do row = 1, n, 1
        Diag(row, row) = 1/Coeffs(row, row)
    end do
end subroutine Create_Matrices

subroutine Solve()
    real, allocatable, dimension(:) :: Old_Temps
    real, allocatable, dimension(:,:) :: Temp_Coeffs
    allocate(Temp_Coeffs(n,n))
    allocate(Old_Temps(n))
    Temp_Coeffs = 0.0
    Old_Temps = 0.0
    do while (change > tolerance .or. change < - tolerance)
        Old_Temps = Temps
        Temp_Coeffs = Ident - MATMUL(Diag, Coeffs)
        Temps = MATMUL(Temp_Coeffs, Temps) + Sol
        change = MAXVAL(Temps - Old_Temps)
    end do
    deallocate(Temp_Coeffs, Old_Temps)
end subroutine Solve

subroutine Deallocate_Matrices()
    deallocate(Temps, Sol, Coeffs, Ident, Diag)
end subroutine Deallocate_Matrices

end module hfe
