import data                         
import math

def gravity_force(mass):                # calculating the froce of gravity
    Fg = mass * data.g

    return Fg

def thrust_force(time):                 # thrust determined by time
    if time <= data.burn_time:
        Ft = data.thrust
    else:
        Ft = 0
    return Ft

def reference_area():                       # reference area for the vehicle
    A = math.pi *(data.diameter / 2)**2
    return A

def drag_force(rho, velocity):              # calculations of drag force
    A = reference_area()
    if velocity >= 0:                       # drag going up
        Fd = 0.5 * rho * velocity**2 * data.Cd * A
    else:                                               # drag coming down
        Fd = -0.5 * rho * velocity**2 * data.Cd * A

    return Fd

def net_force(time, mass, rho, velocity):           # sum of forces acting on the vehicle
    Ft = thrust_force(time)
    Fg = gravity_force(mass)
    Fd = drag_force(rho, velocity)
    Fnet = Ft - Fg - Fd
    return Fnet

def acceleration(Fnet, mass):                       # calculation of acceleration
    a = Fnet / mass
    return a


def dynamic_pressure(rho, velocity):                # calculation of dynamic pressure
    q = 0.5 * rho *velocity**2
    return q



