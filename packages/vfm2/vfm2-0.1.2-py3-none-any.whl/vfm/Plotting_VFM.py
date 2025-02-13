import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

def plotting_vfm_v2(data_vfm, data_bdo, time_bdo, qw_sc_est, qo_sc_est, qg_sc_est, pos_sim, flag_init, dir_save):
    """
    Plot and compare estimated flowrates with actual BDO (production) data.

    Args:
        data_vfm (pd.DataFrame): PI data containing timestamps and flowrates.
        data_bdo (pd.DataFrame): BDO data containing timestamps and flowrates.
        time_bdo (pd.Series): Time indices for BDO data.
        qw_sc_est (np.ndarray): Estimated water flowrates (matrix: time x wells).
        qo_sc_est (np.ndarray): Estimated oil flowrates (matrix: time x wells).
        qg_sc_est (np.ndarray): Estimated gas flowrates (matrix: time x wells).
        pos_sim (np.ndarray): Indices of simulation time steps.
        flag_init (int): Initialization flag to select the model version.
        dir_save (str): Directory path to save the plots.

    Returns:
        tuple: Contains calculated and comparison metrics:
            - qot_pi_est (np.ndarray): Total oil flowrate (hourly PI).
            - qgt_pi_est (np.ndarray): Total gas flowrate (hourly PI).
            - qot_bdo_est (np.ndarray): Total estimated oil flowrate (daily BDO).
            - qgt_bdo_est (np.ndarray): Total estimated gas flowrate (daily BDO).
            - qwt_bdo_est (np.ndarray): Total estimated water flowrate (daily BDO).
            - pre_qo_pi (np.ndarray): Percent relative error (PRE) for oil (PI).
            - pre_qg_pi (np.ndarray): PRE for gas (PI).
            - pre_qo_bdo (np.ndarray): PRE for oil (BDO).
            - pre_qg_bdo (np.ndarray): PRE for gas (BDO).
            - pre_qw_bdo (np.ndarray): PRE for water (BDO).
            - mape_q (np.ndarray): Mean absolute percentage error for flowrates.
    """

    # Convert Time columns to datetime
    # data_vfm['Time'] = pd.to_datetime(data_vfm['Time'], errors='coerce')
    # data_bdo['Time'] = pd.to_datetime(data_bdo['Time'], errors='coerce')
    # time_bdo = pd.to_datetime(time_bdo, errors='coerce')

    # Define input sizes
    n_bdo = len(time_bdo)
    ts = (data_vfm['Time'].iloc[1] - data_vfm['Time'].iloc[0]).total_seconds() / (24 * 3600)
    n_row, n_col = qo_sc_est.shape

    # Initialize arrays for flowrate estimations
    qot_pi_est = np.zeros(n_row)
    qgt_pi_est = np.zeros(n_row)
    qot_bdo_est = np.full(n_bdo, np.nan)
    qwt_bdo_est = np.full(n_bdo, np.nan)
    qgt_bdo_est = np.full(n_bdo, np.nan)

    # Calculate total flowrates for PI data (hourly)
    for i in range(n_col):
        qot_pi_est[pos_sim] += qo_sc_est[pos_sim, i] / 24  # Convert to hourly [N m^3/h]
        qgt_pi_est[pos_sim] += qg_sc_est[pos_sim, i] / 24  # Convert to hourly [N m^3/h]

    # Align BDO and VFM data, and calculate daily flowrates
    for i in range(n_bdo):
        k = np.searchsorted(data_vfm['Time'], time_bdo.iloc[i], side='right')
        j = np.searchsorted(data_bdo['Time'], time_bdo.iloc[i], side='right') - 1

        if k > 0 and j >= 0:
            k_start = max(0, k - int(7 / ts))
            k_end = min(n_row, k + int(16 / ts))

            # Aggregate hourly flowrates to daily estimates
            qot_bdo_est[i] = np.sum(np.nan_to_num(qo_sc_est[k_start:k_end].sum(axis=1))) * ts
            qwt_bdo_est[i] = np.sum(np.nan_to_num(qw_sc_est[k_start:k_end].sum(axis=1))) * ts
            qgt_bdo_est[i] = np.sum(np.nan_to_num(qg_sc_est[k_start:k_end].sum(axis=1))) * ts

    # Extract actual BDO flowrates
    qot_bdo = data_bdo['Qo_SC'][:n_bdo].values
    qgt_bdo = data_bdo['Qg_SC'][:n_bdo].values
    qwt_bdo = data_bdo['Qw_SC'][:n_bdo].values

    # Calculate Percent Relative Errors (PRE)
    pre_qo_pi = (qot_pi_est - data_vfm['Qo_SC']) / data_vfm['Qo_SC'] * 100
    pre_qg_pi = (qgt_pi_est - data_vfm['Qg_SC']) / data_vfm['Qg_SC'] * 100
    pre_qo_bdo = (qot_bdo_est - qot_bdo) / qot_bdo * 100
    pre_qg_bdo = (qgt_bdo_est - qgt_bdo) / qgt_bdo * 100
    pre_qw_bdo = (qwt_bdo_est - qwt_bdo) / qwt_bdo * 100

    # Define positions for Mean Absolute Percentage Error (MAPE) calculation
    def valid_positions(arr1, arr2):
        return ~np.isnan(arr1) & ~np.isnan(arr2) & (np.abs(arr1) < 100)

    pos_mape11 = valid_positions(pre_qo_pi, data_vfm['Qo_SC'])
    pos_mape21 = valid_positions(pre_qg_pi, data_vfm['Qg_SC'])
    pos_mape12 = valid_positions(pre_qo_bdo, qot_bdo)
    pos_mape22 = valid_positions(pre_qg_bdo, qgt_bdo)
    pos_mape32 = valid_positions(pre_qw_bdo, qwt_bdo)

    # Calculate MAPE values
    def safe_mean(arr):
        return np.mean(np.abs(arr)) if np.any(arr) else np.nan

    mape_q = np.array([
        [safe_mean(pre_qo_pi[pos_mape11]), safe_mean(pre_qo_bdo[pos_mape12])],
        [safe_mean(pre_qg_pi[pos_mape21]), safe_mean(pre_qg_bdo[pos_mape22])],
        [0, safe_mean(pre_qw_bdo[pos_mape32])]
    ])

    # Create results directory if not exists
    if not os.path.exists(dir_save):
        os.makedirs(dir_save)

    def plot_flowrate_comparison(est, actual, pre, ylabel, deviation, file_name):
        plt.figure(figsize=(12, 10))
        plt.subplot(2, 1, 1)
        plt.plot(est, '-k', label="Current model")
        plt.plot(actual, 'ob', label="BDO")
        plt.axhline(y=deviation, color='r', linestyle=':', label=f"+{deviation}% deviation")
        plt.axhline(y=-deviation, color='r', linestyle=':')
        plt.xlabel("Daily period")
        plt.ylabel(ylabel)
        plt.legend(loc="best")
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.plot(pre, '-k')
        plt.axhline(deviation, color='r', linestyle=':')
        plt.axhline(-deviation, color='r', linestyle=':')
        plt.xlabel("Daily period")
        plt.ylabel(f"PRE {ylabel} (%)")
        plt.grid(True)

        plt.tight_layout()
        plt.savefig(os.path.join(dir_save, file_name), dpi=300)
        plt.close()

    # Oil Flowrate
    plot_flowrate_comparison(qot_bdo_est, qot_bdo, pre_qo_bdo,
                             'Oil Flowrate [N m$^3$/d]', 10, "Oil_BDO.jpeg")

    # Gas Flowrate
    plot_flowrate_comparison(qgt_bdo_est, qgt_bdo, pre_qg_bdo,
                             'Gas Flowrate [N m$^3$/d]', 15, "Gas_BDO.jpeg")

    # Water Flowrate
    plot_flowrate_comparison(qwt_bdo_est, qwt_bdo, pre_qw_bdo,
                             'Water Flowrate [N m$^3$/d]', 30, "Water_BDO.jpeg")

    return (qot_pi_est, qgt_pi_est, qot_bdo_est, qgt_bdo_est, qwt_bdo_est, 
            pre_qo_pi, pre_qg_pi, pre_qo_bdo, pre_qg_bdo, pre_qw_bdo, mape_q)