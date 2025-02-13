import pandas as pd
from UpdateDataVFM import DataImporter

def main():
    """
    Main function to load, process, and inspect VFM-related data.

    This function performs the following steps:
    1. Reads and inspects an Excel file containing configuration data.
    2. Initializes a DataImporter instance to process well data from multiple sources.
    3. Reads, processes, and saves the data using the DataImporter class.

    Files:
    - `Config_TAGS_PI-Daniel_PIDATALINK.xlsx`: Configuration file for tags.
    - Data files for BTP, PI, and BDO are processed by the DataImporter class.

    Example Usage:
    main()
    """

    # Step 1: Load and inspect the Excel configuration file
    pi_path = "/.../vfm_v2/vfm/Data/....xlsx"
    aux = pd.read_excel(pi_path)
    print("Loaded Excel configuration file. Columns:", aux.columns)

    # Step 2: Initialize the DataImporter with the data directory
    data_directory = "/.../vfm_v2/vfm/Data"
    data_importer = DataImporter(data_directory=data_directory)

    # Step 3: Read, process, and save the data using the DataImporter
    data_importer.read_and_process_data()
    print("Data processing completed successfully.")

# Run the main function
if __name__ == "__main__":
    main()
