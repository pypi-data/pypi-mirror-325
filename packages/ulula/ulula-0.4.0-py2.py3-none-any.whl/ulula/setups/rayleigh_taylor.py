###################################################################################################
#
# This file is part of the ULULA code.
#
# (c) Benedikt Diemer, University of Maryland
#
###################################################################################################

import numpy as np

import ulula.core.setup_base as setup_base

###################################################################################################

class SetupRayleighTaylor(setup_base.Setup):
    """
    Rayleigh-Taylor instability

    A denser fluid sits on top of a less dense fluid, but as the boundary is perturbed, a well-
    known mushroom-like structure forms. In the default setup, the top of the cold mushroom 
    structure forms its own Rayleigh-Taylor instability as it rises. This setup demonstrates:
    
    * Fixed-acceleration gravity in 2D with wall boundary conditions
    * Instabilities at a two-fluid interface.

    Parameters
    ----------
    n_waves: float
        The number of wave periods by which the boundary between fluids is perturbed.
    aspect_ratio: float
        The ratio of y to x extent of the domain.
    unit_l: float
        Code unit for length in units of centimeters.
    unit_t: float
        Code unit for time in units of seconds.
    unit_m: float
        Code unit for mass in units of gram.
    """
    
    def __init__(self, n_waves = 0.5, aspect_ratio = 3.0, unit_l = 1.0, unit_t = 1.0, unit_m = 1.0):

        setup_base.Setup.__init__(self, unit_l = unit_l, unit_t = unit_t, unit_m = unit_m)
        
        self.aspect_ratio = aspect_ratio
        self.rho_up = 2.0
        self.rho_dn = 1.0
        self.P0 = 2.5
        self.g = 1.0
        self.n_waves = n_waves
        self.delta_y =  0.05
        self.delta_vy =  0.1

        return

    # ---------------------------------------------------------------------------------------------

    def shortName(self):
        
        return 'rt'

    # ---------------------------------------------------------------------------------------------
    
    def setInitialData(self, sim, nx):
        
        sim.setGravityMode(gravity_mode = 'fixed_acc', g = self.g)
        sim.setDomain(nx, int(nx * self.aspect_ratio), xmin = 0.0, xmax = 1.0 / self.aspect_ratio, 
                      ymin = 0.0, bc_type = 'wall')

        DN = sim.q_prim['DN']
        VX = sim.q_prim['VX']
        VY = sim.q_prim['VY']
        PR = sim.q_prim['PR']
        
        # Sine wave in y-velocity
        x, y = sim.xyGrid()
        vy = self.delta_vy * np.sin(2.0 * np.pi * x * self.n_waves * self.aspect_ratio) \
                * np.exp(-0.5 * (y - 0.5)**2 / self.delta_y**2)

        # Set the pressure to increase towards the bottom to avoid some of the resulting shock waves
        sim.V[DN][y > 0.5] = self.rho_up
        sim.V[DN][y <= 0.5] = self.rho_dn
        sim.V[VX] = 0.0
        sim.V[VY] = vy
        sim.V[PR] = self.P0 + self.g * (1.0 - y) * self.rho_dn
    
        return
    
    # ---------------------------------------------------------------------------------------------

    def plotLimits(self, q_plot):
        
        vmin = []
        vmax = []

        for q in q_plot:
            if q == 'DN':
                vmin.append(self.rho_dn * 0.9)
                vmax.append(self.rho_up * 1.1)
            elif q in ['VX', 'VY']:
                vmin.append(-0.6)
                vmax.append(0.6)
            elif q == 'PR':
                vmin.append(self.P0 * 0.7)
                vmax.append(self.P0 * 1.3)
            else:
                vmin.append(None)
                vmax.append(None)
        
        return vmin, vmax, None

###################################################################################################
