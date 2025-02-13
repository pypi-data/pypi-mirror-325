import os
import numpy as np
import pandas as pd
from datetime import datetime
from vfm.VFM import VFM
from vfm.GetDataPure import GetDataPure
from vfm.ExtendCG import ExtendCG
from vfm.Plotting_VFM import plotting_vfm_v2
from hampel import hampel  # Import Hampel filter
import time

class VFMProcessor:
    """
    A class to process and calculate data for the Virtual Flow Meter (VFM) algorithm.

    Attributes:
        data_directory (str): Directory containing the input data files.
        results_directory (str): Directory to save the processed results.
        flag_init (int): Initialization flag for the processing logic.
        flag_code (int): Code to specify the type of processing.
        wells (list): List of wells to be processed.
        SGw (float): Global specific gravity of water.
        btp_data (dict): Preprocessed BTP data for each well.
        pi_data (dict): Preprocessed PI data for each well.
        bdo_data (pd.DataFrame): Preprocessed BDO data.
    """
    def __init__(self, data_directory, results_directory, flag_init, flag_code,
                 apply_hampel=False, apply_moving_avg=False, replace_invalid=False):
        """
        Initialize the VFMProcessor with input parameters and preprocessing options.

        Args:
            data_directory (str): Path to the directory containing input data files.
            results_directory (str): Path to the directory to save results.
            flag_init (int): Initialization flag for processing logic.
            flag_code (int): Code to define specific processing behavior.
            apply_hampel (bool): Whether to apply the Hampel filter during preprocessing.
            apply_moving_avg (bool): Whether to apply moving average smoothing.
            replace_invalid (bool): Whether to replace invalid values during preprocessing.
        """
        self.data_directory = data_directory
        self.results_directory = results_directory
        self.flag_init = flag_init
        self.flag_code = flag_code
        self.apply_hampel = apply_hampel
        self.apply_moving_avg = apply_moving_avg
        self.replace_invalid = replace_invalid
        self.wells = ['RJS-680', 'LL-60', 'LL-69', 'LL-90', 'LL-97', 'LL-100', 'LL-102']
        # self.wells = ['RJS-680'] 

        self.SGw = 1.040  # Define SGw globally

        self.load_data()
        self.process_data()

    def preprocess_data(self, df, fill_value=0):
        """
        Preprocess the given DataFrame by filling missing values, sorting, and deduplicating.

        Args:
            df (pd.DataFrame): Input data to preprocess.
            required_columns (list): List of required columns. Rows missing these will be dropped.
            fill_value (float): Value to fill missing or invalid data.

        Returns:
            pd.DataFrame: Preprocessed DataFrame.
        """
        df = df.copy()  # Work with a copy to avoid SettingWithCopyWarning

        # Drop rows with missing 'Time' or non-convertible 'Time'
        df.dropna(subset=['Time'], inplace=True)

        # Forward-fill and back-fill missing values
        df.ffill(inplace=True)
        df.bfill(inplace=True)

        # Remove duplicates based on 'Time'
        df.sort_values(by='Time', inplace=True)
        df.drop_duplicates(subset=['Time'], inplace=True)

        return df

    
    def apply_hampel_filter(self, df, columns, window_size=3, n_sigma=1.5):
        """
        Apply the Hampel filter to specified columns of a DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.
            columns (list): List of column names to apply the Hampel filter.
            window_size (int): Window size for the Hampel filter.
            n_sigma (float): Threshold for outlier detection.

        Returns:
            pd.DataFrame: DataFrame with filtered columns.
        """
        # for col in columns:
        #     if col in df.columns:
        #         result = hampel(df[col], window_size=window_size, n_sigma=n_sigma)
        #         df[col] = result.filtered_data
        for col in columns:
            if col in df.columns:
                # Ensure the column is numeric and apply the Hampel filter
                series = df[col].values
                n = len(series)
                k = 1.4826  # Scale factor for Gaussian distribution
                half_window = window_size // 2
                
                # Initialize the filtered data array
                filtered_data = series.copy()
                
                for i in range(n):
                    # Define the window bounds
                    start = max(0, i - half_window)
                    end = min(n, i + half_window + 1)
                    
                    # Calculate median and MAD
                    window_data = series[start:end]
                    median = np.median(window_data)
                    mad = k * np.median(np.abs(window_data - median))
                    
                    # Detect and replace outliers
                    if mad > 0 and abs(series[i] - median) > n_sigma * mad:
                        filtered_data[i] = median  # Replace outlier with median
                
                # Update the DataFrame with the filtered column
                df[col] = filtered_data
        return df

    def apply_moving_average(self, df, columns, window_size=5):
        """
        Apply a moving average to specified columns of a DataFrame.

        Args:
            df (pd.DataFrame): Input DataFrame.
            columns (list): List of column names to apply the moving average.
            window_size (int): Size of the moving average window.

        Returns:
            pd.DataFrame: DataFrame with smoothed columns.
        """
        for col in columns:
            if col in df.columns:
                df[col] = df[col].rolling(window=window_size, min_periods=1).mean()
        return df


    def replace_invalid_values(self, df, columns, default=0):
        """
        Replace NaN or Inf in the specified columns of a DataFrame with a default value.

        Args:
            df (pd.DataFrame): Input DataFrame.
            columns (list): Columns to check and replace values.
            default (float): Value to replace NaN/Inf.

        Returns:
            pd.DataFrame: Cleaned DataFrame.
        """
        for col in columns:
            if col in df.columns:
                df[col] = df[col].replace([np.inf, -np.inf], np.nan).fillna(default)
        return df

    def load_data(self):
        """
        Load and preprocess input data from the specified directory, including Hampel filtering
        and moving average smoothing.

        Raises:
            KeyError: If required columns are missing from input files.
        """
        btp_file_path = os.path.join(self.data_directory, 'Data_BTP.xlsx')
        pi_file_path = os.path.join(self.data_directory, 'Data_PI.xlsx')
        bdo_file_path = os.path.join(self.data_directory, 'Data_BDO.csv')

        self.btp_data = {}
        self.pi_data = {}

        for well in self.wells:
            # Preprocess BTP data
            btp_df = pd.read_excel(btp_file_path, sheet_name=well)

            # Optionally apply preprocessing steps
            if self.replace_invalid:
                btp_df = self.replace_invalid_values(btp_df, btp_df.columns)
            if self.apply_hampel:
                numeric_columns_btp = btp_df.select_dtypes(include=np.number).columns.tolist()
                btp_df = self.apply_hampel_filter(btp_df, columns=numeric_columns_btp)
            if self.apply_moving_avg:
                numeric_columns_btp = btp_df.select_dtypes(include=np.number).columns.tolist()
                btp_df = self.apply_moving_average(btp_df, columns=numeric_columns_btp)

            # Process time column and add preprocessed BTP data to dictionary
            self.btp_data[well] = self.preprocess_data(btp_df)
            self.btp_data[well]['Time'] = pd.to_datetime(
                self.btp_data[well]['Time'], format='%Y-%m-%d %H:%M:%S', dayfirst=False, errors='coerce'
            )

            # Preprocess PI data
            pi_df = pd.read_excel(pi_file_path, sheet_name=well)

            if self.replace_invalid:
                pi_df = self.replace_invalid_values(pi_df, pi_df.columns)
            if self.apply_hampel:
                numeric_columns_pi = pi_df.select_dtypes(include=np.number).columns.tolist()
                pi_df = self.apply_hampel_filter(pi_df, columns=numeric_columns_pi)
            if self.apply_moving_avg:
                numeric_columns_pi = pi_df.select_dtypes(include=np.number).columns.tolist()
                pi_df = self.apply_moving_average(pi_df, columns=numeric_columns_pi)

            # Process time column and add preprocessed PI data to dictionary
            self.pi_data[well] = self.preprocess_data(pi_df)
            self.pi_data[well]['Time'] = pd.to_datetime(
                self.pi_data[well]['Time'], format='%Y-%m-%d %H:%M:%S', dayfirst=False, errors='coerce'
            )

            # Debugging: Check time intervals after filtering and smoothing
            pi_time_diff = self.pi_data[well]['Time'].diff().dt.total_seconds().dropna()
            print(f"PI data time intervals for well {well}: {pi_time_diff.unique()}")

        # Preprocess BDO data
        bdo_df = pd.read_csv(bdo_file_path, delimiter=';', decimal=',')

        if self.replace_invalid:
            bdo_df = self.replace_invalid_values(bdo_df, bdo_df.columns)
        if self.apply_hampel:
            numeric_columns_bdo = bdo_df.select_dtypes(include=np.number).columns.tolist()
            bdo_df = self.apply_hampel_filter(bdo_df, columns=numeric_columns_bdo)
        if self.apply_moving_avg:
            numeric_columns_bdo = bdo_df.select_dtypes(include=np.number).columns.tolist()
            bdo_df = self.apply_moving_average(bdo_df, columns=numeric_columns_bdo)

        # Process time column and add preprocessed BDO data to attribute
        self.bdo_data = self.preprocess_data(bdo_df)
        self.bdo_data['Time'] = pd.to_datetime(
            self.bdo_data['Time'], format='%Y-%m-%d', dayfirst=False, errors='coerce'
        )

    def process_data(self):
        """
        Perform data processing and calculations for the VFM algorithm.

        Raises:
            KeyError: If required columns are missing from the data.
            ValueError: If inconsistencies are found in the data.
        """
        required_columns = [
            'Rhoo_SC', 'Qo_SC', 'Qg_SC', 'Qw_SC', 'SGg', 'T_sep', 'P_sep'
        ]

        # Check data availability for each well
        for well in self.wells:
            missing_columns = [col for col in required_columns if col not in self.btp_data[well].columns]
            if missing_columns:
                raise KeyError(f"Missing columns in btp_data for well {well}: {missing_columns}")

            time_diff = self.pi_data[well]['Time'].diff().dt.total_seconds().dropna()
            if time_diff.min() <= 0:
                print(f"Error: Non-positive time interval found in 'Time' column of PI data for well {well}.")
            else:
                print(f"Minimum time interval for well {well}: {time_diff.min()} seconds")

        # Define the number of time steps and wells
        n_rows = len(self.pi_data[self.wells[0]]['Time'])
        n_wells = len(self.wells)

        # Initialize arrays with dimensions (n_rows, n_wells)
        T_us_PI = np.full((n_rows, n_wells), np.nan)
        P_us_PI = np.full((n_rows, n_wells), np.nan)
        P_ds_SDV_PI = np.full((n_rows, n_wells), np.nan)
        DeltaPManifold_PI = np.full((n_rows, n_wells), np.nan)
        Qgi_PI = np.full((n_rows, n_wells), np.nan)
        u_PI = np.full((n_rows, n_wells), np.nan)
        u_RWT = np.full((n_rows, n_wells), np.nan)
        Fc = np.full((n_rows, n_wells), np.nan)
        T_us_RWT = np.full((n_rows, n_wells), np.nan)
        P_us_RWT = np.full((n_rows, n_wells), np.nan)
        P_ds_SDV_RWT = np.full((n_rows, n_wells), np.nan)
        DeltaPManifold_RWT = np.full((n_rows, n_wells), np.nan)
        Qgi_RWT = np.full((n_rows, n_wells), np.nan)

        for j, well in enumerate(self.wells):
        # for well in ['RJS-680']:

            # print(self.pi_data[well]['TimeBTP'])
        
            if 'TimeBTP' in self.pi_data[well]:

                self.pi_data[well]['TimeBTP'] = pd.to_datetime(self.pi_data[well]['TimeBTP'], errors='coerce')
                
            else:
                # print(f"Error: 'TimeBTP' column not found in pi_data for well {well}")
                continue

            # Fill these arrays using the data for each well    
            T_us_PI[:, j] = self.pi_data[well]['T_us_PI'].values
            P_us_PI[:, j] = self.pi_data[well]['P_us_PI'].values
            P_ds_SDV_PI[:, j] = self.pi_data[well]['P_ds_SDV_PI'].values
            DeltaPManifold_PI[:, j] = self.pi_data[well]['DeltaPManifold_PI'].values
            Qgi_PI[:, j] = self.pi_data[well]['Qgi_PI'].values
            u_PI[:, j] = self.pi_data[well]['u_PI'].values
            u_RWT[:, j] = self.pi_data[well]['u_RWT'].values
            Fc[:, j] = self.pi_data[well]['P_us_RWT'].values / self.pi_data[well]['P_us_PI'].values
            T_us_RWT[:, j] = self.pi_data[well]['T_us_RWT'].values
            P_us_RWT[:, j] = self.pi_data[well]['P_us_RWT'].values
            P_ds_SDV_RWT[:, j] = self.pi_data[well]['P_ds_SDV_RWT'].values
            DeltaPManifold_RWT[:, j] = self.pi_data[well]['DeltaPManifold_RWT'].values
            Qgi_RWT[:, j] = self.pi_data[well]['Qgi_RWT'].values

        P_ds_PI = P_ds_SDV_PI + DeltaPManifold_PI
        P_us_SDV = P_ds_SDV_RWT
        P_ds_RWT = P_us_SDV + DeltaPManifold_RWT
        T_us_PI = T_us_PI + 273.15
        T_us_RWT = T_us_RWT + 273.15
        P_us_PI = P_us_PI * 0.01
        P_us_RWT = P_us_RWT * 0.01
        P_ds_PI = P_ds_PI * 0.01
        P_ds_RWT = P_ds_RWT * 0.01
        opening_PI = u_PI / 100
        opening_RWT = u_RWT / 100

        n_pi = len(self.pi_data[well]['Time'].values)
        # print(f"Processing well {well}: n_btp = {len(self.btp_data[well]['Time'])}, n_pi = {n_pi}")

        Tag = ["N2", "CO2", "C1", "C2", "C3", "iC4", "nC4", "iC5", "nC5", "nC6", "nC7", "nC8", "nC9", "nC10"]
        PureProperties = GetDataPure(Tag)

        Qg_SC = np.full((n_rows, n_wells), np.nan)
        Qo_SC = np.full((n_rows, n_wells), np.nan)
        Qw_SC = np.full((n_rows, n_wells), np.nan)
        Ql_SC = np.full((n_rows, n_wells), np.nan)
        BSW = np.empty((n_rows, n_wells), dtype=object)
        GOR = np.empty((n_rows, n_wells), dtype=object)
        SGg = np.empty((n_rows, n_wells), dtype=object)
        T_sep = np.empty((n_rows, n_wells), dtype=object)
        P_sep = np.empty((n_rows, n_wells), dtype=object)
        y = np.empty((n_rows, n_wells), dtype=object)

        T_us_est = np.full((n_rows, n_wells), np.nan)
        P_us_est = np.full((n_rows, n_wells), np.nan)
        P_ds_est = np.full((n_rows, n_wells), np.nan)
        Qgi_est = np.full((n_rows, n_wells), np.nan)
        opening_est = np.full((n_rows, n_wells), np.nan)
        Fc_est = np.full((n_rows, n_wells), np.nan)


        # Adjust variables for further use in calculations
        P_ds_est = P_ds_PI.copy()
        P_us_est = P_us_PI.copy()
        T_us_est = T_us_PI.copy()
        Fc_est = Fc.copy()
        opening_est = opening_PI.copy()
        Qgi_est = Qgi_PI.copy()

        self.Cv_est = np.full((n_rows, n_wells), np.nan)
        self.Cv_gpm_est = np.full((n_rows, n_wells), np.nan)
        self.Qw_SC_est = np.full((n_rows, n_wells), np.nan)
        self.Qo_SC_est = np.full((n_rows, n_wells), np.nan)
        self.Qg_SC_est = np.full((n_rows, n_wells), np.nan)
        self.API_est = np.full((n_rows, n_wells), np.nan)
        self.GOR_est = np.full((n_rows, n_wells), np.nan)
        self.SGg_est = np.full((n_rows, n_wells), np.nan)
        self.z_est = np.empty((n_rows, n_wells), dtype=object)
        self.x_est = np.empty((n_rows, n_wells), dtype=object)
        self.y_est = np.empty((n_rows, n_wells), dtype=object)
        self.pseudo_est = np.empty((n_rows, n_wells), dtype=object)
        self.MW_vector = np.full((n_rows, n_wells), np.nan)
        self.FO_del = np.full((n_rows, n_wells), np.nan)

        # Iterate over wells to process their data
        for j, well in enumerate(self.wells):
            btp_time_series = self.btp_data[well]['Time'].reset_index(drop=True)
            pi_time_series = pd.Series(self.pi_data[well]['Time'].values.astype('datetime64[s]'))
            N_data_max = len(btp_time_series)

            # Initialize variables
            btp_index = 0  # Similar to 'k' in MATLAB code
            btp_indices = []  # To store valid BTP indices for each PI time

            # Track the last available BTP index
            last_valid_btp_index = None

            # Iterate over PI times
            for pi_time in pi_time_series:
                # Move forward in BTP series until a valid match is found
                while btp_index < N_data_max and btp_time_series[btp_index] < pi_time:
                    btp_index += 1

                # Check if btp_index is within the valid range
                if btp_index >= N_data_max:
                    if last_valid_btp_index is not None:
                        btp_indices.append(last_valid_btp_index)  # Use the last valid index
                    else:
                        btp_indices.append(None)  # No valid BTP time found
                else:
                    btp_indices.append(btp_index)  # Store the current index
                    last_valid_btp_index = btp_index  # Update the last valid index

            # Ensure btp_indices is the same length as pi_time_series
            if len(btp_indices) != len(pi_time_series):
                raise ValueError(f"Mismatch in length: btp_indices ({len(btp_indices)}) and pi_time_series ({len(pi_time_series)})")

            # Align data between PI and BTP
            for i, pi_time in enumerate(pi_time_series):
                if i >= len(btp_indices) or btp_indices[i] is None or btp_indices[i] >= len(self.btp_data[well]):
                    print(f"Skipping i = {i}, well {well}: no valid BTP index for PI Time = {pi_time}")
                    continue
                k = btp_indices[i]

                # Ensure k is within bounds
                if 0 <= k < len(self.btp_data[well]):
                    try:
                        Qg_SC[i, j] = self.btp_data[well]['Qg_SC'].iloc[k]
                        Qo_SC[i, j] = self.btp_data[well]['Qo_SC'].iloc[k]
                        Qw_SC[i, j] = self.btp_data[well]['Qw_SC'].iloc[k]
                        Ql_SC[i, j] = Qw_SC[i, j] + Qo_SC[i, j]
                        BSW[i, j] = Qw_SC[i, j] / Ql_SC[i, j]
                        GOR[i, j] = Qg_SC[i, j] / Qo_SC[i, j]
                    except IndexError:
                        print(f"IndexError at i = {i}, k = {k}, well = {well}")
                        continue
                else:
                    print(f"Skipping due to out-of-bound index: k={k}, i={i}, well={well}")

                # Adjust for gas solubility and composition based on the flag_code
                if self.flag_code == 1:
                    MWair = 28.97  # [kg/kmol]
                    SGg[i, j] = self.pi_data[well]['SGg'].iloc[i] / MWair
                    y[i, j] = ExtendCG(self.btp_data[well], PureProperties, k, j)
                else:
                    k = max(k - 1, 0)  # Adjust k as per MATLAB logic
                    y[i, j], SGg[i, j] = ExtendCG(self.btp_data[well], PureProperties, k, j)

                T_sep[i, j] = self.btp_data[well]['T_sep'].iloc[k]
                P_sep[i, j] = self.btp_data[well]['P_sep'].iloc[k]

            ts = (pi_time_series[1] - pi_time_series[0]).total_seconds() / (24 * 3600)
            inv_ts = int(1 / ts)
            inv_day = int(1 / (24 * ts))
    
            if ts == 0:
                raise ValueError("Time step (ts) calculated as zero, check the 'Time' column in data_vfm")
    
            pos_sim = list(range(len(pi_time_series)))
            pos_cont = 0
            pos_error = np.zeros((len(pi_time_series), len(self.wells)))
            pos_cons = np.zeros((len(pi_time_series), len(self.wells)))
            Time_BDO = self.bdo_data['Time']


        # Initialize an empty list to store execution times
        execution_times = []

                            
        if self.flag_init == 1:
            # Definition of BDO data used for validation
            Time_BDO = pd.date_range(start="2019-01-02", end="2019-12-02", freq='MS')
            n_BDO = len(Time_BDO)

            # Definition of PI data concurring with the BDO data
            k = 0
            pos_sim = []
            for i in range(n_BDO):
                while k < n_pi and pi_time_series[k] <= Time_BDO[i]:
                    k += 1
                # Define the range of positions for each monthly interval
                if k >= 1:
                    pos_start = max(k - int(7 / (ts * 24)), 0)  # k - 7 days as per MATLAB code
                    pos_end = min(k + int(16 / (ts * 24)), n_pi)  # k + 16 days as per MATLAB code
                    pos_sim.extend(range(pos_start, pos_end))

            # Convert pos_sim to a unique sorted list to avoid duplicates
            pos_sim = sorted(set(pos_sim))

            # Calculation of the VFM algorithm at the set of sampling times previously chosen
            for idx in pos_sim:
                for j, well in enumerate(self.wells):
                    if idx < n_pi and (idx + int(1 / ts)) <= n_pi:
                        # Calculate arithmetic means for the input variables over the interval
                        start_idx = idx
                        end_idx = idx + int(1 / ts)  # Corresponds to the time step

                        T_us_est[start_idx:end_idx, j] = np.mean(T_us_PI[start_idx:end_idx, j])
                        P_us_est[start_idx:end_idx, j] = np.mean(P_us_PI[start_idx:end_idx, j])
                        P_ds_est[start_idx:end_idx, j] = np.mean(P_ds_PI[start_idx:end_idx, j])
                        Qgi_est[start_idx:end_idx, j] = np.mean(Qgi_PI[start_idx:end_idx, j])
                        opening_est[start_idx:end_idx, j] = np.mean(opening_PI[start_idx:end_idx, j])
                        
                        if P_us_est[start_idx, j] != 0:
                            Fc_est[start_idx:end_idx, j] = P_us_RWT[start_idx, j] / P_us_est[start_idx, j]
                        else:
                            Fc_est[start_idx:end_idx, j] = np.nan

                        # Start measuring time
                        # start_time = time.time()

                        # Call the VFM function for each time step and well
                        results = VFM(
                            T_us_est[start_idx, j], T_us_RWT[start_idx, j], P_us_est[start_idx, j], P_us_RWT[start_idx, j],
                            P_ds_est[start_idx, j], P_ds_RWT[start_idx, j], Qgi_est[start_idx, j], Qgi_RWT[start_idx, j],
                            opening_est[start_idx, j], opening_RWT[start_idx, j], Fc_est[start_idx, j], 
                            self.pi_data[well]['rhoo_SC'].iloc[start_idx],
                            SGg[start_idx, j], self.SGw, GOR[start_idx, j], BSW[start_idx, j], Ql_SC[start_idx, j], 
                            PureProperties, y[start_idx, j], T_sep[start_idx, j], P_sep[start_idx, j], self.flag_code
                        )

                        # # End measuring time
                        # end_time = time.time()

                        # # Calculate and print the total execution time
                        # execution_time = end_time - start_time

                        # # Append to execution_times list
                        # execution_times.append(execution_time)

                        # Unpack the results and store in matrices
                        (Cv_est, Cv_gpm_est, Qw_SC_est, Qo_SC_est, Qg_SC_est, API_est, 
                        GOR_est, SGg_est, z_est, x_est, y_est, MW_vector, FO_del, 
                        pseudo_est) = results

                        # Store results for the full time interval
                        self.Cv_est[start_idx:end_idx, j] = Cv_est
                        self.Cv_gpm_est[start_idx:end_idx, j] = Cv_gpm_est
                        self.Qw_SC_est[start_idx:end_idx, j] = Qw_SC_est
                        self.Qo_SC_est[start_idx:end_idx, j] = Qo_SC_est
                        self.Qg_SC_est[start_idx:end_idx, j] = Qg_SC_est
                        self.API_est[start_idx:end_idx, j] = API_est
                        self.GOR_est[start_idx:end_idx, j] = GOR_est
                        self.SGg_est[start_idx:end_idx, j] = SGg_est
                        self.z_est[start_idx:end_idx, j] = z_est
                        self.x_est[start_idx:end_idx, j] = x_est
                        self.y_est[start_idx:end_idx, j] = y_est
                        self.MW_vector[start_idx:end_idx, j] = MW_vector
                        self.FO_del[start_idx:end_idx, j] = FO_del
                        self.pseudo_est[start_idx:end_idx, j] = pseudo_est

                        pos_cont += 1


        else:
            # for i in pos_sim:
            # for i in pos_sim[-17490:-1]:
            # for i in pos_sim[-2300:-1]:
            # for i in pos_sim[:2420]:
            for i in pos_sim[-3984:]: # comparison with MVM

                for j, well in enumerate(self.wells):
                    if self.flag_init == 3:
                        pos_min = 1e5
                        k = 0

                        # Adjust P_ds_est based on available data, considering fallback logic
                        while np.isnan(P_ds_PI[i - k, j]) or P_ds_PI[i - k, j] == 0:
                            if i - k == 0:
                                break
                            k += 1
                        P_ds_est[i, j] = P_ds_PI[i - k, j]
                        pos_min = min(pos_min, i - k)

                        # Adjust P_us_est based on fallback logic and constraints
                        k = 0
                        while np.isnan(P_us_PI[i - k, j]) or P_us_PI[i - k, j] == 0 or P_us_PI[i - k, j] > 200:
                            if i - k == 0:
                                break
                            k += 1
                        P_us_est[i, j] = P_us_PI[i - k, j]
                        pos_min = min(pos_min, i - k)

                        # Ensure P_us_est is not less than P_ds_est to avoid complex calculations
                        if P_us_est[i, j] < P_ds_est[i, j]:
                            P_us_est[i, j] = P_ds_est[i, j]

                        # Adjust T_us_est with fallback for invalid data
                        k = 0
                        while np.isnan(T_us_PI[i - k, j]) or T_us_PI[i - k, j] == 273.15:
                            if i - k == 0:
                                break
                            k += 1
                        T_us_est[i, j] = T_us_PI[i - k, j]
                        pos_min = min(pos_min, i - k)

                        # Adjust opening_est for missing or zero values with conditions
                        k = 0
                        while np.isnan(opening_PI[i - k, j]) or opening_PI[i - k, j] == 0:
                            if i - k == 0 or i >= n_pi - 3:
                                break
                            # Check for realistic closed valve behavior
                            if opening_PI[i - k, j] == 0 and (
                                P_us_PI[i + int(2 * inv_day), j] < P_us_PI[i, j] or
                                P_us_PI[i + int(3 * inv_day), j] < P_us_PI[i, j]
                            ):
                                break
                            k += 1
                        opening_est[i, j] = opening_PI[i - k, j]
                        pos_min = min(pos_min, i - k)

                        # Adjust Qgi_est with fallback for missing or out-of-range data
                        k = 0
                        while np.isnan(Qgi_PI[i - k, j]) or Qgi_PI[i - k, j] > 1000:
                            if i - k == 0:
                                break
                            k += 1
                        Qgi_est[i, j] = Qgi_PI[i - k, j]
                        pos_min = min(pos_min, i - k)

                    # Calculate Fc_est only if P_us_est is non-zero to avoid division by zero
                    if P_us_est[i, j] != 0:
                        Fc_est[i, j] = P_us_RWT[i, j] / P_us_est[i, j]
                    else:
                        Fc_est[i, j] = np.nan

                    try:

                        # # Start measuring time
                        # start_time = time.time()

                        # Call the VFM function with the appropriate parameters
                        results = VFM(
                            T_us_est[i, j], T_us_RWT[i, j], P_us_est[i, j], P_us_RWT[i, j],
                            P_ds_est[i, j], P_ds_RWT[i, j], Qgi_est[i, j], Qgi_RWT[i, j],
                            opening_est[i, j], opening_RWT[i, j], Fc_est[i, j],
                            self.pi_data[well]['rhoo_SC'].iloc[i],
                            SGg[i, j], self.SGw, GOR[i, j], BSW[i, j], Ql_SC[i, j], PureProperties,
                            y[i, j], T_sep[i, j], P_sep[i, j], self.flag_code
                        )
                        
                        # # End measuring time
                        # end_time = time.time()

                        # # Calculate the execution time
                        # execution_time = end_time - start_time

                        # # Append to execution_times list
                        # execution_times.append(execution_time)

                        # Unpack the results from the VFM function
                        (self.Cv_est[i, j], self.Cv_gpm_est[i, j], self.Qw_SC_est[i, j], self.Qo_SC_est[i, j],
                        self.Qg_SC_est[i, j], self.API_est[i, j], self.GOR_est[i, j], self.SGg_est[i, j],
                        self.z_est[i, j], self.x_est[i, j], self.y_est[i, j], self.MW_vector[i, j], self.FO_del[i, j],
                        self.pseudo_est[i, j]) = results

                        # Update counters and flags
                        pos_cont += 1
                        pos_cons[i, j] = i + j * n_rows  # Store the index of successful calculations

                    except Exception as e:
                        # In case of an error, mark the error and log it
                        pos_error[i, j] = 1
                        print(f"Error processing time step {i}, well {j}: {e}")

            # Filter the valid positions for further analysis
            pos_cons = np.argwhere(pos_cons > 0).flatten()

        if not os.path.exists(self.results_directory):
            os.makedirs(self.results_directory)

        # # After all loops, print the execution times
        # print("Execution times for all iterations:")
        # print(execution_times)


        # Perform the plotting of results

        # (Qot_PI_est, Qgt_PI_est, Qot_BDO_est, Qgt_BDO_est, Qwt_BDO_est,
        # PRE_Qo_PI, PRE_Qg_PI, PRE_Qo_BDO, PRE_Qg_BDO, PRE_Qw_BDO, MAPE_Q) = plotting_vfm_v2(
        #     self.pi_data[well], self.bdo_data, Time_BDO, self.Qw_SC_est, self.Qo_SC_est, self.Qg_SC_est,
        #     pos_sim, self.flag_init-1, self.results_directory
        # )

        # Calculate API for plotting delumping results
        rhow_SC = 1000  # [kg/m^3]
        API = 141.5 / (self.btp_data[well]['Rhoo_SC'].mean() / rhow_SC) - 131.5

        ########################################################################

        # np.savez(os.path.join(self.results_directory, "Results"), Cv_est=self.Cv_est, Cv_gpm_est=self.Cv_gpm_est, Qw_SC_est=self.Qw_SC_est, Qo_SC_est=self.Qo_SC_est, Qg_SC_est=self.Qg_SC_est,
        #          API_est=self.API_est, GOR_est=self.GOR_est, SGg_est=self.SGg_est, z_est=self.z_est, x_est=self.x_est, y_est=self.y_est, MW_vector=self.MW_vector,
        #          FO_del=self.FO_del, Qot_PI_est=Qot_PI_est, Qgt_PI_est=Qgt_PI_est, Qot_BDO_est=Qot_BDO_est, Qgt_BDO_est=Qgt_BDO_est,
        #          Qwt_BDO_est=Qwt_BDO_est, PRE_Qo_PI=PRE_Qo_PI, PRE_Qg_PI=PRE_Qg_PI, PRE_Qo_BDO=PRE_Qo_BDO, PRE_Qg_BDO=PRE_Qg_BDO,
        #          PRE_Qw_BDO=PRE_Qw_BDO, MAPE_Q=MAPE_Q, pos_sim=pos_sim, flag_init=self.flag_init, flag_code=self.flag_code)  

        np.savez(os.path.join(self.results_directory, "Results"), Cv_est=self.Cv_est, Cv_gpm_est=self.Cv_gpm_est, Qw_SC_est=self.Qw_SC_est, Qo_SC_est=self.Qo_SC_est, Qg_SC_est=self.Qg_SC_est,
                        API_est=self.API_est, GOR_est=self.GOR_est, SGg_est=self.SGg_est, z_est=self.z_est, x_est=self.x_est, y_est=self.y_est, MW_vector=self.MW_vector,
                        FO_del=self.FO_del, pos_sim=pos_sim, flag_init=self.flag_init, flag_code=self.flag_code) 