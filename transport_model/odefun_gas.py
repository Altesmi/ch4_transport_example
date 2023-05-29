import numpy as np


def odefun_gas(t: float, y: np.ndarray, gas) -> np.ndarray:  # pylint: disable=unused-argument
    ''' The right hand sides of ODEs used in the gas module. '''

    # Set the new molar amount of compound from y
    gas.n_in = y[:gas.nr*gas.na*2].reshape(gas.na, gas.nr, 2, order='F')
    # Transport fluxes (mol/s)
    Q_aq_ax_advection = gas.aq_axial_advection()
    Q_gas_rad_diffusion, Q_gas_rad_diffusion_out, _ = gas.gas_radial_diffusion()
    Q_air_water = gas.air_water_fluxes()
    Q_gas_ax_diffusion, Q_gas_ax_diffusion_top, Q_gas_ax_diffusion_bottom = gas.gas_axial_diffusion()

    # Source from user defined source and sink matrix (mol/s)
    R = gas.sources_and_sinks

    # Source from root water uptake (mol/s)
    R_root = gas.axial_water_uptake_source()

    # RHS of derivatives
    dndt_air = (Q_gas_rad_diffusion + R[:, :, 0] + R_root[:, :, 0] + Q_air_water[:, :, 0] + Q_gas_ax_diffusion)
    dndt_water = (Q_aq_ax_advection + R[:, :, 1] + R_root[:, :, 1] + Q_air_water[:, :, 1])

    # Calculate outgoing flux (mol/s)
    dndt_out = -1.0 * (np.minimum(0, Q_gas_rad_diffusion_out[:, -1]))
    # Add bottom and top fluxes through axial diffusion
    dndt_out[0] = dndt_out[0] + (-1.0 * np.sum(np.minimum(0, Q_gas_ax_diffusion_top[0, :])))
    dndt_out[-1] = dndt_out[-1] + (-1.0 * np.sum(np.minimum(0, Q_gas_ax_diffusion_bottom[-1, :])))


    # Assemble 1D array as a return value (required by solve_ivp)
    dydt = np.concatenate([dndt_air.reshape(gas.na*gas.nr, order='F'),
                           dndt_water.reshape(gas.na*gas.nr, order='F'),
                           dndt_out.reshape(gas.na, order='F')])
    return dydt
