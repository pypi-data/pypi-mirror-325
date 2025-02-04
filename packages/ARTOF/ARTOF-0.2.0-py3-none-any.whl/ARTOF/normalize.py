import numpy as np

def norm_sweep(binned_data: np.ndarray, bin_edges: list, sweep_start: float, step_size: float, sweep_steps: int, lens_k: float):
    """
    Normalize sweep data to lens k value.

    Args:
        bin_edges: Bin edges for sweep data.
        sweep_start: Start value of sweep.
        step_size: Step size of sweep.
        sweep_steps: Number of steps in sweep.
        lens_k: Lens k value.

    Returns:
        Normalized sweep data.
    """
    # calculate bin centers
    bin_centers = np.array([(bin_edges[i] + bin_edges[i+1]) / 2 for i in range(len(bin_edges)-1)])
    center_hits = np.zeros(len(bin_centers))
    # count how often each bin center is hit during
    for i in range(sweep_steps):
        e = sweep_start + i * step_size
        step_min = e*(1-lens_k/2)
        step_max = e*(1+lens_k/2)
        hits = np.where(np.logical_and(bin_centers >= step_min, bin_centers <= step_max))    
        for j in hits[0]:
            center_hits[j] += 1
    # fit to linear function
    fit_pars = np.polyfit(bin_centers, center_hits, 1)
    norm_values = np.polyval(fit_pars, bin_centers)
    # normalize data
    return binned_data / norm_values[:, np.newaxis, np.newaxis]