from data import Pc, Tc, gamma, R, At, Ae, Pa               # importing the data and equations 
from nozzle import area_ratio, exit_temperature, exit_pressure, exit_velocity
from mnum import exit_mach
from engine import mass_flow_rate, thrust, isp

eps = area_ratio(Ae, At)                                    # calculating the output values based on the given data
Me = exit_mach(eps, gamma)
Te = exit_temperature(Tc, gamma, Me)
Pe = exit_pressure(Pc, Tc, Te, gamma)
Ve = exit_velocity(gamma, R, Tc, Pe, Pc)
mdot = mass_flow_rate(Pc, At, Tc, gamma, R)
F = thrust(mdot, Ve, Pe, Pa, Ae)
Isp = isp(F, mdot)

print('expansion ratio = ', eps)                            # printing the values calculated with units
print('exit mach number = ', round(Me, 3))
print(f'exit temperature = {Te:.1f} K')
print(f'exit pressure = {Pe:.3f} MPa')
print(f'exit velocity = {Ve:.3f} m/s')
print(f'mass flow rate = {mdot:.2f} kg/s')
print(f'thrust = {F:.2f} N')
print(f'specific impulse = {Isp:.2f} s')