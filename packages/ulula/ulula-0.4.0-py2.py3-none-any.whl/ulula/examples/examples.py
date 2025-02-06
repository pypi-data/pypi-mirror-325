###################################################################################################
#
# This file is part of the ULULA code.
#
# (c) Benedikt Diemer, University of Maryland
#
###################################################################################################

import ulula.core.simulation as ulula_sim
import ulula.core.run as ulula_run

import ulula.setups.advection as setup_advection
import ulula.setups.atmosphere as setup_atmosphere
import ulula.setups.cloud_crushing as setup_cloud_crushing
import ulula.setups.freefall as setup_freefall
import ulula.setups.kelvin_helmholtz as setup_kelvin_helmholtz
import ulula.setups.rayleigh_taylor as setup_rayleigh_taylor
import ulula.setups.sedov_taylor as setup_sedov_taylor
import ulula.setups.shocktube as setup_shocktube
import ulula.setups.soundwave as setup_soundwave
import ulula.setups.tidal_disruption as setup_tidal_disruption

###################################################################################################

def main():
    
    # ---------------------------------------------------------------------------------------------
    # 1D setups
    # ---------------------------------------------------------------------------------------------

    #runSoundwave()
    
    #runShocktube()
    
    #runFreefall()

    #runAtmosphere()

    # ---------------------------------------------------------------------------------------------
    # 2D setups
    # ---------------------------------------------------------------------------------------------
    
    #runAdvection()
    
    #runKelvinHelmholtz(movie = False)

    #runCloudCrushing()
    
    #runSedovTaylor(plot_1d = False)

    #runRayleighTaylor()
    
    #runTidalDisruption()

    return

###################################################################################################

def runSoundwave():
    """
    Run the sound wave setup
    """

    setup = setup_soundwave.SetupSoundwave(eos_mode = 'isothermal', amplitude = 0.01)
    ulula_run.run(setup, nx = 300, tmax = 4.0, max_steps = 10000, plot_time = 0.5, save_plots = True,
                q_plot = ['DN', 'VX'], plot_file_ext = 'pdf', 
                plot_unit_l = 'm', plot_unit_t = 's', plot_unit_m = 'kg')
    
    return

###################################################################################################

def runShocktube():
    """
    Run the shock tube setup

    The function creates outputs for piecewise-constant states and piecewise-linear reconstruction.
    """

    setup = setup_shocktube.SetupShocktube()
    kwargs = dict(tmax = 0.2, nx = 100, plot_step = 100, save_plots = True,
                plot_ics = False, q_plot = ['DN', 'VX', 'PR'])
    
    hs = ulula_sim.HydroScheme(reconstruction = 'const', cfl = 0.5)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_const', **kwargs)

    hs = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'vanleer', riemann = 'hll', 
                            time_integration = 'hancock', cfl = 0.5)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_linear', **kwargs)
    
    return

###################################################################################################

def runFreefall():
    """
    Run the freefall setup
    """

    setup = setup_freefall.SetupFreefall()
    ulula_run.run(setup, nx = 300, tmax = 1.2, plot_step = None, plot_time = 0.1, print_step = 100, 
                save_plots = True, q_plot = ['DN', 'VX'], plot_file_ext = 'pdf')

    return

###################################################################################################

def runAtmosphere():
    """
    Run the atmosphere setup
    """

    setup = setup_atmosphere.SetupAtmosphere()
    ulula_run.run(setup, nx = 200, tmax = 10.0, 
                save_plots = True, plot_step = None, plot_time = 0.5, print_step = 1000, 
                q_plot = ['DN', 'VX'], plot_file_ext = 'pdf', movie = False,
                plot_unit_l = 'km', plot_unit_t = 'hr', plot_unit_m = 't')
    
    return

###################################################################################################

def runAdvection():
    """
    Run the advection test setup
    
    We run the advection test with different numerical algorithms. When using the MC limiter with 
    an Euler (first-order) time integration, the test fails spectacularly. 
    """

    setup = setup_advection.SetupAdvection()
    kwargs = dict(nx = 100, tmax = 2.5, plot_step = 1000, save_plots = True, plot_ics = False, q_plot = ['DN'])

    hs = ulula_sim.HydroScheme(reconstruction = 'const', cfl = 0.8)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_const', **kwargs)

    hs = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'minmod', time_integration = 'euler', cfl = 0.8)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_linear_minmod_euler', **kwargs)

    hs = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'mc', time_integration = 'euler', cfl = 0.8)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_linear_mc_euler', **kwargs)

    hs = ulula_sim.HydroScheme(reconstruction = 'linear', limiter = 'mc', time_integration = 'hancock', cfl = 0.8)
    ulula_run.run(setup, hydro_scheme = hs, plot_suffix = '_linear_mc_hancock', **kwargs)

    return

###################################################################################################

def runKelvinHelmholtz(movie = False):
    """
    Run the Kelvin-Helmholtz setup

    This function demonstrates how to make movies with Ulula. By passing the ``movie`` parameter,
    the function outputs frames at a user-defined rate and combines them into a movie at the end
    of the simulation.
    
    Parameters
    ----------
    movie: bool
        Whether to produce plots or a movie.
    """
    
    setup = setup_kelvin_helmholtz.SetupKelvinHelmholtz(n_waves = 1)

    if movie:
        kwargs = dict(tmax = 4.0, movie = True, movie_length = 20.0, plot_ics = False)
    else:
        kwargs = dict(tmax = 3.0, plot_time = 1.0)

    ulula_run.run(setup, nx = 200, q_plot = ['DN'], **kwargs)

    return

###################################################################################################

def runCloudCrushing():
    """
    Run the cloud crushing setup
    """

    setup = setup_cloud_crushing.SetupCloudCrushing()
    ulula_run.run(setup, tmax = 20, nx = 300, q_plot = ['DN', 'VX'], plot_file_ext = 'pdf', plot_time = 1.0)

    return

###################################################################################################

def runSedovTaylor(plot_1d = True):
    """
    Run the Sedov-Taylor explosion setup
    
    This function demonstrates a style of 1D plotting where the solution is averaged in 
    radial bins.

    Parameters
    ----------
    plot_1d: bool
        If True, the usual 2D plots are replaced by radial 1D plots.
    """

    setup = setup_sedov_taylor.SetupSedovTaylor()
    kwargs = dict(tmax = 0.02, nx = 200, plot_step = 1000, save_plots = True, 
                plot_ics = False, plot_file_ext = 'pdf')    
    if plot_1d:
        kwargs.update(dict(plot_1d = True, q_plot = ['DN', 'PR', 'VT'], plot_type = 'radius'))
    else:
        kwargs.update(dict(q_plot = ['DN', 'PR']))

    ulula_run.run(setup, plot_suffix = '', **kwargs)

    return

###################################################################################################

def runRayleighTaylor():
    """
    Run the Rayleigh-Taylor setup
    """

    setup = setup_rayleigh_taylor.SetupRayleighTaylor()
    ulula_run.run(setup, nx = 80, tmax = 6.0, plot_time = 0.2, print_step = 100, 
                save_plots = True, q_plot = ['DN', 'VY'], 
                plot_ghost_cells = False, plot_file_ext = 'pdf')

    return

###################################################################################################

def runTidalDisruption():
    """
    Run the tidal disruption setup
    """

    setup = setup_tidal_disruption.SetupTidalDisruption()
    ulula_run.run(setup, nx = 120, tmax = 3.0, plot_step = None, plot_time = 0.1, print_step = 100, 
                save_plots = True, q_plot = ['DN', 'GP'], plot_ghost_cells = False, 
                plot_file_ext = 'pdf')

    return

###################################################################################################
# Trigger
###################################################################################################

if __name__ == "__main__":
    main()
