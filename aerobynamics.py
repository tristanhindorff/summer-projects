def dynamic_pressure(rho, velocity):                # function for calculating dynamic pressure 
    q = 0.5 * rho * velocity**2                     # calculating dynalic pressure 
    return q

def lift(rho, velocity, area, cl):                  # function for calculating lift 
    q = dynamic_pressure(rho, velocity)             # calculating dynamic pressure for lift 
    L = q * area * cl                               # calculating lift 
    return L

def drag(rho, velocity, area, cd):                  # function for calculating drag 
    q = dynamic_pressure(rho, velocity)             # calculating dynamic pressure for drag
    D = q * area * cd                               # calculating drag 
    return D

def reynolds_number(rho, velocity, lenght, mu):     # function for calculate reynolds number 
    Re = (rho * velocity * lenght) / mu             # calculating reynolds number 
    return Re

def lift_to_drag(cl, cd):                           # function to calculate lift to drag ratio
    L_D = cl / cd                                   # calculating lift to drag ratio 
    return L_D

