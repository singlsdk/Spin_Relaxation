import numpy as np
from Modulation import spin_average_relaxation_time
import File_Operations as FO

# parameters; creates outside omega value list with constant step
omega_tau = 0.1
outside_omega_value_min = 16
outside_omega_value_max = 16
n_points = 1
n_modulations = 2000

outside_omega_value_list = np.linspace(outside_omega_value_min, outside_omega_value_max, n_points)
average_relaxation_time_list = [
    spin_average_relaxation_time(omega_tau, n_modulations, [0, outside_omega_value, 0])
    for outside_omega_value in outside_omega_value_list
    ]

# saving in temporary file
file = FO.FileOperations('Field_Plot.txt')
file.writing(inf='Field ' + str(omega_tau) + ' ' + str(n_modulations),
             x=outside_omega_value_list, y=average_relaxation_time_list)

# saving in real file
inf = 'Field ' + str(omega_tau) + ' ' + str(n_modulations)
file_name = FO.file_name_creating(inf, outside_omega_value_list)
file = FO.FileOperations(file_name)
file.writing(inf, x=outside_omega_value_list, y=average_relaxation_time_list)
