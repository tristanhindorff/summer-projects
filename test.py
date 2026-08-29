from vehicle import vehicle_mass            # test function
import data

for t in [135]:
    print(f'Time = {t:3} s  Mass = {vehicle_mass(t, data.dry_mass, data.initial_mass):0.2f} kg')
