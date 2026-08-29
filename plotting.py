from data import gamma                          # importing constant gamma

import matplotlib.pyplot as plt                 # importing ploting function
import numpy as np
from atmosphere import temperature, pressure, density, mach             # importing calculators for atmosphere
from compressible_flow import temperature_ratio, pressure_ratio, area_ratio             # importing calculators for compressible flow
from aerobynamics import lift, drag, lift_to_drag               # importing calculators for aerodynamics
from orbital import circular_velocity, orbital_period                   # importing calculators from orbital 

def plot_atmosphere():                          # functions for atmosphere graphs 
    altitude = np.linspace(0, 20000, 200)          # values for altitude in the calculation

    temperature_output = []                 # temperatures calculated in loop for given altitude
    pressure_output = []                    # pressures calculated in loop for given altitude 
    density_output = []                     # densities calculated in loop for given altitude
    mach_output = []                        # speed of sound calculated in loop for given altitude

    for h in altitude:                      # calculations done in loop for altitude values 
        temperature_output.append(temperature(h))
        pressure_output.append(pressure(h))
        density_output.append(density(h))
        mach_output.append(mach(h))

    plt.figure()                            # plotting altitude and temperature graph 
    plt.plot(altitude, temperature_output)
    plt.title('Temperature vs Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Temperature (K)')
    plt.grid(True)

    plt.figure()                            # plotting altitude and pressure graph
    plt.plot(altitude, pressure_output)
    plt.title('Pressure vs Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Pressure (Pa)')
    plt.grid(True)

    plt.figure()                            # plotting altitude and density graph
    plt.plot(altitude, density_output)
    plt.title('Density vs Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Density (kg/m^3)')
    plt.grid(True)

    plt.figure()                            # plotting altitude and speed of sound graph
    plt.plot(altitude, mach_output)
    plt.title('Speed of Sound vs Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Speed of Sound (m/s)')
    plt.grid(True)

    plt.show()                              # showing plots generated 


def plot_flow():                            # function of generate graphs for compressible flow
    machs = np.linspace(0.1, 5, 500)        # mach values used in calculations 

    temperature_ratio_output = []           # storage functions for values generated in loop
    pressure_ratio_output = []
    area_ratio_output = []

    for mach in machs:                      # loop to calculate temperature, pressure and area ratios for graphing
        temperature_ratio_output.append(temperature_ratio(mach, gamma))
        pressure_ratio_output.append(pressure_ratio(mach, gamma))
        area_ratio_output.append(area_ratio(mach, gamma))

    plt.figure()                            # plotting mach number and pressure ratio
    plt.plot(machs, pressure_ratio_output)
    plt.title('Pressure Ratio vs Mach Number')
    plt.xlabel('Mach Number')
    plt.ylabel('Pressure Ratio')
    plt.grid(True)

    plt.figure()                            # plotting mach number and temperature ratio
    plt.plot(machs, temperature_ratio_output)
    plt.title('Temperature Ratio vs Mach Number')
    plt.xlabel('Mach Number')
    plt.ylabel('Temperature Ratio')
    plt.grid(True)

    plt.figure()                            # plotting mach number and area ratio
    plt.plot(machs, area_ratio_output)
    plt.title('Area Ratio vs Mach Number')
    plt.xlabel('Mach Number')
    plt.ylabel('Area Ratio')
    plt.grid(True)

    plt.show()                              # showing plots generated 



def aero_perfromance():                     # aerodynamics graphing function
    velocities = np.linspace(10, 300, 200)  # velocity values used in calculations 

    lift_output = []                        # storage for values generated in calculations 
    drag_output = []
    ratio_output = []

    rho = float(input('Air Density (kg/m^3): '))        # input for air density in calculations 
    area = float(input('Reference Area (m^2): '))       # input for reference area in calculations 
    cl = float(input('Lift Coefficient: '))             # input for lift coefficient in calculations
    cd = float(input('Drag Coefficient: '))             # input for drag coefficient in calculations 

    for vel in velocities:                              # loop for calculations for lift, drag and ratio based on different velocities
        
        lift_output.append(lift(rho, vel, area, cl))
        drag_output.append(drag(rho, vel, area, cd))
        ratio_output.append(lift_to_drag(cl, cd))

    plt.figure()                            # plotting velocity and lift output 
    plt.plot(velocities, lift_output)
    plt.title('Lift vs Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Lift (N)')
    plt.grid(True)

    plt.figure()                            # plotting velocity and drag output
    plt.plot(velocities, drag_output)
    plt.title('Drag vs Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Drag (N)')
    plt.grid(True)

    plt.figure()                            # plotting velocity and ratio output
    plt.plot(velocities, ratio_output)
    plt.title('Lift-to-Drag Ratio vs Velocity')
    plt.xlabel('Velocity (m/s)')
    plt.ylabel('Lift-to-Drag Ratio')
    plt.grid(True)

    plt.show()                              # showing plotting generated 


def orbital_plotting():                     # function for plotting orbital relationships 
    altitude_values = np.linspace(0, 1000000, 500)              # altitude values used in calculations 

    velocity_output = []                    # storage for velocity values generated
    period_output = []                      # storage for period values generated

    for altitude in altitude_values:        # loop for calculating velocity and period values based on altitude 
        velocity_output.append(circular_velocity(altitude))
        period_output.append(orbital_period(altitude))

    plt.figure()                            # plotting altitude and velocity
    plt.plot(altitude_values, velocity_output)
    plt.title('Circular Orbital Velocity vs. Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.figure()                            # plotting altiude and period
    plt.plot(altitude_values, period_output)
    plt.title('Orbital Period vs Altitude')
    plt.xlabel('Altitude (m)')
    plt.ylabel('Orbital Period (s)')
    plt.grid(True)

    plt.show()                              # showing graphs plotted