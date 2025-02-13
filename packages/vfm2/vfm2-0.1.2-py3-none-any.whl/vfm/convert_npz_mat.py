import numpy as np
import scipy.io

def convert_npz_to_mat():
    """
    Converts a `.npz` file to a `.mat` file for MATLAB compatibility, handling
    jagged arrays, None values, and non-convertible data.

    Paths:
        Input: '/media/.../vfm_v2/vfm/Results/VFM_case/Results.npz'
        Output: '/media/.../vfm_v2/vfm/Results/VFM_case/results.mat'

    Cleaning Process:
        - Replaces None with NaN at all levels.
        - Handles jagged arrays by padding, flattening, or converting to object arrays.
        - Logs and skips non-convertible keys.
    """
    input_path = '/media/torraca/Arquivos/vfm2_daniel/vfm_v2/vfm/Results/VFM_case/Results.npz'
    output_path = '/media/torraca/Arquivos/vfm2_daniel/vfm_v2/vfm/Results/VFM_case/results.mat'

    print(f"Loading NPZ file from: {input_path}")
    npz_file = np.load(input_path, allow_pickle=True)

    def clean_value(value):
        """
        Recursively cleans the input value:
        - Replaces None with NaN.
        - Handles jagged arrays by padding, flattening, or converting to object arrays.
        """
        if value is None:
            return np.nan
        elif isinstance(value, np.ndarray):
            if value.dtype == object:
                try:
                    # Handle jagged arrays
                    max_length = max(
                        len(item) if isinstance(item, (list, np.ndarray)) else 0
                        for item in value
                    )
                    padded_array = np.array([
                        np.pad(
                            np.array(item, dtype=float),
                            (0, max_length - len(item)),
                            mode='constant',
                            constant_values=np.nan
                        ) if isinstance(item, (list, np.ndarray)) else np.full(max_length, np.nan)
                        for item in value
                    ])
                    return padded_array
                except Exception as e:
                    print(f"Failed to pad jagged array: {e}. Saving as object array.")
                    # Fallback: Save as object array
                    return np.array([clean_value(item) for item in value], dtype=object)
            else:
                return value  # Already a valid NumPy array
        elif isinstance(value, (list, tuple)):
            # Convert lists and tuples to arrays
            return np.array([clean_value(v) for v in value], dtype=object)
        else:
            try:
                return np.array(value)
            except Exception as e:
                print(f"Skipping non-convertible value: {value} (Error: {e})")
                return np.nan

    print("Processing NPZ file contents...")
    npz_dict = {}
    for key in npz_file:
        try:
            value = npz_file[key]
            cleaned_value = clean_value(value)
            if cleaned_value is not None:
                npz_dict[key] = cleaned_value
            else:
                print(f"Skipping key '{key}' due to NoneType or incompatible data.")
        except Exception as e:
            print(f"Error processing key '{key}': {e}")

    print(f"Saving MAT file to: {output_path}")
    try:
        scipy.io.savemat(output_path, npz_dict)
        print("Conversion completed successfully.")
    except Exception as e:
        print(f"Error saving .mat file: {e}")

if __name__ == "__main__":
    convert_npz_to_mat()
