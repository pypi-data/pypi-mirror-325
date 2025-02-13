import numpy as np

def BisectionMethod(Fun, var_0, lbx, ubx, Tol):
    """
    Perform the Bisection Method to optimize a variable within specified bounds
    based on the objective function `Fun`.

    Args:
        Fun (callable): The objective function to be minimized. It must return
                        the objective value and additional outputs.
        var_0 (float): Initial guess for the variable to optimize.
        lbx (float): Lower bound of the variable.
        ubx (float): Upper bound of the variable.
        Tol (float): Tolerance for convergence of the optimization.

    Returns:
        tuple: 
            - FO_out (float): Final value of the objective function.
            - var_0 (float): Optimized variable value.
            - flag_otim (int): Optimization flag (1 for success, -1 for failure).
            - PRE_API (float): Predicted API deviation.
            - PRE_GOR (float): Predicted GOR deviation.
            - PRE_SGg (float): Predicted SGg deviation.
            - z_comp (array): Compositional properties for z.
            - x_comp (array): Compositional properties for x.
            - MW_comp (array): Molecular weight of the components.
            - z_pseudo (array): Pseudo-critical properties.

    Raises:
        Exception: If the maximum number of iterations is exceeded without convergence.
    """
    # Maximum number of iterations
    MaxIter = 500
    
    # Evaluate the model at the initial guess and the bounds
    FO = np.zeros(3)
    FO[0], PRE_API, PRE_GOR, PRE_SGg, z_comp, x_comp, MW_comp, z_pseudo = Fun(var_0)
    FO[1], *_ = Fun(ubx)
    FO[2], *_ = Fun(lbx)
    
    cont = 1
    while True:
        LowestFobj = min(FO)

        # Update bounds based on the lowest objective function value
        if LowestFobj == FO[2]:
            ubx = var_0
            FO[1] = FO[0]
        elif LowestFobj == FO[1]:
            lbx = var_0
            FO[2] = FO[0]
        elif abs(FO[0] - FO[1]) < abs(FO[0] - FO[2]):
            lbx = var_0
            FO[2] = FO[0]
        else:
            ubx = var_0
            FO[1] = FO[0]

        # Update the variable to the midpoint of the bounds
        var_0 = (ubx + lbx) / 2

        # Calculate the cost function at the new midpoint
        FO[0], PRE_API, PRE_GOR, PRE_SGg, z_comp, x_comp, MW_comp, z_pseudo = Fun(var_0)

        # Check for stopping criteria
        if abs(FO[0] - FO[1]) < Tol and abs(FO[0] - FO[2]) < Tol:
            flag_otim = 1
            break
        cont += 1
        if cont > MaxIter:
            print('Optimization failed to converge to a solution within the tolerance and iteration limit')
            flag_otim = -1
            break

    FO_out = FO[0]
    return (FO_out, var_0, flag_otim, PRE_API, PRE_GOR, PRE_SGg, z_comp, x_comp, MW_comp, z_pseudo)
