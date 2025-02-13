import numpy as np

def PengRobinsonCalculation(x, y, T, P, Tc, Pc, Acentric, k_bin):
    """
    Calculate fugacity coefficients, molar volume of the mixture, and b parameter
    using the Peng-Robinson equation of state.

    Args:
    x (np.array): Molar fraction in the oil phase.
    y (np.array): Molar fraction in the gas phase.
    T (float): Temperature in K.
    P (float): Pressure in Pa.
    Tc (np.array): Critical temperature in K for each component.
    Pc (np.array): Critical pressure in Pa for each component.
    Acentric (np.array): Acentric factor for each component.
    k_bin (np.array): Binary interaction parameter matrix.

    Returns:
    tuple: Fugacity coefficients (phi), molar volume of the mixture (V_mist), 
           and b parameter (b) for the Peng-Robinson equation.
    """
    R = 8.314  # J/(mol*K)
    n_comp = len(x)
    alpha = (1 + (0.37464 + 1.54226 * Acentric - 0.26992 * Acentric**2) * (1 - np.sqrt(T / Tc)))**2
    a = 0.45724 * R**2 * Tc**2 / Pc * alpha
    b = 0.07780 * R * Tc / Pc

    # Initialize arrays for mixture properties
    a_mist = np.zeros(2)
    b_mist = np.zeros(2)
    phi = np.zeros((2, n_comp))
    Z_mist = np.zeros(2)
    V_mist = np.zeros(2)
    x_comp = np.array([x, y])

    for j in range(2):  # Loop over phases (oil and gas)
        xj = x_comp[j]
        
        # Calculate a_mist and b_mist using vectorized operations
        for i in range(n_comp):
            for k in range(n_comp):
                a_mist[j] += x_comp[j, i] * x_comp[j, k] * np.sqrt(a[i] * a[k]) * (1 - k_bin[i, k])
            b_mist[j] += x_comp[j, i] * b[i]

        # Coefficients for the Peng-Robinson cubic equation of state
        A = a_mist[j] * P / (R * T)**2
        B = b_mist[j] * P / (R * T)
        coeffs = [1, -1 + B, A - 3*B**2 - 2*B, -(A * B - B**2 - B**3)]
        
        # Solve the cubic equation and handle real roots directly
        roots = np.roots(coeffs)
        aux = 1e5 if j == 0 else -1e5
        roots[~np.isreal(roots)] = aux  # Filter real roots
        roots = roots.real
        Z = np.min(roots) if j == 0 else np.max(roots)  # Smallest root for liquid, largest for gas

        Z_mist[j] = Z

        # Calculate fugacity coefficients (phi) for each component
        for i in range(n_comp):
            phi[j, i] = np.exp((b[i] / b_mist[j] * (Z - 1) - np.log(Z - B) + A / (2 * np.sqrt(2) * B) * 
                                (b[i] / b_mist[j] - (2 * np.sqrt(a[i]) / a_mist[j]) * np.sum(x_comp[j,:] *
                                np.sqrt(a) * (1-k_bin[i,:]))) * np.log((Z + (1 + np.sqrt(2)) * B) / 
                                (Z + (1 - np.sqrt(2)) * B))))

        # Calculate the molar volume of the mixture
        V_mist[j] = Z * R * T / P

    return phi, V_mist, b
