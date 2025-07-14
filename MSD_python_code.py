# This script processes and visualizes Mean Squared Displacement (MSD) data for a chromatin simulation.
# It calculates the MSD in both longitudinal and transverse directions, fits power laws to the data, 
# and detects saturation points based on variance of slope in log-log space.
# The resulting MSD curves and fitted exponents are saved in a publication-quality plot.
# Intended for use in analyzing output like 'msdcom_middle.txt' generated from simulation trajectories.
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ---- Parameters ----
filename = "msdcom_middle.txt"
threshold_variance_increase = 1
# Threshold for detecting saturation point via variance in local slope
window_size = 100
min_data_points = 10
xmin_time = 100  # Start plotting and fitting from this time (after t_start shift)

# ---- Load and normalize data ----
data = np.loadtxt(filename)
raw_time = data[:, 0]
t_start = np.min(raw_time)  # auto-detect start time
time = (raw_time - t_start) / 100  # shifted and normalized

msd_left = data[:, 1]
msd_right = data[:, 2]
msd_middle = data[:, 3]
msd_avg = 0.5 * (msd_left + msd_right)

# ---- Select data from xmin_time onward ----
xmin_index = np.argmax(time >= xmin_time)
T = time[xmin_index:]
log_T = np.log10(T)
log_L = np.log10(msd_middle[xmin_index:])
log_R = np.log10(msd_avg[xmin_index:])

# ---- Calculate slopes and variance ----
def moving_variance(x, window):
    return np.convolve(x**2, np.ones(window)/window, mode='valid') - \
           np.convolve(x, np.ones(window)/window, mode='valid')**2

slopes_L = np.diff(log_L) / np.diff(log_T)
slopes_R = np.diff(log_R) / np.diff(log_T)
var_L = moving_variance(slopes_L, window_size)
var_R = moving_variance(slopes_R, window_size)

sat_idx_L = np.argmax(var_L > threshold_variance_increase) + window_size
sat_idx_R = np.argmax(var_R > threshold_variance_increase) + window_size

if sat_idx_L < min_data_points or sat_idx_L >= len(T):
    sat_idx_L = len(T)
if sat_idx_R < min_data_points or sat_idx_R >= len(T):
    sat_idx_R = len(T)

# ---- Linear fits ----
T_fit_L = log_T[:sat_idx_L]
MSD_fit_L = log_L[:sat_idx_L]
slope_L, intercept_L, _, _, std_err_L = linregress(T_fit_L, MSD_fit_L)

T_fit_R = log_T[:sat_idx_R]
MSD_fit_R = log_R[:sat_idx_R]
slope_R, intercept_R, _, _, std_err_R = linregress(T_fit_R, MSD_fit_R)

# ---- Plot ----
plt.figure(figsize=(5, 5))
plt.rcParams.update({'font.size': 12})
plt.loglog(time, msd_middle, 'o', markersize=3, color='green', label='Longitudinal MSD')
plt.loglog(time, msd_avg, 'o', markersize=3, color='purple', label='Transverse MSD')

# Fit curves
time_fit = np.logspace(np.log10(time[xmin_index]), np.log10(T[sat_idx_L - 1]), 100)
fit_curve_L = 10**intercept_L * time_fit**slope_L
fit_curve_R = 10**intercept_R * time_fit**slope_R

plt.plot(time_fit, fit_curve_L, '-', linewidth=3, color='red',
         label=fr'$\alpha_\ell={slope_L:.2f}$')
plt.plot(time_fit, fit_curve_R, '-', linewidth=3, color='black',
         label=fr'$\alpha_r={slope_R:.2f}$')

plt.xlabel(r"Time ($\tau$)")
plt.ylabel(r"MSD ($\sigma^2$)")
#plt.title(f"Middle region")
plt.ylim(5, 200)
plt.yticks([10, 100])
plt.xlim(200, 100000)
plt.xticks([200, 1000, 10000, 100000])
plt.legend(loc="lower right")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("middle_MSDcom_vs_time.png", dpi=300)
plt.show()
