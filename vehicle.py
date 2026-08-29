import data


mdot = data.thrust / (data.isp * data.g)                # calculation of mass flow rate (constant)

def vehicle_mass(time, initial_mass, dry_mass):         # calculation of vehicle mass over time
    if time <= data.burn_time:
        mass = data.initial_mass - mdot * time
    else:                                               # vehicle mass after burn time
        mass = data.dry_mass

    return mass