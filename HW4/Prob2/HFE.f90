module HFE
implicit none

real, allocatable, dimension(:) :: Temps, Sol
real, allocatable, dimension(:,:) :: Coeffs, Ident, Diag
!Define the constants
real :: A = 1.0, B = 0.0, C = 1.0, D = 0.0, aa = 100.0, bb = 100.0, k = 1.0, Q = 5.0
real :: T0, TL, L = 10.0, dx, change = 1.0
real, parameter :: tolerance = 0.0001
integer :: n = 5

contains

subroutine Allocate_Matrices()
    allocate(Temps(n), Sol(n), Coeffs(n,n), Ident(n,n), Diag(n,n))
end subroutine Allocate_Matrices

subroutine Create_Temp_Sol_Vectors()
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
end subroutine Create_Temp_Sol_Vectors

subroutine Create_Identity_Matrix()
    integer :: row, element
    Ident= 0.0
    !Set diagonal elements to 1.0
    do row = 1, n, 1
        Ident(row, row) = 1.0
    end do
end subroutine

subroutine Create_Coeffs_Matrix()
    integer :: row
    Coeffs = 0.0
    !Do the interior rows of the coeffs array
    do row = 2, n - 1, 1
        Coeffs(row, row - 1) = 1.0
        Coeffs(row, row) = -2.0
        Coeffs(row, row + 1) = 1.0
    end do
    !Take care of the first and last rows of the coeffs array
    Coeffs(1, 1) = A
    Coeffs(1, 2) = B
    Coeffs(n, n) = C
    Coeffs(n, n - 1) = D
end subroutine Create_Coeffs_Matrix

subroutine Create_Diag_Matrix()
    real :: temp
    integer :: row, element
    Diag = 0.0
    !Set diagonal elements to 1/coeff(i,i)
    do row = 1, n, 1
        temp = Coeffs(row, row)
        Diag(row, row) = 1/temp
    end do
end subroutine Create_Diag_Matrix

subroutine Solve()
    real, allocatable, dimension(:,:) :: Temp_Coeffs
    real, allocatable, dimension(:) :: Old_Temps
    real :: change = 1.0
    allocate(Temp_Coeffs(n,n))
    allocate(Old_Temps(n))
    Temp_Coeffs = 0.0
    Old_Temps = 0.0
    do while (change > tolerance .or. change < -tolerance)
        Old_Temps = Temps
        Temp_Coeffs = Ident- MATMUL(Diag, Coeffs)
        Temps = MATMUL(Temp_Coeffs, Temps) + Sol
        change = MAXVAL(Temps - Old_Temps)
    end do
    deallocate(Temp_Coeffs, Old_Temps)
end subroutine Solve

subroutine Deallocate_Matrices()
    deallocate(Temps, Sol, Coeffs, Ident, Diag)
end subroutine Deallocate_Matrices

end module HFE
