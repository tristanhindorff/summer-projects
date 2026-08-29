#ambiant pressure is zero since engine is optimzed for space opperations 

import matplotlib.pyplot as plt                 # importing the plot generator
import numpy as np

from data import Pc, Tc, gamma, R, At, Pa       # importing data and equations to solve 
from nozzle import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

expansion_ratio = np.linspace(5, 100)           # expansion ratio range used in calculations
thrust_output = []                              # storage for the output produced based on ratio


for eps in expansion_ratio:                     # loop for all all values of the expansion ratio and storage for the thrust output
    Me = exit_mach(eps, gamma)
    Te = exit_temperature(Tc, gamma, Me)
    Ae = At * eps
    Pe = exit_pressure(Pc, Tc, Te, gamma)
    Ve = exit_velocity(gamma, R, Tc, Pe, Pc)
    mdot = mass_flow_rate(Pc, At, Tc, gamma, R)
    F = thrust(mdot, Ve, Pe, Pa, Ae)
    thrust_output.append(F)

max_thrust = max(thrust_output)                # finding max thrust
max_index = thrust_output.index(max_thrust)
best_eps = expansion_ratio[max_index]          # finding best expansion ratio based on max thrust

plt.figure()                                   # plotting the generating the figure with thrust point

plt.plot(expansion_ratio, thrust_output)
plt.scatter(best_eps, max_thrust)
plt.xlabel('Expansion Ratio')
plt.ylabel('Thrust (N)')
plt.title('Expansion Ratio vs Thrust')
plt.annotate(f'Optimun\n = {best_eps:0.1f}', (best_eps, max_thrust))
plt.grid(True)
plt.show()


print('Optimization Results:')                  # printing the results for max thrust and optimal expansion ratio
print(f'Maximum Thrust = {max_thrust:.0f} N')
print(f'Optimal Expansion Ratio = {best_eps:.2f}')