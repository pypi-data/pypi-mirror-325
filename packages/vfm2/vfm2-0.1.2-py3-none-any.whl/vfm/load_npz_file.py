import numpy as np
import matplotlib.pyplot as plt

def load_and_display_npz_file(file_path):
    """
    Load and display the contents of a .npz file.

    Parameters:
    file_path (str): The path to the .npz file to be loaded.

    Functionality:
    - Loads the .npz file using `numpy.load`.
    - Lists all the variables present in the file.
    - Iterates through each variable:
        - Prints the name and content of the variable.
        - If the variable is a NumPy array:
            - Plots 2D arrays using `imshow` with a colorbar.
            - Plots 1D arrays using `plot`.
    - Closes the .npz file after processing.

    Note:
    This function assumes the data in the .npz file can be visualized as either 1D or 2D arrays. 
    For more complex data structures, additional handling may be required.

    Example:
    load_and_display_npz_file('/path/to/your/file.npz')
    """
    # Load the .npz file
    npz_file = np.load(file_path, allow_pickle=True)

    # List all variables in the .npz file
    print("Variables in the .npz file:", npz_file.files)

    # Iterate over each variable and print its content
    for var_name in npz_file.files:
        try:
            # Load the data for the variable
            data = npz_file[var_name]
            
            # Print variable name and its content
            print(f"\nData for '{var_name}':\n", data)

            # If the data is plot-worthy (e.g., 1D or 2D arrays), plot it
            if isinstance(data, np.ndarray):
                if data.ndim == 2:  # For 2D arrays
                    plt.figure()
                    plt.imshow(data, aspect='auto')
                    plt.colorbar()
                    plt.title(var_name)
                    plt.show()
                elif data.ndim == 1:  # For 1D arrays
                    plt.figure()
                    plt.plot(data)
                    plt.title(var_name)
                    plt.show()
        except Exception as e:
            print(f"Could not load data for '{var_name}': {e}")

    print("All variables have been printed.")

    # Close the .npz file after loading its content
    npz_file.close()

# Example usage:
# load_and_display_npz_file('/media/.../vfm_v2/vfm/Results/VFM_case/Results.npz')
