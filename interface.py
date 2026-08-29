def main_menu():                                            # function for main menu of interface
    print('\n===============================================')
    print('       AEROSPACE PERFROMANCE TOOLKIT     ')
    print('===============================================')
    print('1. Standard Atmosphere Module')
    print('2. Compressible Flow Module')
    print('3. Aerodynamics Module')
    print('4. Orbital Mechanics Module')
    print('5. Exit')
    print('===============================================')

    choice = input('Select Modulel: ')                      # selection choice from menu 

    return choice

def atmosphere_menu():                                      # function for the atmosphere menu 
    print('\n=============================')
    print('STANDARD ATMOSPHERE')
    print('=============================')
    print('1. Calculate Properties')
    print('2. Plot Atmosphere')
    print('3. Return to Main Menu')

    choice = input('Select Option: ')                       # selection choice from menu 

    return choice

def compressible_flow_menu():                               # function for the compressible flow menu
    print('\n=============================')
    print('COMPRESSIBLE FLOW')
    print('=============================')
    print('1. Calculate Flow Properties')
    print('2. Plot Isentropic Relations')
    print('3. Return to Main Menu')

    choice = input('Select Option: ')                       # selection choice from menu 

    return choice

def aerodyanmics_menu():                                    # function for aerodynamics menu 
    print('\n=============================')
    print('AERODYNAMICS')
    print('=============================')
    print('1. Calculate Aerodynamic Properties')
    print('2. Plot Aerodynamic Performance')
    print('3. Return to Main Menu')

    choice = input('Select Option: ')                       # selection choice from menu 

    return choice

def orbital_menu():                                         # fucntion for orbital menu 
    print('\n=============================')
    print('ORBITAL MECHANICS')
    print('=============================')
    print('1. Circular Orbital Velocity')
    print('2. Escape Velocity')
    print('3. Orbital Period')
    print('4. Hohmann Transer')
    print('5. Plot Orbital Properties')
    print('6. Return to main menu')

    choice = input('Select Option: ')                       # selection choice from menu 
    return choice