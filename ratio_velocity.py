import matplotlib.pyplot as plt                 # importing plotting function
import numpy as np

from data import Pc, Tc, gamma, R, At, Pa       # importing data and equations
from nozzle import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

expansion_ratio = np.linspace(5, 100)           # expansion ratios values and steps
v_exit = []                                     # exit velocity based on expansion ratio


for eps in expansion_ratio:                     # calculation of exit velocity based on expansion ratio
    Me = exit_mach(eps, gamma)
    Te = exit_temperature(Tc, gamma, Me)
    Ae = At * eps
    Pe = exit_pressure(Pc, Tc, Te, gamma)
    Ve = exit_velocity(gamma, R, Tc, Pe, Pc)

    v_exit.append(Ve)

plt.figure()                                    # plotting the graph of the comparison

plt.plot(expansion_ratio, v_exit)
plt.xlabel('Expansion Ratio')
plt.ylabel('Exit Velocity (m/s)')
plt.title('Expansion Ratio vs Exit Velocity')
plt.grid(True)
plt.show()