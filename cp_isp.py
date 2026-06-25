import matplotlib.pyplot as plt                                 # importing plotting and solvers
import numpy as np

from data import Pc, Tc, gamma, R, At, Ae, Pa                   # importing data and equation outputs
from nozzel import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

chamber_pressures = np.linspace(5e6, 30e6, 50)              # establishing the data range and step for the chamber pressure
isp_output = []                                             #isp output based on the chamber pressures

eps = area_ratio(Ae, At)                                    # calculating the area ratio 

for Pc in chamber_pressures:                                # loop for calculating the isp for all values of chamber pressure
    Me = exit_mach(eps, gamma)
    Te = exit_temperature(Tc, gamma, Me)
    Pe = exit_pressure(Pc, Tc, Te, gamma)
    Ve = exit_velocity(gamma, R, Tc, Pe, Pc)
    mdot = mass_flow_rate(Pc, At, Tc, gamma, R)
    F = thrust(mdot, Ve, Pe, Pa, Ae)
    Isp = isp(F, mdot)
    isp_output.append(Isp)                                  # stores output for isp

plt.figure()                                                # creates the comparitive plot

plt.plot(chamber_pressures/1e6, isp_output)
plt.xlabel('Chamber Pressure (MPa)')
plt.ylabel('ISP')
plt.title('Chamber Pressure vs ISP')
plt.grid(True)
plt.show()