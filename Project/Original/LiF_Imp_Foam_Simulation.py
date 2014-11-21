# ==================================================================================
#   Author: Michael Reichenberger
#   Date: 5/9/2014
#   File: Foam_Neutron_MC_Simulation.py
#   Uses: E_X.py
#         PM_RNG.py
#         math
#         matplotlib.pyplot
#   Description:
#       Determine the energy deposition from alphas and tritons (from Li6 reaction
#       in a foam.
#       Strut mean and sigma must be set
#       Pocket mean and sigma must be set
# ==================================================================================
from __future__ import division
from PM_RNG import PM_RNG
import math
import matplotlib.pyplot as plt
from e_x import E_X
from path import Path
import numpy as np
# ==================================================================================
#Initialize Physical Stuff
# ==================================================================================
#Reaction Product energies (eV)
E_alpha_init = 2.0553e6
E_triton_init = 2.7276e6
#LLD (eV)
LLD = 100E3
#Physical characteristics of the materials
#Avogodros number (#/mol)
Avg = 6.022E23
#Densities in g/cm3
strut_density = 1.2
#Impregnation percent
percent_LiF = 1#0.045#0.275
Li_A = 6.941
F_A = 18.9984032
P = Li_A*.5 + F_A*.5
percent_Li = percent_LiF*Li_A*.5/P
#Microscopic Cross-section data in cm2
Li_micro_cs = 940E-24
Li_macro_cs = percent_Li*Avg*Li_micro_cs/Li_A #divided by density
#Macroscopic Cross-section data in cm-1
strut_macro_cs = strut_density*Li_macro_cs
# ==================================================================================
#Initialize Simulation Stuff
# ==================================================================================
#Energy deposition lists from the E_X class
E_X = E_X()
#Random Number Generator and relevant MC stuff
random = PM_RNG()
i = 0
N = 1E5
percent = N/100
#Various Counters
energy_dep = []
not_detected = 0
escaped = 0
strut_material = 0
pocket_material = 0
# ==================================================================================
#Conduct the MC Simulation
# ==================================================================================
while i < N:
    #Transport the neutron through the foam material to see if it interacts
    neutron = Path()
    #Neutron starts out having traveled 0 distance through the device    
    x = 0    
    #Initialize the interaction distance and strut thickness to get into the
    #neutron transport loop    
    d = 1
    D_strut = 0
    while d > D_strut and x <= neutron.maximum_length:
        # ==================================================================================        
        #Pocket        
        # ==================================================================================        
        #Calculate the diameter of the first pocket        
        D = neutron.create_pocket(random)
        #Determine the angle from tangent that the neutron passes through the circle        
        omega = random.New()
        r = D/2
        #Find the chord length of the neutron through the pocket
        D_pocket = math.fabs(2*r*math.sqrt(1 - omega*omega))  
        neutron.path.append(D_pocket)
        x += D_pocket
        # ==================================================================================
        #Strut
        # ==================================================================================        
        #Calculate the distance to the next interaction
        d = -(1/strut_macro_cs)*math.log(random.New())        
        #Find the thickness and width of the strut        
        (T, W) = neutron.create_strut(random)
        #Determine where along the width of the strut the neutron enters        
        I = random.New()*W/2
        #Determine the angle at which the neutron enters the strut
        omega = random.New()*2 - 1
        #If the neutron enters headed towards the center, change the axis around
        #to make that work out        
        if omega < 0:
            omega = omega*-1
            I = W - I
        #Determine the length of strut material the neutron will see as it travels
        #along theta through the strut
        theta = math.acos(omega)
        #Assume the neutron does not hit the side limits        
        D_strut = math.fabs(T/math.sin(theta))
        #Check to see if the neutron hits the side limits. If it does, change the
        #distance to account for this
        if D_strut*math.cos(theta) > I:
            D_strut = I/omega
        neutron.path.append(D_strut)
        x += D_strut
    #When d < the strut distance, the neutronis absorbed into the strut at distance d
    x += d
    if x > neutron.maximum_length:
        escaped += 1
    else:
        # ==================================================================================
        #Transport the reaction products
        # ==================================================================================
        #Initialize the reaction product paths
        alpha = Path()
        triton = Path()        
        #First, determine the distance to all of the sides of the strut
        x0 = W - I + D_strut*math.cos(theta)
        y0 = D_strut*math.sin(theta)
        psi1 = math.asin(T - y0)
        psi2 = math.pi - psi1
        psi3 = math.pi + math.asin(y0)
        psi4 = 2*math.pi - math.asin(y0)
        #Now, determine the ejection angle (relative to strut) for the alpha (and subsiquently the triton)
        psi_alpha = random.New()*2*math.pi
        psi_triton = psi_alpha + math.pi
        #Determine what ejection quadrant the alpha and triton are headed in order to
        #determine how much strut material they travel through before exiting into a pocket
        if psi1 <= psi_alpha and psi_alpha < psi2:
            y = T
            x = x0 + (T - y0)*math.tan(psi_alpha - math.pi/2)
            alpha_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
            y = 0
            x = x0 - y0*math.tan(psi_alpha - 3*math.pi/2)
            triton_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
        if psi2 <= psi_alpha and psi_alpha < psi3:
            y = y0 - I*math.tan(psi_alpha - math.pi)
            x = W
            alpha_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
            y = y0 + x0*math.tan(psi_alpha)
            x = 0
            triton_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
        if psi3 <= psi_alpha and psi_alpha < psi4:
            y = 0
            x = x0 - y0*math.tan(psi_alpha - 3*math.pi/2)
            alpha_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
            y = T
            x = x0 + (T - y0)*math.tan(psi_alpha - math.pi/2)
            triton_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
        if psi4 <= psi_alpha or psi_alpha < psi1:
            y = y0 + x0*math.tan(psi_alpha)
            x = 0
            alpha_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
            y = y0 - I*math.tan(psi_alpha - math.pi)
            x = W
            triton_first_strut = math.sqrt((x - x0)*(x - x0) + (y - y0)*(y - y0))
        #Determine the angle of the alpha and triton relative to the original neutron direction
        theta_alpha = theta + psi_alpha
        theta_triton = theta_alpha - math.pi
        #Determine the distance to the edge of the detector for the alpha and the triton
        if math.cos(theta_alpha) > 0:
            alpha.maximum_length = (alpha.maximum_length - x)/math.cos(theta_alpha)
            triton.maximum_length = -x/math.cos(theta_triton)
        else:
            alpha.maximum_length = -x/math.cos(theta_alpha)
            triton.maximum_length = (triton.maximum_length - x)/math.cos(theta_triton)
        # ==================================================================================
        #Charge deposition
        # ==================================================================================
        #Alpha first
        # ==================================================================================
        alpha_dist = 0
        E_alpha = E_alpha_init
        alpha_energy_dep = 0
        j = 0
        while E_alpha > 0 and alpha_dist < alpha.maximum_length:
            # ==================================================================================
            #In the strut
            # ==================================================================================            
            if j%2 == 0:
                #Determine how far into strut material the alpha would have had to travel in
                #order to have the same energy as E_alpha
                x0 = E_X.find_x_alpha_Strut(E_alpha)
                #Find the thickness and width of the strut        
                (T, W) = alpha.create_strut(random)
                #Determine where along the width of the strut the alpha enters        
                I = random.New()*W/2
                #Determine the angle at which the alpha enters the strut
                omega = random.New()*2 - 1
                #If the alpha enters headed towards the center, change the axis around
                #to make that work out        
                if omega < 0:
                    omega = omega*-1
                    I = W - I
                #Determine the length of strut material the alpha will see as it travels
                #along theta through the strut
                theta = math.acos(omega)
                #Assume the alpha does not hit the side limits        
                D_strut = T/math.sin(theta)
                #Check to see if the alpha hits the side limits. If it does, change the
                #distance to account for this
                if D_strut*math.cos(theta) > I:
                    D_strut = I/omega
                dx = D_strut
                x = x0 + dx
                #Determine how much energy an alpha entering strut material would have
                #after traveling a total distance x into the material. This is the same
                #as finding the new alpha energy after traveling through the strut
                E_alpha = E_X.find_E_alpha_Strut(x)
                alpha_dist += dx
                alpha.path.append(dx)
                j += 1
            # ==================================================================================
            #In Ar
            # ==================================================================================
            else:
                #Determine how far into argon the alpha would have had to travel in
                #order to have the same energy as E_alpha
                x0 = E_X.find_x_alpha_Ar(E_alpha)
                #Calculate the diameter of the first pocket        
                D = alpha.create_pocket(random)
                #Determine the angle from tangent that the alpha passes through the circle        
                omega = random.New()
                r = D/2
                #Find the chord length of the alpha through the pocket
                D_pocket = 2*r*math.sqrt(1 - omega*omega)
                dx = D_pocket
                x = x0 + dx
                #Determine the new alpha energy by the same method as for the strut
                E_alpha_new = E_X.find_E_alpha_Ar(x)
                #Record the change in alpha energy as energy deposited in argon
                alpha_energy_dep = alpha_energy_dep + E_alpha - E_alpha_new
                #Remember to change the alpha energy for the next step                
                E_alpha = E_alpha_new
                alpha_dist += dx
                alpha.path.append(dx)
        # ==================================================================================
        #Triton second
        # ==================================================================================
        triton_dist = 0
        E_triton = E_triton_init
        triton_energy_dep = 0
        j = 0
        while E_triton > 0 and triton_dist < triton.maximum_length:
            # ==================================================================================
            #In the strut
            # ==================================================================================            
            if j%2 == 0:
                #Determine how far into strut material the triton would have had to travel in
                #order to have the same energy as E_triton
                x0 = E_X.find_x_triton_Strut(E_triton)
                #Find the thickness and width of the strut        
                (T, W) = triton.create_strut(random)
                #Determine where along the width of the strut the triton enters        
                I = random.New()*W/2
                #Determine the angle at which the triton enters the strut
                omega = random.New()*2 - 1
                #If the triton enters headed towards the center, change the axis around
                #to make that work out        
                if omega < 0:
                    omega = omega*-1
                    I = W - I
                #Determine the length of strut material the triton will see as it travels
                #along theta through the strut
                theta = math.acos(omega)
                #Assume the triton does not hit the side limits        
                D_strut = T/math.sin(theta)
                #Check to see if the triton hits the side limits. If it does, change the
                #distance to account for this
                if D_strut*math.cos(theta) > I:
                    D_strut = I/omega
                dx = D_strut
                x = x0 + dx
                #Determine how much energy an triton entering strut material would have
                #after traveling a total distance x into the material. This is the same
                #as finding the new triton energy after traveling through the strut
                E_triton = E_X.find_E_triton_Strut(x)
                triton_dist += dx
                triton.path.append(dx)
                j += 1
            # ==================================================================================
            #In Ar
            # ==================================================================================
            else:
                #Determine how far into argon the triton would have had to travel in
                #order to have the same energy as E_triton
                x0 = E_X.find_x_triton_Ar(E_triton)
                #Calculate the diameter of the first pocket        
                D = triton.create_pocket(random)
                #Determine the angle from tangent that the triton passes through the circle        
                omega = random.New()
                r = D/2
                #Find the chord length of the triton through the pocket
                D_pocket = 2*r*math.sqrt(1 - omega*omega)
                dx = D_pocket
                x = x0 + dx
                #Determine the new triton energy by the same method as for the strut
                E_triton_new = E_X.find_E_triton_Ar(x)
                #Record the change in triton energy as energy deposited in argon
                triton_energy_dep = triton_energy_dep + E_triton - E_triton_new
                #Remember to change the triton energy for the next step                
                E_triton = E_triton_new
                triton_dist += dx
                triton.path.append(dx)
        # ==================================================================================
        #Finished with reaction product transport
        # ==================================================================================
        total_energy_dep = triton_energy_dep + alpha_energy_dep
        #See if the energy deposited in the Ar is above the LLD setting. If so, add the energy
        #to the energy_dep list (for the reaction product pulse height spectrum). If not, we
        #didn't detect this neutron, so not_detected counter gets increased
        if total_energy_dep >= LLD:
            energy_dep.append(total_energy_dep/1e6)
        else:
            not_detected += 1
    # ==================================================================================
    #Finished with this history... time to move to the next neutorn
    # ==================================================================================
    i += 1
    #Just printing out the progress in percent complete
    if i%percent == 0:
        print i/percent
#Printing the causes of neutrons which are not detected
#Some neutrons make it all the way through the detector without interacting (escaped)
print 'Escaped Neutrons:', escaped
#Some neutorns interact, but the reaction products do not deposit enough energy to be
#detected (below the LLD)
print 'Below LLD:', not_detected
# ==================================================================================
#Calculate Detector Efficiency
# ==================================================================================
detected = (N - not_detected - escaped)
detection_efficiency = detected/N*100
error = math.sqrt(detected)/N*100
print 'Detection Efficiency:', detection_efficiency, '+/-', error, '%'
font = {'family' : 'normal',
        'weight' : 'normal',
        'size' : 14}
plt.rc('font', **font)
plt.figure(1)
#plt.title('Reaction Product Pulse Height Spectrum 40% LiF Impregnated Foam 1in tube\n')
plt.xlabel('Reaction Product Energy Deposited in Gas Pores (MeV)')
plt.ylabel('Number of Histories')
plt.xlim(0, 4.8)
plt.hist(energy_dep,100)
np.savetxt("PHS.csv", energy_dep, delimiter=',')