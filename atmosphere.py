import data
import math

def air_density(altitude):                      # calculation equation for the changing atmospheric density

    rho = data.rho * math.exp(-altitude / 8500)

    return rho