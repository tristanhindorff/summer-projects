from scipy.optimize import fsolve               # importing equation solver
from nozzel import area_ratio                   # importing equations and data
from data import At, gamma, Ae

eps = area_ratio(Ae, At)                        # calculating the expansion ratio

def area_mach_relation(Me, gamma, eps):         # calculating the area mach relations number in response to expansion ratio
    rhs = (1/Me) * (2/(gamma + 1) * (1 + ((gamma-1)/2) * Me**2))**((gamma + 1)/(2*(gamma - 1)))
    return eps - rhs

def exit_mach(eps, gamma):                       # calculating the exit mach number using fsolve
    Me_guess = 3.0
    solution = fsolve(
        area_mach_relation,
        Me_guess,
        args=(gamma, eps)
    )

    return solution[0]

