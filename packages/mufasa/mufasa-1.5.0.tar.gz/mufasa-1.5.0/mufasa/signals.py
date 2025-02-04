"""
The `mufasa.signals` module provides robust tools for preprocessing spectral data, including RMS estimation,
signal masking, spatial trimming, and moment calculations.
"""

__author__ = "Mike Chen"

import gc

#=======================================================================================================================

import numpy as np
from spectral_cube.masks import LazyComparisonMask
from skimage.morphology import binary_dilation, remove_small_objects, binary_erosion, disk, binary_opening, ball
import astropy.units as u

#=======================================================================================================================
# Import in-house functions
from .utils.mufasa_log import get_logger
logger = get_logger(__name__)
#=======================================================================================================================


def get_snr(cube, rms=None, **kwargs):
    """
    Calculate the peak signal-to-noise ratio of the cube.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    rms : float or None, optional
        Root mean square of the map. If None, calculate using `get_rms_robust()`.
    **kwargs
        Additional arguments for RMS calculation.

    Returns
    -------
    Quantity
        Peak signal-to-noise ratio.
    """
    if rms is None:
        rms = get_rms_robust(cube, **kwargs)

    return cube.max(axis=0) / rms #, how='ray'


def get_rms_robust(cube, sigma_cut=2.5, expand=20, trim=None, method='robust', return_sigmask=False, **kwargs):
    """
    Make a robust RMS estimate.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    sigma_cut : float, optional
        Signal-to-noise ratio to mask out regions containing signal.
    expand : int, optional
        Number of spectral channels to expand the signal mask.
    trim : int or None, optional
        Number of pixels to trim from the edges of the cube.
    method : {'robust', 'signal_mask'}, optional
        Method to calculate RMS.
    return_sigmask : bool, optional
        Whether to return the 3D signal mask along with the RMS.
    **kwargs
        Additional arguments.

    Returns
    -------
    Quantity or tuple of Quantity
        RMS value, and optionally the signal mask.
    """
    if trim is not None:
        cube = trim_cube_edge(cube, trim)

    if method == 'robust':
        rms = cube.mad_std(axis=0) #how='ray'
        # Refine RMS by masking signal regions
        rms, sig_mask = refine_rms(cube, rms, sigma_cut=sigma_cut, expand=expand)

    elif method == 'signal_mask':
        # Use signal mask method to calculate RMS
        sig_mask = get_signal_mask(cube, sigma_cut=sigma_cut, **kwargs)
        noise_cube = cube.with_mask(~sig_mask & cube.mask.include())
        rms = noise_cube.mad_std(axis=0) #how='ray'

    if return_sigmask:
        return rms, sig_mask
    else:
        return rms


def refine_rms(cube, rms, sigma_cut=3, expand=20):
    """
    Refine the RMS estimate by masking out signal regions.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    rms : Quantity
        Initial RMS estimate.
    sigma_cut : float, optional
        Signal-to-noise threshold to mask signals.
    expand : int, optional
        Number of spectral channels to expand the signal mask.

    Returns
    -------
    Quantity
        Refined RMS.
    ndarray
        Signal mask.
    """
    # Mask above the cut threshold
    sig_mask = (cube > sigma_cut * rms)
    sig_mask = binary_dilation(sig_mask.include(), np.ones(shape=(expand, 1, 1), dtype=bool))
    noise_cube = cube.with_mask(~sig_mask & cube.mask.include())
    rms = noise_cube.mad_std(axis=0) #how='ray'
    return rms, sig_mask


def get_signal_mask(cube, snr_cut=3, minsize=2, expand=20, clean=True, return_rms=False):
    """
    Provide a 3D mask indicating signal regions based on RMS and SNR threshold.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    snr_cut : float, optional
        Signal-to-noise threshold to define signals.
    minsize : int, optional
        Minimum size of connected components in spectral direction.
    expand : int, optional
        Number of spectral channels to expand signal regions.
    clean : bool, optional
        Remove spatially isolated pixels.
    return_rms : bool, optional
        Whether to return RMS along with the signal mask.

    Returns
    -------
    ndarray
        Signal mask.
    Quantity, optional
        RMS value if `return_rms` is True.
    """
    rms = cube.mad_std(axis=0) #how='ray'
    # Mask above the cut threshold
    sig_mask = (cube > snr_cut * rms)
    sig_mask = refine_signal_mask(sig_mask, minsize=minsize, expand=expand, clean=clean)

    if return_rms:
        return sig_mask, rms
    else:
        return sig_mask


def refine_signal_mask(sig_mask, minsize=2, expand=20, clean=True):
    """
    Refine a signal mask by removing noisy features and expanding the mask.

    Parameters
    ----------
    sig_mask : LazyComparisonMask or ndarray
        Initial signal mask.
    minsize : int, optional
        Minimum number of continuous spectral channels for signal mask.
    expand : int, optional
        Number of spectral channels to expand signal regions.
    clean : bool, optional
        Remove spatially isolated pixels.

    Returns
    -------
    ndarray
        Refined signal mask.
    """
    if isinstance(sig_mask, LazyComparisonMask):
        sig_mask = sig_mask.include()

    # Remove voxels that are likely just statistical noise
    sig_mask = binary_erosion(sig_mask, np.ones(shape=(minsize, 1, 1), dtype=bool))
    sig_mask = remove_small_objects(sig_mask, 1)
    # Expand the "signal" regions a bit
    struct = np.ones(shape=(expand, 1, 1), dtype=bool)
    sig_mask = binary_dilation(sig_mask, struct)
    sig_mask = binary_dilation(sig_mask, disk(3)[np.newaxis, :])

    if clean:
        # Remove isolated pixels
        sig_mask *= remove_small_objects(binary_erosion(np.any(sig_mask, axis=0)), 1)

    return sig_mask


def trim_cube_edge(cube, trim=3, min_size=1000):
    """
    Remove spatial edges from a cube.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    trim : int, optional
        Number of pixels to trim from edges.
    min_size : int, optional
        Minimum size of cube for trimming to be applied.

    Returns
    -------
    SpectralCube
        Trimmed cube.
    """
    mask = cube.mask.include()
    planemask = np.any(mask, axis=0)

    if np.sum(planemask) > min_size:
        # Trim edges using a 2D mask
        planemask = trim_edge(planemask, trim=trim)
        mask[:, ~planemask] = False
        return cube.with_mask(mask)
    else:
        return cube


def trim_edge(mask, trim=3):
    """
    Trim edges using a 2D mask.

    Parameters
    ----------
    mask : ndarray
        2D mask.
    trim : int, optional
        Number of pixels to trim.

    Returns
    -------
    ndarray
        Trimmed mask.
    """
    # Set all edge pixels to False
    mask[[0, -1], :] = False
    mask[:, [0, -1]] = False
    return binary_erosion(mask, disk(trim))


def v_estimate(cube, rms, snr_cut=3):
    """
    Estimate the velocity centroid based on peak emission.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    rms : Quantity
        Root mean square of the map.
    snr_cut : float, optional
        Signal-to-noise threshold for quality control.

    Returns
    -------
    Quantity
        Velocity centroid estimate.
    """
    sig_mask = cube > rms * snr_cut
    # Clean the mask to remove noisy features
    sig_mask = binary_erosion(sig_mask.include(), ball(2))
    return get_v_at_peak(cube.with_mask(sig_mask))


def get_v_at_peak(cube_masked):
    """
    Find the velocity corresponding to the peak emission.

    Parameters
    ----------
    cube_masked : SpectralCube
        SpectralCube object with mask.

    Returns
    -------
    ndarray
        Velocity at peak emission.
    """
    idx_max = cube_masked.argmax(axis=0)#, how='slice')
    v_est = cube_masked.spectral_axis[idx_max]
    # Set velocity to NaN where no valid data is present
    v_est[~np.any(cube_masked.get_mask_array(), axis=0)] = np.nan
    return v_est.value


def get_v_mask(cube_masked, v_center, rms=None, window_hwidth=5):
    """
    Return a mask centered on a reference velocity with a spectral window.

    Parameters
    ----------
    cube_masked : SpectralCube
        SpectralCube object with mask.
    v_center : Quantity
        Reference velocity at center of spectral window.
    rms : Quantity or None, optional
        Root mean square of the map.
    window_hwidth : float, optional
        Half-width of spectral window in km/s.

    Returns
    -------
    ndarray
        Velocity mask.
    """
    snr_cut = 3
    # Get window centered on v_center with a half-width of window_hwidth
    window_mask = (cube_masked.spectral_axis[:, np.newaxis, np.newaxis] < (v_center + window_hwidth) * u.km / u.s) & \
                  (cube_masked.spectral_axis[:, np.newaxis, np.newaxis] > (v_center - window_hwidth) * u.km / u.s)

    if rms is not None:
        # Remove voxels that are likely noise
        mask_new = binary_opening((cube_masked > rms * snr_cut).include())
        return mask_new & window_mask
    else:
        return cube_masked.get_mask_array() & window_mask


def get_moments(cube, window_hwidth=5, linewidth_sigma=True, trim=3, return_rms=False, central_win_hwidth=None,
                **kwargs):
    """
    Calculate moments of the signals in a cube.

    Parameters
    ----------
    cube : SpectralCube
        SpectralCube object.
    window_hwidth : float, optional
        Half-width of spectral window for moment calculation.
    linewidth_sigma : bool, optional
        Whether to calculate linewidth sigma instead of moment 2 (see spectral_cube documentation for further details).
    trim : int, optional
        Number of pixels to trim from edges of the cube.
    return_rms : bool, optional
        Whether to return RMS along with moments.
    central_win_hwidth : float, optional
        If provided, re-evulate velocity at peak using a window centered on the mode of the initial velocity estimate, with a
        half-wdith of central_win_hwidth. Note that window is the same for all pixels, but only applied as an intermediate step.
        This should only used if hyperfine lines far from the main hyperfines have a comprable brightness.

    **kwargs
        Additional arguments.

    Returns
    -------
    tuple of Quantity
        Tuple of moment maps (moment 0, moment 1, linewidth or moment 2, optionally RMS).
    """
    snr_cut = 3
    noise_mask_cut = 2.5

    # Trim cube edges
    if trim is not None:
        cube = trim_cube_edge(cube, trim=trim)
    rms = get_rms_robust(cube, sigma_cut=noise_mask_cut, **kwargs)
    v_peak = v_estimate(cube, rms, snr_cut=snr_cut)

    if central_win_hwidth is not None:
        # impose a strick window based on the esitmated mode velocity to re-evaulate v_peak
        v_mode = estimate_mode(v_peak, bins=25)
        signal_mask_tmp = get_v_mask(cube, v_center=v_mode, rms=rms, window_hwidth=central_win_hwidth)
        cube_signal_tmp = cube.with_mask(signal_mask_tmp)
        v_peak = v_estimate(cube_signal_tmp, rms, snr_cut=snr_cut)
        del signal_mask_tmp
        del cube_signal_tmp
        gc.collect()

    # Get velocity mask centered on v_peak with window_hwidth
    signal_mask = get_v_mask(cube, v_peak, rms=rms, window_hwidth=window_hwidth)
    # Expand the footprint a bit
    signal_mask = binary_dilation(signal_mask, disk(3)[np.newaxis, :])

    cube_signal = cube.with_mask(signal_mask)
    mom0 = cube_signal.moment0()
    mom1 = cube_signal.moment1()
    output = (mom0, mom1)

    if linewidth_sigma:
        output += (cube_signal.linewidth_sigma(),)
    else:
        output += (cube_signal.moment2(),)

    if return_rms:
        output += (rms,)

    return output


def estimate_mode(data, bins=25):
    """
    Estimate the mode of the data using a histogram.

    Parameters
    ----------
    data : ndarray
        The data for which to estimate the mode. Non-finite values will be ignored.
    bins : int, optional
        Number of bins to use for the histogram. Default is 25.

    Returns
    -------
    float
        The estimated mode of the data.
    """
    data=data[np.isfinite(data)]
    counts, bins = np.histogram(data, bins=bins)

    # Find the bin with the maximum frequency
    max_bin_index = np.argmax(counts)
    return (bins[max_bin_index] + bins[max_bin_index + 1]) / 2
