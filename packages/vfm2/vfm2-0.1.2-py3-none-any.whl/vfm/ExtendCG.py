import numpy as np
import pandas as pd
from vfm.PengRobinsonCalculation import PengRobinsonCalculation

def ExtendCG(Data, PP, pos_row, pos_col):
    """
    Extends gas composition analysis by filling missing data and calculating specific properties.

    Args:
        Data (pd.DataFrame): Input DataFrame containing gas chromatography results and related data.
        PP (dict): PureProperties dictionary containing critical properties and binary interaction parameters.
        pos_row (int): Row index in the DataFrame for the current analysis.
        pos_col (int): Column index in the DataFrame (not used in this function).

    Returns:
        tuple:
            - y (np.array): Molar composition vector of the gas phase.
            - SGg (float): Specific gravity of the gas phase.
    """
    # Constants
    T_SC = 293.15  # Standard temperature [K]
    P_SC = 101325  # Standard pressure [Pa]
    R = 8.314  # Universal gas constant [m^3*bar/K/mol]
    MWair = 28.97  # Molar weight of air [g/mol]
    rhoair_SC = 0.001 * MWair * P_SC / (R * T_SC)  # Air density at standard conditions [kg/m^3]

    # Searches the closest consistent data in time
    Tempo = Data['Time']
    pos_aux = pos_row

    # Ensure that N2 column is numeric
    Data['N2'] = pd.to_numeric(Data['N2'], errors='coerce')

    if np.isnan(Data['N2'].iloc[pos_row]):
        # Searches for consistent data entry at previous sampling times
        pos_p = 0
        while pos_row - pos_p >= 0 and np.isnan(Data['N2'].iloc[pos_row - pos_p]):
            pos_p += 1
            if pos_row - pos_p < 0:
                break

        # Searches for consistent data entry at later sampling times
        pos_f = 0
        while pos_row + pos_f < len(Data['Time']) and np.isnan(Data['N2'].iloc[pos_row + pos_f]):
            pos_f += 1
            if pos_row + pos_f >= len(Data['Time']):
                break

        # Determine the closest consistent data entry in time
        if pos_row - pos_p < 0:
            pos_aux = pos_row + pos_f
        elif pos_row + pos_f >= len(Data['Time']):
            pos_aux = pos_row - pos_p
        else:
            if (Tempo.iloc[pos_row] - Tempo.iloc[pos_row - pos_p]).days < (Tempo.iloc[pos_row + pos_f] - Tempo.iloc[pos_row]).days:
                pos_aux = pos_row - pos_p
            else:
                pos_aux = pos_row + pos_f

    # Define molar composition vector based on gas chromatography results
    y = 0.01 * np.array([
        Data['N2'].iloc[pos_aux], Data['CO2'].iloc[pos_aux], Data['C1'].iloc[pos_aux], 
        Data['C2'].iloc[pos_aux], Data['C3'].iloc[pos_aux], Data['iC4'].iloc[pos_aux], 
        Data['nC4'].iloc[pos_aux], Data['iC5'].iloc[pos_aux], Data['nC5'].iloc[pos_aux], 
        Data['nC6'].iloc[pos_aux], Data['nC7'].iloc[pos_aux], Data['nC8'].iloc[pos_aux], 
        Data['nC9'].iloc[pos_aux], Data['nC10'].iloc[pos_aux]
    ])

    # Correction of incomplete n-decane entries
    y[-1] = max(y[-1], 1e-6)

    # Calculation of the specific gravity of the gas phase if not available
    if np.isnan(Data['SGg'].iloc[pos_row]):
        _, V_mist, b = PengRobinsonCalculation(np.zeros(PP['N']), y, T_SC, P_SC, PP['Tc'], PP['Pc'], PP['Acentric'], PP['k_bin'])
        Vm_gas = V_mist[1] - np.sum(y * b * PP['s'])  # Gas molar volume [m^3/mol]
        MW_gas = np.sum(y * PP['MW'])  # Molar weight of the gas [kg/mol]
        rhog = MW_gas / Vm_gas * 0.001  # Gas density [kg/m^3]
        SGg = rhog / rhoair_SC
    else:
        SGg = Data['SGg'].iloc[pos_aux]

    return y, SGg
