import matplotlib.pyplot as plt             # importing plotting libary
from simulation import run_simulation       # importing simulation data and function


def plotting_results(time, altitude, velocity, acceleration, mass, dynamic_pressure):
    

    plt.figure()                            # plot for time and altitude
    plt.plot(time, altitude)
    plt.title('Altitude vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (m)')
    plt.grid(True)

    plt.figure()                            # plot for time and velocity
    plt.plot(time, velocity)
    plt.title('Velocity vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.grid(True)

    plt.figure()                            # plot for time and acceleration
    plt.plot(time, acceleration)
    plt.title('Acceleration vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s^2)')
    plt.grid(True)

    plt.figure()                            # plot for time and mass
    plt.plot(time, mass)
    plt.title('Mass vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Mass (Kg)')
    plt.grid(True)

    plt.figure()                            # plot for time and dynamic pressure
    plt.plot(time, dynamic_pressure)
    plt.title('Dynamic Pressure vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Dynamic Pressure (Pa)')
    plt.grid(True)

    plt.show()                              # showing all plots created