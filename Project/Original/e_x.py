# ==================================================================================
#   Author: Michael Reichenberger
#   Date: 5/9/2014
#   File: e_x.py
#   Uses: csv
#         math
#   Description:
#       Creates the E(x) function tables for each of the 4 cases (alpha and
#       triton in strut and argon)
#       
#       Methods can find x given E or E given x for the particle in any of the
#       4 cases by using a histogram of the E(x) function and linear interpolation
# ==================================================================================
import csv
import math

class E_X:
    def __init__(self):
          #build dEdx for alpha in Ar
          self.EX_alpha_Ar = []
          EX = csv.reader(open("./Data/alphaInArEX.csv", "r"))
          EX_list = []
          EX_list.extend(EX)
          i = 0
          for row in EX_list:
               self.EX_alpha_Ar.append([])
               for element in row:
                    subelement = element.split()
                    for number in subelement:
                         self.EX_alpha_Ar[i].append(float(number))
               i += 1
          #build dEdx for alpha in strut
          self.EX_alpha_Strut = []
          EX = csv.reader(open("./Data/alphaInStrutEX.csv", "r"))
          EX_list = []
          EX_list.extend(EX)
          i = 0
          for row in EX_list:
               self.EX_alpha_Strut.append([])
               for element in row:
                    subelement = element.split()
                    for number in subelement:
                         self.EX_alpha_Strut[i].append(float(number))
               i += 1
          #build dEdx for triton in Ar
          self.EX_triton_Ar = []
          EX = csv.reader(open("./Data/tritonInArEX.csv", "r"))
          EX_list = []
          EX_list.extend(EX)
          i = 0
          for row in EX_list:
               self.EX_triton_Ar.append([])
               for element in row:
                    subelement = element.split()
                    for number in subelement:
                         self.EX_triton_Ar[i].append(float(number))
               i += 1
          #build dEdx for triton in strut
          self.EX_triton_Strut = []
          EX = csv.reader(open("./Data/tritonInStrutEX.csv", "r"))
          EX_list = []
          EX_list.extend(EX)
          i = 0
          for row in EX_list:
               self.EX_triton_Strut.append([])
               for element in row:
                    subelement = element.split()
                    for number in subelement:
                         self.EX_triton_Strut[i].append(float(number))
               i += 1            
               
    def find_x_alpha_Ar(self, E):
           i = 0
           while self.EX_alpha_Ar[i][1] > E:
               i += 1
           ratio = math.fabs((E - self.EX_alpha_Ar[i][1])/(self.EX_alpha_Ar[i - 1][1] - self.EX_alpha_Ar[i][1]))
           x = self.EX_alpha_Ar[i][0] - (self.EX_alpha_Ar[i][0] - self.EX_alpha_Ar[i - 1][0])*ratio
           return x
           
    def find_E_alpha_Ar(self, x):
           i = 0
           if x < self.EX_alpha_Ar[len(self.EX_alpha_Ar) - 1][0]:
               while self.EX_alpha_Ar[i][0] < x:
                   i += 1
               ratio = math.fabs((x - self.EX_alpha_Ar[i - 1][0])/(self.EX_alpha_Ar[i][0] - self.EX_alpha_Ar[i - 1][0]))
               E = self.EX_alpha_Ar[i - 1][1] - (self.EX_alpha_Ar[i - 1][1] - self.EX_alpha_Ar[i][1])*ratio
           else:
               E = 0
           return E
           
    def find_x_alpha_Strut(self, E):
           i = 0
           while self.EX_alpha_Strut[i][1] > E:
               i += 1
           ratio = math.fabs((E - self.EX_alpha_Strut[i][1])/(self.EX_alpha_Strut[i - 1][1] - self.EX_alpha_Strut[i][1]))
           x = self.EX_alpha_Strut[i][0] - (self.EX_alpha_Strut[i][0] - self.EX_alpha_Strut[i - 1][0])*ratio
           return x
           
    def find_E_alpha_Strut(self, x):
           i = 0
           if x < self.EX_alpha_Strut[len(self.EX_alpha_Strut) - 1][0]:
               while self.EX_alpha_Strut[i][0] < x:
                   i += 1
               ratio = math.fabs((x - self.EX_alpha_Strut[i - 1][0])/(self.EX_alpha_Strut[i][0] - self.EX_alpha_Strut[i - 1][0]))
               E = self.EX_alpha_Strut[i - 1][1] - (self.EX_alpha_Strut[i - 1][1] - self.EX_alpha_Strut[i][1])*ratio
           else:
               E = 0
           return E
    
    def find_x_triton_Ar(self, E):
           i = 0
           while self.EX_triton_Ar[i][1] > E:
               i += 1
           ratio = math.fabs((E - self.EX_triton_Ar[i][1])/(self.EX_triton_Ar[i - 1][1] - self.EX_triton_Ar[i][1]))
           x = self.EX_triton_Ar[i][0] - (self.EX_triton_Ar[i][0] - self.EX_triton_Ar[i - 1][0])*ratio
           return x
           
    def find_E_triton_Ar(self, x):
           i = 0
           if x < self.EX_triton_Ar[len(self.EX_triton_Ar) - 1][0]:
               while self.EX_triton_Ar[i][0] < x:
                   i += 1
               ratio = math.fabs((x - self.EX_triton_Ar[i - 1][0])/(self.EX_triton_Ar[i][0] - self.EX_triton_Ar[i - 1][0]))
               E = self.EX_triton_Ar[i - 1][1] - (self.EX_triton_Ar[i - 1][1] - self.EX_triton_Ar[i][1])*ratio
           else:
               E = 0
           return E
           
    def find_x_triton_Strut(self, E):
           i = 0
           while self.EX_triton_Strut[i][1] > E:
               i += 1
           ratio = math.fabs((E - self.EX_triton_Strut[i][1])/(self.EX_triton_Strut[i - 1][1] - self.EX_triton_Strut[i][1]))
           x = self.EX_triton_Strut[i][0] - (self.EX_triton_Strut[i][0] - self.EX_triton_Strut[i - 1][0])*ratio
           return x
           
    def find_E_triton_Strut(self, x):
           i = 0
           if x < self.EX_triton_Strut[len(self.EX_triton_Strut) - 1][0]:
               while self.EX_triton_Strut[i][0] < x:
                   i += 1
               ratio = math.fabs((x - self.EX_triton_Strut[i - 1][0])/(self.EX_triton_Strut[i][0] - self.EX_triton_Strut[i - 1][0]))
               E = self.EX_triton_Strut[i - 1][1] - (self.EX_triton_Strut[i][1 - 1] - self.EX_triton_Strut[i][1])*ratio
           else:
               E = 0
           return E
    
