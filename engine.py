from data import Pc, Tc, gamma, R, At, Ae, Pa           # importing data
g = 9.81                                                # value for acceleration due to gravity


def mass_flow_rate(Pc, At, Tc, gamma, R):               # function for solving mass flow rate
    mdot = (Pc*At/(Tc**0.5))*((gamma/R)*(2/(gamma + 1))**((gamma + 1)/(gamma - 1)))**0.5
    return mdot

def thrust(mdot, Ve, Pe, Pa, Ae):                       # function for solving thrust
    F = mdot*Ve + (Pe - Pa)*Ae
    return F

def isp(F, mdot):                                       # function for solving isp
    isp = F / (mdot*g)
    return isp