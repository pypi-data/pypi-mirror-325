# Import necessary modules
import numpy as np
from scipy.optimize import fsolve, least_squares, minimize, root_scalar, basinhopping, differential_evolution
from vfm.DelumpingMethod import DelumpingMethod
from vfm.VFMCalculation import VFMCalculation
from vfm.BisectionMethod import BisectionMethod
import time

def VFM(T_us_PI, T_us_RWT, P_us_PI, P_us_RWT, P_ds_PI, P_ds_RWT, Qgi_PI, Qgi_RWT,
        opening_PI, opening_RWT, Fc, Rhoo_SC, SGg, SGw, GOR, BSW, Ql_SC, PureProperties,
        y_CG, T_sep, P_sep, flag_code):
    """
    Perform Virtual Flow Meter (VFM) calculations to estimate flow parameters and fluid properties.

    Args:
        T_us_PI (float): Upstream temperature during Production Injection (PI) in Kelvin.
        T_us_RWT (float): Upstream temperature during Reference Well Test (RWT) in Kelvin.
        P_us_PI (float): Upstream pressure during PI in bar.
        P_us_RWT (float): Upstream pressure during RWT in bar.
        P_ds_PI (float): Downstream pressure during PI in bar.
        P_ds_RWT (float): Downstream pressure during RWT in bar.
        Qgi_PI (float): Gas injection rate during PI in standard cubic meters per day.
        Qgi_RWT (float): Gas injection rate during RWT in standard cubic meters per day.
        opening_PI (float): Valve opening percentage during PI (0 to 1).
        opening_RWT (float): Valve opening percentage during RWT (0 to 1).
        Fc (float): Correction factor for flow calculations.
        Rhoo_SC (float): Oil density at standard conditions in kg/m^3.
        SGg (float): Specific gravity of gas.
        SGw (float): Specific gravity of water.
        GOR (float): Gas-oil ratio in standard cubic meters per cubic meter.
        BSW (float): Basic sediment and water content as a fraction (0 to 1).
        Ql_SC (float): Liquid flow rate at standard conditions in standard cubic meters per day.
        PureProperties (dict): Dictionary containing molecular weight and other properties of pure components.
        y_CG (np.array): Compositional data for gas.
        T_sep (float): Separator temperature in Kelvin.
        P_sep (float): Separator pressure in bar.
        flag_code (int): Indicator for calculation method or algorithm to use.

    Returns:
        tuple: Contains estimated values for:
            - Cv_est (float): Flow coefficient.
            - Cv_gpm_est (float): Flow coefficient in gallons per minute.
            - Qw_SC_est (float): Water flow rate at standard conditions in m^3/day.
            - Qo_SC_est (float): Oil flow rate at standard conditions in m^3/day.
            - Qg_SC_est (float): Gas flow rate at standard conditions in m^3/day.
            - API_est (float): Estimated API gravity.
            - GOR_est (float): Estimated gas-oil ratio in m^3/m^3.
            - SGg_est (float): Estimated specific gravity of gas.
            - z_est (float): Compressibility factor.
            - x_est (np.array): Compositional vector for liquid phase.
            - y_est (np.array): Compositional vector for vapor phase.
            - MWblackoil (float): Estimated molecular weight of black oil.
            - FO (float): Optimization objective function value.
            - pseudo_est (dict): Dictionary of estimated pseudocritical properties.
    """
    # Constants and initial setup
    rhow_SC = 984.252  # Water density at 60 oF in kg/m^3
    SGo = Rhoo_SC / rhow_SC
    API = 141.5 / SGo - 131.5

    # Definitions concerning the Gamma-Distribution model used to split the heavy hydrocarbons
    Lambda = 0.5  # Parameter for heavy hydrocarbon distribution

    if flag_code == 1:
        MWblackoil = 197
        eta = PureProperties['MW'][PureProperties['N'] - 1]
        M_b = np.array([156.31, 170.34, 184.37, 198.39, 212.42, 226.45, 240.47, 1100])
        lb_var, ub_var = 144, 250
    else:
        MWblackoil = np.exp(-(API - 202.99) / 29.95)
        eta = PureProperties['MW'][9]
        M_b = np.append(PureProperties['MW'][10:], [170.34, 198.39, 226.45, 1100])
        lb_var, ub_var = M_b[0], M_b[-1]

    # Calculate initial estimates using VFMCalculation
    Cv_est, Cv_gpm_est, Wt, Rhom, Vt, Qw_SC_est, Qo_SC_est, Qg_SC_est = VFMCalculation(
        T_us_RWT, P_us_RWT, P_ds_RWT, Qgi_RWT, opening_RWT, 1, SGo, SGg, SGw, GOR, BSW, Ql_SC, -flag_code)

    # Use fsolve to find Ql_SC_est
    def equations(Ql_var):
        Cv_est_temp, _, _, _, _, _, _, _ = VFMCalculation(
            T_us_PI, P_us_PI, P_ds_PI, Qgi_PI, opening_PI, Fc, SGo, SGg, SGw, GOR, BSW, Ql_var, -flag_code)
        return Cv_est_temp - Cv_est

    # start_time = time.time()  # Start timing

    # try:   
    #     # Ql_SC_est = fsolve(equations, Ql_SC, xtol=1e-6, maxfev=1000, col_deriv=True)[0]
    #     # Ql_SC_est = fsolve(equations, Ql_SC, xtol=1e-6, maxfev=500)[0]
    #     Ql_SC_est = fsolve(equations, Ql_SC, xtol=1e-6)[0]
    # except Exception:
    #     Ql_SC_est = Ql_SC

    # end_time = time.time()


######################3

    # Define bounds and solve using root_scalar
    lower_bound = max(0, Ql_SC * 0.001)  # Prevent unrealistic negative values
    upper_bound = Ql_SC * 1000  # Assume the solution lies within a reasonable range
    
    try:
        root_result = root_scalar(
            equations,
            bracket=[-lower_bound, upper_bound],
            method='bisect',  # Choose method: 'bisect', 'brentq', etc.
            xtol=1e-6,  # Tolerance for convergence
            # maxiter=100  # Limit the number of iterations
        )
        Ql_SC_est = root_result.root if root_result.converged else Ql_SC  # Use the result if converged
    except ValueError as e:
        print(f"Root finding failed: {e}")
        Ql_SC_est = Ql_SC  # Fallback to initial guess


##########################


    # start_time = time.time()  # Start timing

    # # Define initial bounds and dynamically adjust
    # lower_bound = max(0, Ql_SC * 0.001)
    # upper_bound = Ql_SC * 2
    # max_expansion_attempts = 5  # Limit the number of bound expansions
    # expansion_factor = 2

    # # Dynamically adjust bounds to find a bracketing interval
    # for attempt in range(max_expansion_attempts):
    #     try:
    #         f_lower = equations(lower_bound)
    #         f_upper = equations(upper_bound)
    #         if f_lower * f_upper < 0:
    #             break  # Valid bounds found
    #         # Expand the upper bound if signs are not opposite
    #         upper_bound *= expansion_factor
    #     except ValueError:
    #         # Handle invalid inputs to the equations function
    #         upper_bound *= expansion_factor

    # if f_lower * f_upper >= 0:
    #     print("Failed to find bounds with opposite signs after expansion. Returning initial guess.")
    #     Ql_SC_est = Ql_SC  # Fallback to initial guess
    # else:
    #     try:
    #         root_result = root_scalar(
    #             equations,
    #             bracket=[lower_bound, upper_bound],
    #             method='brentq',
    #             xtol=1e-6,
    #             maxiter=100
    #         )
    #         Ql_SC_est = root_result.root if root_result.converged else Ql_SC
    #     except Exception as e:
    #         print(f"Root finding failed: {e}")
    #         Ql_SC_est = Ql_SC  # Fallback to initial guess

    # end_time = time.time()

    # # Apply bounds to prevent unrealistic solutions
    # lower_bound = max(0, Ql_SC * 0.001)  # Prevent negative or very low Ql_var
    # upper_bound = Ql_SC * 2  # Assume the solution is not more than twice the initial guess

    # result = least_squares(
    #     equations,
    #     Ql_SC,  # Initial guess
    #     bounds=(lower_bound, upper_bound),
    #     xtol=1e-6,
    #     # max_nfev=100
    # )

    # if result.success:
    #     Ql_SC_est = result.x[0]  # Extract the scalar solution
    # else:
    #     Ql_SC_est = Ql_SC  # Fallback to initial guess if no convergence

    # Update estimates after solving
    Cv_est, Cv_gpm_est, Wt, Rhom, Vt, Qw_SC_est, Qo_SC_est, Qg_SC_est = VFMCalculation(
        T_us_PI, P_us_PI, P_ds_PI, Qgi_PI, opening_PI, Fc, SGo, SGg, SGw, GOR, BSW, Ql_SC_est, -flag_code)

    # Define the objective function used in the BisectionMethod
    def objective_function(Ql_var):

        # start_time = time.time()  # Start timing

        FO, _, _, _, _, _, _, _ = DelumpingMethod(
            Ql_var, eta, Lambda, M_b, PureProperties, y_CG, T_sep, P_sep, Qg_SC_est, Qo_SC_est,
            SGo, API, Qg_SC_est / Qo_SC_est, SGg, flag_code
        )

        # end_time = time.time()  # End timing
        # print(f"Objective function evaluated in {end_time - start_time} seconds")
        return FO

    # Perform optimization
    if flag_code == 1:
        FO, aux, _, PRE_API, PRE_GOR, PRE_SGg, z_est, x_comp, _, pseudo_est = BisectionMethod(
            objective_function, MWblackoil, lb_var, ub_var)
    else:
        # Init of GOR_est
        GOR_est = Qg_SC_est / Qo_SC_est  # Initialize GOR_est
        # print(GOR_est,Cv_est)

        # print("Starting optimization...")

        # minimizer_kwargs = {"method": "L-BFGS-B", "bounds": [(lb_var, ub_var)], "options": {"ftol": 1e-1}}
        # minimizer_kwargs = {"method": "Nelder-Mead", "options": {"xatol": 1e-3}}  # Replace xtol with xatol
        # opt_result = basinhopping(objective_function, x0=MWblackoil, minimizer_kwargs=minimizer_kwargs, disp=True, niter=10)

        # start_time = time.time()  # Start timing

        opt_result = minimize(objective_function, x0=MWblackoil, bounds=[(lb_var, ub_var)],
                            method='Nelder-Mead', options={'xatol': 1e-6, 'fatol':1e-6})
                            # method='Nelder-Mead', options={'xatol': 1e-4, 'fatol':1e-4, 'maxiter': 50})
                            # method='Nelder-Mead', options={'xatol': 1e-3, 'fatol':1e-3, 'maxiter': 5})
                            # method='Nelder-Mead', options={'ftol': 1e-3, 'gtol': 1e-3, 'maxiter':5,})
        

                            # method='SLSQP', options={'ftol': 1e-6, 'maxiter':10, 'disp': True,}, callback=optimization_callback)
        
        # end_time = time.time()  # End timing
        # print(f"Minimization in {end_time - start_time} seconds")

        # print("Finished optimization.")
        
        aux = opt_result.x[0]
        FO = opt_result.fun

        FO, PRE_API, PRE_GOR, PRE_SGg, z_est, x_comp, MW_comp, pseudo_est = DelumpingMethod(aux, eta, Lambda, M_b, PureProperties, y_CG, T_sep, P_sep, Qg_SC_est, Qo_SC_est, SGo, API, GOR_est, SGg, flag_code)

    # Storage of output variables
    MWblackoil = aux
    API_est = API + PRE_API * API / 100
    GOR_est = Qg_SC_est / Qo_SC_est + PRE_GOR * Qg_SC_est / Qo_SC_est / 100
    SGg_est = SGg + PRE_SGg * SGg / 100
    x_est = x_comp[0, :]
    y_est = x_comp[1, :]

    return Cv_est, Cv_gpm_est, Qw_SC_est, Qo_SC_est, Qg_SC_est, API_est, GOR_est, \
           SGg_est, z_est, x_est, y_est, MWblackoil, FO, pseudo_est