import data
from vehicle import vehicle_mass                    # importing equations and functions
from forces import net_force, acceleration, dynamic_pressure
from atmosphere import air_density

def run_simulation():   
    time = 0.0                      # initial values for the simulation
    altitude = 0.0
    velocity = 0.0

    time_history = []                   # storages for the output values produced
    altitude_history = []
    velocity_history = []
    acceleration_history = []
    mass_history = []
    dynamic_pressure_history = []

    while altitude >= 0 and time <= 700:            # calculation of values given period of time and height

        rho = air_density(altitude)                 # calculation of rho (changing)

        mass = vehicle_mass(time, data.initial_mass, data.dry_mass)
        Fnet = net_force(time, mass, rho, velocity)
        a = acceleration(Fnet, mass)
        velocity = velocity + a*data.dt
        altitude = altitude + velocity*data.dt
        time = time + data.dt
        q = dynamic_pressure(rho, velocity)
        time_history.append(time)                               # storing calculated values into lists for plotting
        altitude_history.append(altitude)
        velocity_history.append(velocity)
        acceleration_history.append(a)
        mass_history.append(mass)
        dynamic_pressure_history.append(q)
    return(time_history, altitude_history, velocity_history, acceleration_history, mass_history, dynamic_pressure_history)
