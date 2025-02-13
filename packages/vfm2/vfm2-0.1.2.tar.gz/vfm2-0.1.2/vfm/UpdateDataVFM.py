import os
import numpy as np
import pandas as pd

class DataImporter:
    """
    A class to import, process, and save well data from multiple sources.

    Attributes:
    - data_directory (str): Path to the directory containing data files.
    - wells (list): List of well identifiers.
    - data_btp (dict): Dictionary to store BTP data for each well.
    - data_pi (dict): Dictionary to store PI data for each well and common variables.
    - data_well_specific (dict): Dictionary to store well-specific PI and RWT data for each well.
    - data_bdo (dict): Dictionary to store BDO data.

    Methods:
    - read_btp_data(): Reads and processes BTP data from a CSV file.
    - read_pi_data(): Reads and processes PI data from a CSV file.
    - read_bdo_data(): Reads and processes BDO data from a CSV file.
    - ensure_consistent_lengths(): Ensures consistent array lengths across data for compatibility.
    - safe_float_conversion(value): Safely converts values to floats, handling strings and errors.
    - save_data(): Saves processed PI and BDO data to Excel and CSV files.
    - read_and_process_data(): Orchestrates the data reading, processing, and saving.

    Example usage:
    data_importer = DataImporter(data_directory="/path/to/data/")
    data_importer.read_and_process_data()
    """
    def __init__(self, data_directory):
        """
        Initializes the DataImporter class with the specified data directory.

        Parameters:
        - data_directory (str): Path to the directory containing data files.
        """
        self.data_directory = data_directory
        self.wells = ['RJS-680', 'LL-60', 'LL-69', 'LL-90', 'LL-97', 'LL-100', 'LL-102']
        self.data_btp = {well: {} for well in self.wells}
        self.data_pi = {'Time': [], 'P_sep': [], 'Qo_SC': [], 'Qg_SC': []}
        self.data_well_specific = {
            well: {
                'DeltaPManifold_PI': [], 'DeltaPManifold_RWT': [], 'P_ds_SDV_PI': [], 'P_us_PI': [], 'T_us_PI': [],
                'u_PI': [], 'Qgi_PI': [], 'TimeBTP': [], 'P_us_RWT': [], 'T_us_RWT': [], 'u_RWT': [], 'Qgi_RWT': [],
                'P_ds_SDV_RWT': [], 'rhoo_SC': []
            } for well in self.wells
        }
        self.data_bdo = {'Time': [], 'Ql_SC': [], 'Qo_SC': [], 'Qg_SC': [], 'Qw_SC': []}

    def read_btp_data(self):
        """
        Reads and processes BTP data from 'BTP_Data.csv'.

        - Adjusts column names for consistency.
        - Filters and organizes data by well.

        Raises:
        - FileNotFoundError: If 'BTP_Data.csv' is not found.
        """
        btp_path = os.path.join(self.data_directory, 'BTP_Data.csv')
        aux = pd.read_csv(btp_path, delimiter=',', encoding='utf-8-sig')
        print("BTP_Data.csv columns:", aux.columns)

        aux['Time'] = pd.to_datetime(aux['Time'], dayfirst=True)
        aux.columns = [col.replace('Bo_inv', 'Bo').replace('PusChoke', 'P_us').replace('TusChoke', 'T_us').replace('Unnamed: 32', 'MolarMass') for col in aux.columns]
        aux = aux.drop(columns=['Unnamed: 33'])

        for _, row in aux.iterrows():
            well = row['Well']
            if well in self.wells:
                for col in aux.columns:
                    if col not in self.data_btp[well]:
                        self.data_btp[well][col] = []
                    self.data_btp[well][col].append(row[col])
        print(f"BTP data processed for wells: {self.wells}")

    def read_pi_data(self):
        """
        Reads and processes PI data from 'Data_PI.csv'.

        - Separates common columns for all wells.
        - Processes well-specific data, removing unnecessary prefixes.

        Raises:
        - FileNotFoundError: If 'Data_PI.csv' is not found.
        """
        # Load the CSV file, specifying the correct delimiter as semicolon
        pi_path = os.path.join(self.data_directory, 'Data_PI.csv')
        aux = pd.read_csv(pi_path, delimiter=';', encoding='utf-8-sig')
        print("Data_PI.csv columns:", aux.columns)

        # Separate common columns (P_sep, Qo_SC, Qg_SC) and add them to each well's data
        common_columns = ['Time', 'P_sep', 'Qo_SC', 'Qg_SC']

        for well in self.wells:
            # Filter the well-specific columns (excluding 'Fc_{well}' columns)
            well_columns = [
                'DeltaPManifold_PI', 'DeltaPManifold_RWT', 'P_ds_SDV_PI', 'P_us_PI', 'T_us_PI', 'u_PI',
                'Qgi_PI', 'TimeBTP', 'P_us_RWT', 'T_us_RWT', 'u_RWT', 'Qgi_RWT', 'P_ds_SDV_RWT', 'rhoo_SC'
            ]

            # Full list of expected columns for the well
            well_columns_full = common_columns + [f'{col}_{well}' for col in well_columns]

            # Extract relevant columns for each well, excluding any 'Fc_{well}' columns
            selected_columns = common_columns + [col for col in aux.columns if col.endswith(f'_{well}') and not col.startswith('Fc_')]

            # Extract the data for the well
            well_df = aux[selected_columns].copy()

            # Rename the well-specific columns to match the desired format by removing the well suffix
            new_column_names = common_columns + [col.replace(f'_{well}', '') for col in well_columns]
            well_df.columns = new_column_names

            # Convert 'Time' and 'TimeBTP' columns to datetime format without forcing to strings
            well_df['Time'] = pd.to_datetime(well_df['Time'])
            well_df['TimeBTP'] = pd.to_datetime(well_df['TimeBTP'])

            # Store the processed data for the well
            self.data_pi[well] = well_df

        print(f"PI data processed for wells: {self.wells}")
        
    def read_bdo_data(self):
        """
        Reads and processes BDO data from 'BDO_Data.csv'.

        - Converts 'Time' to datetime format.
        - Calculates water flow rate (Qw_SC).

        Raises:
        - FileNotFoundError: If 'BDO_Data.csv' is not found.
        """
        bdo_path = os.path.join(self.data_directory, 'BDO_Data.csv')
        aux = pd.read_csv(bdo_path, delimiter=';', decimal=',', encoding='utf-8-sig')
        print("BDO_Data.csv columns:", aux.columns)

        aux['Time'] = pd.to_datetime(aux['Time'], dayfirst=True, errors='coerce')

        for _, row in aux.iterrows():
            self.data_bdo['Time'].append(pd.to_datetime(row['Time'], dayfirst=True))
            self.data_bdo['Ql_SC'].append(self.safe_float_conversion(row['Ql_SC']))
            self.data_bdo['Qo_SC'].append(self.safe_float_conversion(row['Qo_SC']))
            self.data_bdo['Qg_SC'].append(self.safe_float_conversion(row['Qg_SC']))
            self.data_bdo['Qw_SC'].append(self.safe_float_conversion(row['Ql_SC']) - self.safe_float_conversion(row['Qo_SC']))
        print("BDO data processing completed.")

    def ensure_consistent_lengths(self):
        """
        Ensures all data lists have consistent lengths by padding shorter lists with NaN.
        """
        max_length = max(len(self.data_pi[key]) for key in self.data_pi)
        for key in self.data_pi:
            if len(self.data_pi[key]) < max_length:
                self.data_pi[key].extend([np.nan] * (max_length - len(self.data_pi[key])))

        for well in self.wells:
            lengths = {key: len(self.data_well_specific[well][key]) for key in self.data_well_specific[well]}
            # print(f"Lengths for well {well}: {lengths}")
            max_length = max(lengths.values())
            for key in self.data_well_specific[well]:
                if len(self.data_well_specific[well][key]) < max_length:
                    self.data_well_specific[well][key].extend([np.nan] * (max_length - len(self.data_well_specific[well][key])))

    def safe_float_conversion(self, value):
        """
        Safely converts a value to a float, handling strings and invalid inputs.

        Parameters:
        - value: The value to convert.

        Returns:
        - float: The converted value, or NaN if conversion fails.
        """
        if isinstance(value, str):
            value = value.replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return float('nan')

    def save_data(self):
        """
        Saves processed PI and BDO data to Excel and CSV files.
        """
        # Save data_pi to Excel file with each well in a separate sheet
        with pd.ExcelWriter(os.path.join(self.data_directory, 'Data_PI.xlsx'), engine='openpyxl') as writer:
            for well in self.wells:
                well_df = self.data_pi[well]
                well_df['Wells'] = well  # Add the 'Wells' column
                well_df = well_df[['Time', 'Wells'] + well_df.columns.tolist()[1:-1]]  # Reorder columns as needed
                well_df.to_excel(writer, sheet_name=well, index=False)
        print("PI data saved to Excel.")

        # Save data_bdo to CSV
        bdo_df = pd.DataFrame(self.data_bdo)
        bdo_df.to_csv(os.path.join(self.data_directory, 'Data_BDO.csv'), index=False, sep=';')
        print("BDO data saved to CSV.")

    def read_and_process_data(self):
        """
        Reads, processes, and saves data from all sources (BTP, PI, BDO).
        """
        self.read_btp_data()
        self.read_pi_data()
        self.read_bdo_data()
        self.ensure_consistent_lengths()
        self.save_data()
