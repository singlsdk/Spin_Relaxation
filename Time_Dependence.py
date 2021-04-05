import numpy as np
from Modulation import spin_average_relaxation_time
import File_Operations as fo

# parameters; creates omega*tau list with constant step
omega_tau_min = 0.1
omega_tau_max = 1.2
n_points = 12
n_modulations = 50

omega_tau_list = np.linspace(omega_tau_min, omega_tau_max, n_points)
average_relaxation_time_list = [
    spin_average_relaxation_time(omega_tau, n_modulations) for omega_tau in omega_tau_list
    ]

# saving in temporary file
inf = 'Time ' + str(n_modulations) + ' ' + str(n_points)
file = fo.FileOperations('Time_Plot.txt')
file.writing(inf, x=omega_tau_list, y=average_relaxation_time_list)

# saving in real file
file_name = fo.file_name_creating(inf, omega_tau_list)
file = fo.FileOperations(file_name)
file.writing(inf, x=omega_tau_list, y=average_relaxation_time_list)


# TODO: understand map method and maybe use it (I don't think that this code looks prettier or faster)
'''
def wt_avgRT(n):
    omega_tau = omega_tau_min + omega_tau_span * n / divisor
    avg_relaxation_time = spin_average_relaxation_time(omega_tau, n_modulations)
    return omega_tau, avg_relaxation_time


wt, avgRT = zip(*map(wt_avgRT, range(n_points)))

str_spaced = lambda xs: " ".join(map(str, xs))

with open('Spin_Relaxation_Time_Plot.txt', 'w') as file:
    file.write(str_spaced(wt) + '\n' + str_spaced(avgRT))
'''
