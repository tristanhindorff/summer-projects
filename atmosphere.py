import data                                 # importing data constants 

def temperature(altitude):                  # function for calculating temperature 
    T = data.To - data.L * altitude         # calculating temperature based on altitude 
    return T

def pressure(altitude):                     # function for calculating pressure 
    T = temperature(altitude)               # calculating temperature for pressure
    P = data.Po * (T / data.To)**(data.g / (data.L * data.R))       # calculating pressure based on altitude
    return P

def density(altitude):                      # function for calculating density 
    T = temperature(altitude)               # calculaing temperature for density 
    P = pressure(altitude)                  # calculating pressure for density 
    rho = P / (data.R * T)                  # calculating density based on altitude
    return rho

def mach(altitude):                         # function for calculating the speed of sound 
    T = temperature(altitude)               # calculating temperature for mach number 
    a = (data.lamda * data.R * T)**0.5      # calculating speed of sounds based on altitude 
    return a