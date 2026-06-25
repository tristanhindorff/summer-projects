import matplotlib.pyplot as plt                     # importing plot generator
import numpy as np

from data import Pc, Tc, gamma, R, At, Ae, Pa       # importing data and equations solvers
from nozzel import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

chamber_pressures = np.linspace(5e6, 30e6, 50)      # range and steps for the chamber pressure values
thrust_values = []                                  # thrust values produced

eps = area_ratio(Ae, At)                            # calculating the expansion ratio

for Pc in chamber_pressures:                        # calculating the thrust for the different chamber pressures
    Me = exit_mach(eps, gamma)
    Te = exit_temperature(Tc, gamma, Me)
    Pe = exit_pressure(Pc, Tc, Te, gamma)
    Ve = exit_velocity(gamma, R, Tc, Pe, Pc)
    mdot = mass_flow_rate(Pc, At, Tc, gamma, R)
    F = thrust(mdot, Ve, Pe, Pa, Ae)
    thrust_values.append(F)                         # storing the thrust values produced

plt.figure()                                        # creating figure and plotting the information

plt.plot(chamber_pressures/1e6, thrust_values)
plt.xlabel('Chamber Pressure (MPa)')
plt.ylabel('Thrust (n)')
plt.title('Chamber Pressure vs Thrust')
plt.grid(True)
plt.show()