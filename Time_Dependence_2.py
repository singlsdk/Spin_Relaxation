import numpy as np
from Modulation import spin_average_relaxation_time_2
import File_Operations as fo

# parameters; creates omega*tau list with constant step
omega_tau_min = 0.1
omega_tau_max = 1.3
n_points = 13
n_modulations = 2000

omega_tau_list = np.linspace(omega_tau_min, omega_tau_max, n_points)
average_relaxation_time_list = [
    spin_average_relaxation_time_2(omega_tau, n_modulations) for omega_tau in omega_tau_list
    ]

# saving in temporary file
inf = '2_Time ' + str(n_modulations) + ' ' + str(n_points)
file = fo.FileOperations('Time_Plot.txt')
file.writing(inf, x=omega_tau_list, y=average_relaxation_time_list)

# saving in real file
file_name = fo.file_name_creating(inf, omega_tau_list)
file = fo.FileOperations(file_name)
file.writing(inf, x=omega_tau_list, y=average_relaxation_time_list)
