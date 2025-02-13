import sys
import time
import cProfile
import pstats

def main():
    """
    Main function to initialize and execute the VFMProcessor with profiling and execution time measurement.

    This function performs the following steps:
    1. Adds the required module directory to the system path.
    2. Imports and initializes the VFMProcessor class with specified parameters.
    3. Profiles the execution of the VFMProcessor to identify time-consuming functions.
    4. Measures and prints the total execution time.

    Parameters:
    - data_dir (str): Directory containing input data files for the VFMProcessor.
    - results_dir (str): Directory to save the VFMProcessor results.
    - flag_init (int): Initialization flag for VFMProcessor (valid range: [0, 3]).
    - flag_code (int): Code flag for specific behaviour in VFMProcessor (recommended: 3).

    This function profiles the execution of specific functions (DelumpingMethod and VFM) and calculates
    the mean execution time per iteration.

    Example Usage:
    main()
    """

    # Start measuring time
    start_time = time.time()

    # Step 1: Add the required module directory to the system path
    sys.path.append('/.../Arquivos/.../vfm_v2')

    # Step 2: Import and initialize the VFMProcessor
    from main_VFM_var import VFMProcessor

    data_dir = "/.../vfm_v2/vfm/Data"
    results_dir = "/.../vfm_v2/vfm/Results/VFM_case"
    flag_init = 3  # Ensure this value is within the range [0, 3]
    flag_code = 3  # Recommended value: 3

    # User-defined preprocessing flags
    apply_hampel = True # Enable Hampel filter for outlier detection
    apply_moving_avg = True  # Enable moving average smoothing
    replace_invalid = True  # Replace invalid values (NaN, Inf)

    # Step 3: Profile the VFMProcessor execution
    profiler = cProfile.Profile()
    profiler.enable()

    # Initialize the VFMProcessor with user-defined preprocessing options
    vfm_processor = VFMProcessor(
        data_dir,
        results_dir,
        flag_init,
        flag_code,
        apply_hampel=apply_hampel,
        apply_moving_avg=apply_moving_avg,
        replace_invalid=replace_invalid
    )

    profiler.disable()

    stats = pstats.Stats(profiler).sort_stats('tottime')

    # stats.print_stats(10)  # Print the top 10 time-consuming functions

    # Filter specific functions
    print("\nFiltered results for DelumpingMethod and VFM:")
    stats.print_stats('DelumpingMethod')
    stats.print_stats('VFM')

    # Retrieve total time and number of calls for DelumpingMethod and VFM
    delumping_time = 0
    delumping_calls = 0
    vfm_time = 0
    vfm_calls = 0

    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        if 'DelumpingMethod' in func[2]:
            delumping_time += tt
            delumping_calls += nc
        elif 'VFM' in func[2]:
            vfm_time += tt
            vfm_calls += nc

    # Calculate mean times
    mean_delumping_time = delumping_time / delumping_calls if delumping_calls > 0 else 0
    mean_vfm_time = vfm_time / vfm_calls if vfm_calls > 0 else 0

    print(f"\nTotal DelumpingMethod Time: {delumping_time:.2f} seconds, Calls: {delumping_calls}, Mean Time: {mean_delumping_time:.10f} seconds")
    print(f"Total VFM Time: {vfm_time:.2f} seconds, Calls: {vfm_calls}, Mean Time: {mean_vfm_time:.10f} seconds")    

    # Step 4: End measuring time
    end_time = time.time()

    # Calculate and print the total execution time
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time:.2f} seconds")

# Run the main function
if __name__ == "__main__":
    main()
