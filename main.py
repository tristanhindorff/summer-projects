from interface import main_menu, atmosphere_menu, compressible_flow_menu, aerodyanmics_menu, orbital_menu               # importing interfaces with options 
import data                                                 # improting  data constants                             
import atmosphere                                           # importing atmosphere calculations  
import plotting                                             # improting plotting functions 
import compressible_flow                                    # importing compressible flow calculations 
import aerobynamics                                         # importing aerodynamics calculations 
import orbital                                              # importing orbital calculations 


def main():                                                 # main menu for tool kit 
    while True:                                             # loop to stay in function until broken
        choice = main_menu()                                # input to select menu type 

        if choice == '1':                                   # menu for atmosphere functions 
            while True:                                     # loop to stay in atmosphere menu 
                user_choice = atmosphere_menu()             # selection for menu function 
                if user_choice == '1':                      # for calculations, altitude input and calculated results printed 
                    altitude = float(input('Altitude(m): '))
                    print(f'Temperature: {atmosphere.temperature(altitude):.2f} K')
                    print(f'Pressure: {atmosphere.pressure(altitude):.2f} Pa')
                    print(f'Density: {atmosphere.density(altitude):.2f} kg/m³')
                    print(f'Speed of Sound: {atmosphere.mach(altitude):.2f} m/s')

                elif user_choice == '2':                    # plotting and showing altitude graphs 
                    plotting.plot_atmosphere()
                
                elif user_choice == '3':                    # exit atmosphere menu 
                    break
                else:                                       # failsafe to stay in loop 
                    print('Invalid response')
                
        elif choice == '2':                                 # menu for compressible flow functions 
            while True:                                     # loop to stay in compressible flow menu
                user_choice = compressible_flow_menu()      # input to select menu type
                if user_choice == '1':                      # for calculations in menu, inputs needed and outputs printed  
                    mach = float(input('Mach Number: '))
                    temp = float(input('Static Temperature (K): '))
                    pressure = float(input('Static Pressure (Pa): '))
                    print(f'Temperature Ratio: {compressible_flow.temperature_ratio(mach, data.gamma):.2f}')
                    print(f'Pressure Ratio: {compressible_flow.pressure_ratio(mach, data.gamma):.2f}')
                    print(f'Density Ratio: {compressible_flow.density_ratio(mach, data.gamma):.2f}')
                    print(f'Stagnation Temperature: {compressible_flow.stag_temperature(mach, temp, data.gamma):.2f} K')
                    print(f'Stagnation Pressure: {compressible_flow.stag_pressure(mach, pressure, data.gamma):.2f} Pa')
                    print(f'Area Ratio: {compressible_flow.area_ratio(mach, data.gamma):.2f}')
                    print(f'Mach Angle: {compressible_flow.mach_angle(mach):.2f} rad')
                elif user_choice == '2':                    # plotting and showing flow graphs 
                    plotting.plot_flow()
                elif user_choice == '3':                    # exit compressible flow menu
                    break
                else:                                       # failsafe to stay in loop 
                    print('Invalid response')

        elif choice == '3':                                 # aerodyanamic function 
            while True:                                     # loop to stay in aerodynamics menu 
                user_choice = aerodyanmics_menu()           # input to select menu type 
                if user_choice == '1':                      # for calculations, inputs and outputs printed 
                    rho = float(input('Air Density (kg/m^3): '))
                    velocity = float(input('Velocity (m/s): '))
                    area = float(input('Reference Area (m^2): '))
                    cl = float(input('Lift Coefficient: '))
                    cd = float(input('Drag Coefficient: '))
                    length = float(input('Characteristic Length (m): '))
                    mu = float(input('Dynamic Viscosity (Pa*s): '))

                    print(f'Dynamic Pressure: {aerobynamics.dynamic_pressure(rho, velocity):.2f} Pa')
                    print(f'Lift: {aerobynamics.lift(rho, velocity, area, cl):.2f} N')
                    print(f'Drag: {aerobynamics.drag(rho, velocity, area, cd):.2f} N')
                    print(f'Reynolds Number: {aerobynamics.reynolds_number(rho, velocity, length, mu):.2e}')
                    print(f'Lift-to-Drag Ratio: {aerobynamics.lift_to_drag(cl, cd):.2f}')
                elif user_choice == '2':                    # plotting and showing aerodynamic graphs 
                    plotting.aero_perfromance()
                elif user_choice == '3':                    # exit aerodynamics menu
                    break
                else:                                       # failsafe to stay in loop 
                    print('Invalid response')


        elif choice == '4':                                 # orbital mechanics function 
            while True:                                     # loop to stay in function 
                user_choice = orbital_menu()                # input to select menu type 
                if user_choice == '1':                      # calculating orbital velocity based on altitude given, printing result 
                    altitude = float(input('Altitude (m): '))
                    print(f'Orbital Velocity: {orbital.circular_velocity(altitude)} m/s')
                elif user_choice == '2':                    # calculating escape velocity based on altitude given, printing result
                    altitude = float(input('Altitude (m): '))
                    print(f'Escape Velocity: {orbital.escape_velocity(altitude)} m/s')
                elif user_choice == '3':                    # calculating orbital period based on altitude ginen, printing result 
                    altitude = float(input('Altitude (m): '))
                    print(f'Orbital Period: {orbital.orbital_period(altitude)} s')
                elif user_choice == '4':                    # calculating Hohmann transfer based of the altitude inputs, printing results 
                    altitude_1 = float(input('Initial Altitude (m): '))
                    altitude_2 = float(input('Final Altitude (m): '))
                    delta_v1, delta_v2, total_delta_v = orbital.hohmann_transfer(altitude_1, altitude_2)
                    print(f'Burn 1 delta V: {delta_v1} m/s')
                    print(f'Burn 2 delta V: {delta_v2} m/s')
                    print(f'Total delta V: {total_delta_v} m/s')
                elif user_choice == '5':                    # plotting orbital functions 
                    plotting.orbital_plotting()
                elif user_choice == '6':                    # exiting orbital menu 
                    break
                else:                                       # failsafe to stay in loop 
                    print('Invalid Response')


        elif choice == '5':                                 # exiting main menu 
            print('Goodbye!')
            break

        else:                                               # failsafe to stay in menu in case of invalid response
            print('Invalid response')

if __name__ == '__main__':                                  # running aerospace perfromance toolkit
    main()
