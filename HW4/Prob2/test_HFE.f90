program test_HFE
  use HFE
  implicit none
  n = 6
  call Allocate_Matrices
  call Create_Identity_matrix
  call Create_Temp_Sol_Vectors
  call Create_Coeffs_Matrix
  call Create_Diag_Matrix
  call Solve
  call Deallocate_Matrices
end program test_HFE
