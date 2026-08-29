from simulation import run_simulation           # importing simulation
from plotting import plotting_results           # importing plotting

results = run_simulation()                      # running simulation

plotting_results(*results)                      # plotting results from simulation

