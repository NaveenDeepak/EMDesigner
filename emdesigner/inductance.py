# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/07_inductance.ipynb.

# %% auto 0
__all__ = ['end_turn']

# %% ../nbs/07_inductance.ipynb 3
import numpy as np
from . import stator, rotor

# %% ../nbs/07_inductance.ipynb 8
def end_turn(motor_data):
    ns = motor_data.slots
    mu0 = 4*np.pi*1e-7
    theta_p = 2*np.pi/ns
    R_si = motor_data.outerdiameter
    tau_p = R_si*theta_p
    Nspp = ns/10/3
    alpha_cp = int(Nspp)/Nspp
    tau_c = alpha_cp*tau_p
    Le = (ns**2)*mu0*motor_data.stator.params['t_c']
    return 'yet to be included'
