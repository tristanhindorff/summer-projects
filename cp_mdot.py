import matplotlib.pyplot as plt                     # import function generators
import numpy as np

from data import Pc, Tc, gamma, R, At, Ae, Pa       # import data and equations 
from nozzle import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

chamber_pressures = np.linspace(5e6, 30e6, 50)       # range and jumps for chamber pressure used in equations 
mass_flow = []                                       # mass flow rate output generated

for Pc in chamber_pressures:                        # calculating mass flow based on chamber pressure 
    mdot = mass_flow_rate(Pc, At, Tc, gamma, R)
    mass_flow.append(mdot)

plt.figure()                                        # creating plot with data line 

plt.plot(chamber_pressures/1e6, mass_flow)
plt.xlabel('Chamber Pressure (MPa)')
plt.ylabel('Mass Flow Rate (kg/s)')
plt.title('Chamber Pressure vs Mass Flow')
plt.grid(True)
plt.show()