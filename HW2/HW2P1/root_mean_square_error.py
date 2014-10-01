#The root_mean_square_error fucntion takes in a tuple of coeffieicnts, the
#function with which to use the coefficients, and a set of data points
#and then computes the root mean square error by comparing the function 
#values to the data points.
#The data list must contain inputs and single result
import inspect
from math import sqrt

def RMS_E(coefficients, function, data):
    #Check the number of coefficients required by function
    func_coeffs = inspect.getargspec(function)[0]
    #Check that the number of coefficients supplied matches the number of coeffs needed by func.
    if len(coefficients) != len(func_coeffs[0]):
        print "number of coefficients specified must equal the number of coefficients in the function"
    else:
        #set the results column as the last column in the data list
        result_pos = len(data[0]) - 1
        #initialize the Root Mean Squared list
        RMS = []
        #initialize the Root Mean Squared error to 0
        RMS_error = 0
        #Determine the number of data points by observing the length of the data set
        N = len(data)
        #For each data point, find the root mean squqred error by taking the difference between the 
        #given value and the calculated value
        for point in range(N):
            func_input = []
            #Assume the result value is the last in the data list
            for i in range(result_pos):
                func_input.append(data[point][i])
            #Calculate a result by using the inputs for this point
            calculated_value = function(coefficients, func_input)
            #Add a new list to the RMS list
            RMS.append([])
            #Add the given value to the RMS list
            RMS[point].append(data[point][result_pos])
            #Add teh calculated value to the RMS list
            RMS[point].append(calculated_value)
            #Calculate the RMS error for this point
            RMS[point].append(((RMS[point][1] - RMS[point][0])**2)/N)
            #Add the error from this point to the sum of the errors
            RMS_error += RMS[point][2]
    #Find the square root of the Root Mean Square error
    RMS_error = sqrt(RMS_error)
    print "Current RMS error:", RMS_error
    return RMS_error
        