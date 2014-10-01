#HW2_Problem1.py
#Michael Reichenberger
#Due: 2014.9.29
#In NE 495, you might recall having learned about the semi-empirical mass formula 
#(SEMF), which fits nuclear mass data to a function of the atomic number (i.e., 
#number of protons) Z and mass number (i.e., number of protons and neutrons) A. 
#Traditionally, the SEMF is given the form
#Your task is lto determine the 5 coefficients a_v , a_s , a_c , a_a , and a_s by
#fitting the given function to the mass data provided online.
#Deliverables:
#1. Short summary of how you solved the problem.
#2. The coefficient values.
#3. The root mean square error.
#4. A plot of the measured data and your fitting function.
#5. Your very well-documented, very clean code.
#=============================================================================================#
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from root_mean_square_error import RMS_E
from SEMF import SEMF
#=============================================================================================#
#Use the cool XKCD ploting format
plt.xkcd()
minimize = optimize.minimize
#Load the data from masses.txt into a numpy array
mass_data = np.loadtxt('masses.txt')
#Minimize the root mean square error in order to find the correct coefficients
#Initialize the first guess at coefficients
starting_coeffs = (1, 0, 0, 0, 0)
#Run the minization function in scipy.optimize
#Want to minimize the RMS error. Start with the inital guess at coeffs. The RMS function
#also needs arguements of the function to RMS (SEMF in this case) and data to comepare to
#(mass_data in this case). These additional arguements are just tacked onto the end of the
#minimize function call.
results = minimize(RMS_E, starting_coeffs, (SEMF, mass_data))
#Print the results of the minization
#print results.message
coeffs = results.x
print "\nCoefficients:", coeffs
RMS_error = results.fun
print "Minimized RMS Error:", RMS_error
#=============================================================================================#
#Plot the data and the approximation
#Desire a  3D plot and a 2D representative slice
#First, initialize the lists which will be used to plot
x = [];
y = []
x2d = []
z = []
z2d = []
z_calc = []
z2d_calc = []
#Assign values to each list for the scatter plots
#Loop through the mass_data list
for i in range(len(mass_data)):
    #Add the a value for the current point
    x.append(mass_data[i][0])
    #Add the z value for the current point
    y.append(mass_data[i][1])
    #Add the BE value for the current point
    z.append(mass_data[i][2])
    #Calculate a BE value using the coefficients found before
    z_calc.append(SEMF(coeffs, (mass_data[i][0], mass_data[i][1])))
    #For a certain 'A' vaule, collect Z and BE data for the 2D slice plot
    if mass_data[i][1] == 69:
        x2d.append(mass_data[i][0])
        z2d.append(mass_data[i][2])
        z2d_calc.append(SEMF(coeffs, (mass_data[i][0], mass_data[i][1])))
#=============================================================================================#
#Plot the 2 fiture
#Initialize figure 1
fig1 = plt.figure()
#Add a third axis to figure 1
ax = fig1.add_subplot(111, projection='3d')
#Scatter plot the given values
ax.scatter(x, y, z, c='b')
#Scatter plot the calculated values
ax.scatter(x, y, z_calc, c='r')
#Save figure 1
plt.savefig('3D_SEMF_plot.jpg')
#Initialize figure 2
fig2 = plt.figure()
plt.xlabel('Z')
plt.xlim((25, 36))
plt.ylabel('Binding Energy')
plt.ylim((68.9, 69))
plt.title('2D Slice for A = 69')
#Scatter plot the given values for the 2D slice
plt.scatter(x2d, z2d, c='b', label='Data"')
#Scatter plot the calculated values for the 2D slice
plt.plot(x2d, z2d_calc, c='r', label='Calcs')
plt.legend(loc=4)
#Save figure 2
plt.savefig('2D_SEMF_slice.jpg')
#Show the figures
plt.show()
