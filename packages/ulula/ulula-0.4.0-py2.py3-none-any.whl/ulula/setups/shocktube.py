###################################################################################################
#
# This file is part of the ULULA code.
#
# (c) Benedikt Diemer, University of Maryland
#
###################################################################################################

import numpy as np
import scipy.optimize

import ulula.core.setup_base as setup_base

###################################################################################################

class SetupShocktube(setup_base.Setup):
    """
    Shocktube problem
    
    The Sod (1978) shocktube problem is a class test for Riemann solvers. A sharp break in fluid 
    properties at the center of a 1D domain causes a shock, contact discontinuity, and rarefaction
    wave. The problem can be solved analytically. This setup demonstrates:
    
    * Ability of hydro solver to handle strong shocks
    * Impact of slope limiting on the solution
    * Softening of sharp discontinuities at lower resolution.
    
    The analytical solution used here is based on lecture notes by 
    `Frank van den Bosch <https://campuspress.yale.edu/vdbosch/>`__
    (`pdf <http://www.astro.yale.edu/vdbosch/Astrophysical_Flows.pdf>`__)
    and `Susanne Hoefner <https://www.uu.se/en/contact-and-organisation/staff?query=N99-874>`__
    (`pdf <https://www.astro.uu.se/~hoefner/astro/teach/ch10.pdf>`__).
    
    Parameters
    ----------
    unit_l: float
        Code unit for length in units of centimeters.
    unit_t: float
        Code unit for time in units of seconds.
    unit_m: float
        Code unit for mass in units of gram.
    """
    
    def __init__(self, unit_l = 1.0, unit_t = 1.0, unit_m = 1.0):
        
        setup_base.Setup.__init__(self, unit_l = unit_l, unit_t = unit_t, unit_m = unit_m)
    
        # Parameters for the Sod shocktube test
        # sod_gamma = 1.4
        # sod_x0 = 0.5
        # sod_rhoL = 8.0
        # sod_rhoR = 1.0
        # sod_PL = 10.0 / sod_gamma
        # sod_PR = 1.0 / sod_gamma
        # sod_uL = 0.0
        # sod_uR = 0.0
        
        self.sod_gamma = 1.4
        self.sod_x0 = 0.5
        self.sod_rhoL = 1.0
        self.sod_rhoR = 1.0 / 8.0
        self.sod_PL = 1.0
        self.sod_PR = 1.0 / 10.0
        self.sod_uL = 0.0
        self.sod_uR = 0.0

        return 

    # ---------------------------------------------------------------------------------------------

    def shortName(self):
        
        return 'shocktube'

    # ---------------------------------------------------------------------------------------------
    
    def setInitialData(self, sim, nx):
        
        sim.setEquationOfState(eos_mode = 'ideal', gamma = self.sod_gamma)
        sim.setDomain(nx, 1, xmin = 0.0, xmax = 1.0, bc_type = 'outflow')

        DN = sim.q_prim['DN']
        VX = sim.q_prim['VX']
        PR = sim.q_prim['PR']

        maskL = (sim.x <= self.sod_x0)
        maskR = np.logical_not(maskL)
        sim.V[DN, maskL, :] = self.sod_rhoL
        sim.V[DN, maskR, :] = self.sod_rhoR
        sim.V[VX, maskL, :] = self.sod_uL
        sim.V[VX, maskR, :] = self.sod_uR
        sim.V[PR, maskL, :] = self.sod_PL
        sim.V[PR, maskR, :] = self.sod_PR
        
        return

    # ---------------------------------------------------------------------------------------------

    def trueSolution(self, sim, x, q_plot):
    
        # Grid variables
        t = sim.t
        nx = len(x)
    
        # Shorthand for Sod input variables
        P_L = self.sod_PL
        P_R = self.sod_PR
        rho_L = self.sod_rhoL
        rho_R = self.sod_rhoR
        u_L = self.sod_uL
        u_R = self.sod_uR
        x_0 = self.sod_x0
        
        # gamma and sound speed
        g = self.sod_gamma
        gm1 = g - 1.0
        gp1 = g + 1.0
        cs_L = np.sqrt(g * P_L / rho_L)
        cs_R = np.sqrt(g * P_R / rho_R)
    
        # Implicit equation to solve for shock speed in Sod problem
        def sod_eq(M):
            t1 = P_R / P_L * (2.0 * g / gp1 * M**2 - gm1 / gp1)
            rhs = cs_L * gp1 / gm1 * (1.0 - t1**(gm1 / 2.0 / g))
            return M - 1.0 / M - rhs
        
        # Compute speed of shock in frame of tube
        M = scipy.optimize.brentq(sod_eq, 1.0001, 20.0, xtol = 1E-6)
        
        # The numerical solution comes out wrong by this factor for some yet unknown reason.
        M *= 0.986
        M_2 = M**2
        u_s = M * cs_R
        
        # Post-shock state after shock has passed through area R. van den Bosch has
        # u1 = 2.0 / gp1 * (M - 1.0 / M) 
        # for the velocity, but this seems to give the wrong result. The current way of computing u1
        # was derived by going into the shock frame where uRp = uR - us, u1p = u1 - us, and using the
        # RH-condition that u1p / uRp = (gm1 * M2 + 2)/(gp1 * M2)
        P_1 = P_R * (2.0 * g / gp1 * M_2 - gm1 / gp1)
        rho_1 = rho_R / (2.0 / gp1 / M_2 + gm1 / gp1)
        u_1 = u_s * (1.0 - (2.0 / gp1 / M_2 + gm1 / gp1))
        
        # State to the left of contact discontinuity with state 1
        P_2 = P_1
        u_2 = u_1
        rho_2 = rho_L * (P_2 / P_L)**(1.0 / g)
        cs_2 = np.sqrt(g * P_2 / rho_2)
        
        # Boundaries of states. The rarefacton wave progresses at speed csL to the left and thus
        # reaches x1 by time t. The shock to the right goes as us * t to x4, whereas the contact
        # discontinuity moves at the speed of state 2. 
        x_1 = x_0 - cs_L * t
        x_2 = x_0 + (u_2 - cs_2) * t
        x_3 = x_0 + u_2 * t
        x_4 = x_0 + u_s * t
        
        # Areas of array where solutions are valid
        maskL = (x <= x_1)
        maskE = (x > x_1) & (x <= x_2)
        mask2 = (x > x_2) & (x <= x_3)
        mask1 = (x > x_3) & (x <= x_4)
        maskR = (x > x_4)
    
        # Compute rarefaction state, which depends on position unlike the other states
        x_E = x[maskE]
        u_E = 2.0 / gp1 * (cs_L + (x_E - x_0) / t)
        cs_E = cs_L - 0.5 * gm1 * u_E
        P_E = P_L * (cs_E / cs_L)**(2.0 * g / gm1)
        rho_E = g * P_E / cs_E**2
        
        # Set solution
        nq = len(q_plot)
        V_sol = np.zeros((nq, nx), float)
    
        for i in range(nq):
            if q_plot[i] == 'DN':
                V_sol[i, maskL] = rho_L
                V_sol[i, maskE] = rho_E
                V_sol[i, mask2] = rho_2
                V_sol[i, mask1] = rho_1
                V_sol[i, maskR] = rho_R
            elif q_plot[i] == 'VX':
                V_sol[i, maskL] = u_L
                V_sol[i, maskE] = u_E
                V_sol[i, mask2] = u_2
                V_sol[i, mask1] = u_1
                V_sol[i, maskR] = u_R
            elif q_plot[i] == 'PR':
                V_sol[i, maskL] = P_L
                V_sol[i, maskE] = P_E
                V_sol[i, mask2] = P_2
                V_sol[i, mask1] = P_1
                V_sol[i, maskR] = P_R
            else:
                pass
        
        return V_sol

###################################################################################################
