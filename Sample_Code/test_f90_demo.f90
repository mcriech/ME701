program test_f90_demo
  use f90_demo
  implicit none
  call allocate_a(10)
  a = 1.0_8
  print *, norm(a, 10)
  call deallocate_a
end program test_f90_demo