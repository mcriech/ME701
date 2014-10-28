# Test of the F2PY HFE_Py module
from HFE_Py import *

HFE.Allocate_Matrices()
HFE.Create_Identity_Matrix()
HFE.Create_Temp_Sol_Vectors()
HFE.Create_Coeffs_Matrix()
HFE.Create_Diag_Matrix()
HFE.Solve()

print HFE.Temps

HFE.Deallocate_Matrices()