from data import Pc, Tc, gamma, R, At, Ae, Pa               # importing data


def area_ratio(Ae, At):                                     # calculating the area ratio
    eps = Ae/At
    return eps

def exit_temperature(Tc, gamma, Me):                        # calculating the exit temperature
    Te = Tc/(1 + (gamma-1)/2*Me**2)
    return Te

def exit_pressure(Pc, Tc, Te, gamma):                       # calculating the exit pressure
    Pe = (Pc * (Te/Tc)**(gamma/(gamma-1))) / (1*10**6)
    return Pe

def exit_velocity(gamma, R, Tc, Pe, Pc):                    # calculating the exit velocity
    Ve = ((2*gamma*R*Tc/(gamma-1))*(1-(Pe/Pc)**((gamma-1)/gamma)))**0.5
    return Ve