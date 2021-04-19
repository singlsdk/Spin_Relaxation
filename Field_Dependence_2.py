import numpy as np
from Modulation import spin_average_relaxation_time_2
import File_Operations as fo

# parameters; creates outside omega value list with constant step
omega_tau = 0.3
outside_omega_value_min = 13
outside_omega_value_max = 16
n_points = 4
n_modulations = 2000

outside_omega_value_list = np.linspace(outside_omega_value_min, outside_omega_value_max, n_points)
average_relaxation_time_list = [
    spin_average_relaxation_time_2(omega_tau, n_modulations, [0, 0, outside_omega_value])
    for outside_omega_value in outside_omega_value_list
    ]

# saving in temporary file
inf = '2_Field ' + str(omega_tau) + ' ' + str(n_modulations) + ' ' + str(n_points)
file = fo.FileOperations('Field_Plot.txt')
file.writing(inf, x=outside_omega_value_list, y=average_relaxation_time_list)

# saving in real file
file_name = fo.file_name_creating(inf, outside_omega_value_list)
file = fo.FileOperations(file_name)
file.writing(inf, x=outside_omega_value_list, y=average_relaxation_time_list)
