from data import G, R_earth, mu                     # importing constant values 
import math                                         # inporting math functions

def circular_velocity(altitude):                    # function for calculating circular velocity
    r = R_earth + altitude                          # calculating radius based on altitude 
    velocity = (mu / r)**0.5                        # calculating circular velocity
    return velocity                                 

def escape_velocity(altitude):                      # function for calculating escape velocoity
    r = R_earth + altitude                          # calculating radius based on altitude 
    velocity = (2 * mu / r)**0.5                    # calculating escape velocity
    return velocity

def orbital_period(altitude):                       # function for calculating orbital period
    r = R_earth + altitude                          # calculating raduis based on altitude 
    period = 2 * math.pi * (r**3 / mu)**0.5         # calculating orbital period 
    return period

def hohmann_transfer(altitude_1, altitude_2):       # function for calculating Hohmann transfer
    r1 = R_earth + altitude_1                       # calculating first radius 
    r2 = R_earth + altitude_2                       # culculating second radius 

    v1 = circular_velocity(altitude_1)              # calculating first orbital velocity
    v2 = circular_velocity(altitude_2)              # calculating second orbital velocity

    transfer_v1 = (mu / r1)**0.5 * (2 * r2 / (r1 + r2))**0.5        # calculating first transfer velocity 
    transfer_v2 = (mu / r2)**0.5 * (2 * r1 / (r1 + r2))**0.5        # calculating second transfer velocity

    delta_v1 = abs(transfer_v1 - v1)                # calculating change in first velocity
    delta_v2 = abs(v2 - transfer_v2)                # calculating change in second velocity 

    total_delta_v = delta_v1 + delta_v2             # total change in velocity 

    return delta_v1, delta_v2, total_delta_v
