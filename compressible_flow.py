import numpy 

def temperature_ratio(mach, gamma):                 # function to calculate temperature ratio
    Tr = 1 / (1 + ((gamma - 1) / 2) * mach**2)      # calculating temperature ratio
    return Tr

def pressure_ratio(mach, gamma):                    # function to calculate pressure ratio
    Tr = temperature_ratio(mach, gamma)             # calculating temperature ratio for pressure ratio
    Pr = Tr**(gamma / (gamma - 1))                  # calculating pressure ratio
    return Pr

def density_ratio(mach, gamma):                     # function to calculate density ratio
    Tr = temperature_ratio(mach, gamma)             # calculating temperature ratio for density ratio
    Dr = Tr**(1 / (gamma - 1))                      # calculating density ratio 
    return Dr

def stag_temperature(mach, temp, gamma):            # function to calculate the stagnation temperature
    Tr = temperature_ratio(mach, gamma)             # calculating temperature ratio for stagnation temperature
    To = temp / Tr                                  # calculating stagnation temperature
    return To

def stag_pressure(mach, pressure, gamma):           # function to calculate stagnation pressure 
    Pr = pressure_ratio(mach, gamma)                # calculating pressure ratio for stagnation pressure 
    Po = pressure / Pr                              # calculating stagnation pressure
    return Po   

def area_ratio(mach, gamma):                        # function to calculate area ratio 
    Ar = ((1 / mach) * ((2 / (gamma + 1)) * (1 + ((gamma - 1) / 2) * mach**2))**((gamma + 1) / (2 * (gamma - 1))))
    return Ar

def mach_angle(mach):                               # function to calculate the mach angle 
    if mach > 1:                                    # calculating angle if mach is greater than 1 
        miu = numpy.arcsin(1 / mach)                # calculating mach angle 
        return miu
    else:                                           # if mach is less than 1 
        return None