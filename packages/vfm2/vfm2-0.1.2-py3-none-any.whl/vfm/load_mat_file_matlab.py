import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def load_and_display_mat_file(file_path):
    """
    Load and display the contents of a .mat file.

    Parameters:
    file_path (str): The path to the .mat file to be loaded.

    Functionality:
    - Loads the .mat file using `scipy.io.loadmat`.
    - Lists all the variables present in the file.
    - Iterates through each variable:
        - Skips internal metadata entries (those starting with '__').
        - Prints the name and content of the variable.
        - If the variable is a NumPy array:
            - Plots 2D arrays using `imshow` with a colorbar.
            - Plots 1D arrays using `plot`.

    Note:
    This function assumes the data in the .mat file can be visualized as either 1D or 2D arrays. For more complex data
    structures, additional handling may be required.

    Example:
    load_and_display_mat_file('/home/.../Results.mat')
    """
    # Load the .mat file
    mat_file = scipy.io.loadmat(file_path)

    # List all variables in the .mat file
    print("Variables in the file:", mat_file.keys())

    # Iterate over each variable and print its content
    for var_name in mat_file:
        # Skip internal metadata entries, which start with '__'
        if var_name.startswith('__'):
            continue
        data = mat_file[var_name]
        
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

    print("All variables have been printed.")

# Example usage:
# load_and_display_mat_file('/home/.../Results.mat')
