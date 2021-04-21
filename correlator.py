import matplotlib.pyplot as plt
import numpy as np
from Modulation import random_unit_vector
plt.figure(figsize=(19, 9.5))


def correlator(_omega_list, step):
    omega_list_x = [omega[0] for omega in _omega_list]
    omega_list_y = [omega[1] for omega in _omega_list]
    omega_list_z = [omega[2] for omega in _omega_list]

    lst_x = []
    lst_y = []
    lst_z = []
    for _i in range(len(_omega_list)-step):
        lst_x.append(omega_list_x[_i] * omega_list_x[_i+step])
        lst_y.append(omega_list_y[_i] * omega_list_y[_i+step])
        lst_z.append(omega_list_z[_i] * omega_list_z[_i+step])

    cor_x = sum(lst_x) / len(lst_x)
    cor_y = sum(lst_y) / len(lst_y)
    cor_z = sum(lst_z) / len(lst_z)

    return cor_x, cor_y, cor_z


k = 0
omega = random_unit_vector()
omega_list = []
number = 100000
for i in range(number):
    if k == 1000:
        k = 0
        omega = random_unit_vector()
    k += 1
    omega_list.append(omega)

x_list = []
y_list = []
z_list = []
a_list = []
for i in range(1, 999):
    a = i
    x, y, z = correlator(omega_list, i)
    a_list.append(a)
    x_list.append(x)
    y_list.append(y)
    z_list.append(z)

plt.figure(figsize=(19, 9.5))
plt.plot(a_list, x_list, 'r')
# plt.plot(a_list, y_list, 'g')
# plt.plot(a_list, z_list, 'b')

# plt.xlim(0, 17)
# plt.ylim(0, 80)

# plt.savefig(r'image_files\external_fields.png')
plt.show()
