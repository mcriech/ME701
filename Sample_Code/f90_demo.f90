module f90_demo

double precision, parameter :: PI = 3.14159265359_8
double precision, allocatable, dimension(:) :: a

contains

double precision function norm(v, n)
  double precision, intent(in) :: v(n)
  integer, intent(in) :: n
  integer :: i
  norm = 0.0_8
  do i = 1, n
    norm = norm + v(i)**2
  end do
  norm = sqrt(norm)
end function norm

subroutine allocate_a(n)
  integer, intent(in) :: n
  allocate(a(n))
end subroutine allocate_a

subroutine deallocate_a()
  deallocate(a)
end subroutine deallocate_a

end module f90_demo