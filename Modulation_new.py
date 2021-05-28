import numpy as np
from numpy import linalg as la


def omega_axis(omega_prev_axis, omega_tau, time_delta):
    th = 1 / omega_tau
    sig = np.sqrt(2 * th / 3)

    return omega_prev_axis - th * omega_prev_axis * time_delta + sig * np.sqrt(time_delta) * np.random.normal()


def omega_new(omega_prev, omega_tau, time_delta):
    return np.array([omega_axis(omega_prev[i], omega_tau, time_delta) for i in range(3)])


def omega_full(omega_random, external_field):
    return [omega_random[i] + external_field[i] for i in range(3)]


def spin_rotation(spin, omega, time_delta):
    omega_value = la.norm(omega)
    omega_unit = [i / omega_value for i in omega]
    x, y, z = omega_unit[0], omega_unit[1], omega_unit[2]
    a = time_delta * omega_value
    cos, sin = np.cos(a), np.sin(a)

    matrix_of_rotation = np.array([
        [cos + (1 - cos) * pow(x, 2), (1 - cos) * x * y - sin * z, (1 - cos) * x * z + sin * y],
        [(1 - cos) * y * x + sin * z, cos + (1 - cos) * pow(y, 2), (1 - cos) * y * z - sin * x],
        [(1 - cos) * x * z - sin * y, (1 - cos) * z * y + sin * x, cos + (1 - cos) * pow(z, 2)]
    ])

    return np.dot(spin, matrix_of_rotation)


def spin_mixed_modulation(spin, omega, time_delta):
    # counting next coordinate of spin

    omega_delta = [x * time_delta / 2 for x in omega]
    matrix_of_coefficients = np.array([[1, omega_delta[2], -omega_delta[1]],
                                       [-omega_delta[2], 1, omega_delta[0]],
                                       [omega_delta[1], -omega_delta[0], 1]])

    negate_off_diagonal = np.identity(3) * 2 - np.ones(3)
    matrix_of_results = np.dot(matrix_of_coefficients * negate_off_diagonal, spin)

    spin = la.solve(matrix_of_coefficients, matrix_of_results)
    return spin


def average_spin_z(spin_list, n_electrons):
    sum_spin_z = 0
    for spin in spin_list:
        sum_spin_z += spin[2]
    return sum_spin_z / n_electrons


def relaxation(omega_tau, external_field, time_delta, n_electrons, flag=0):
    spin_initial = [0, 0, 1]
    omega_initial = [0, 0, 0]
    spin_length = la.norm(spin_initial)
    spin_list = [spin_initial for _ in range(n_electrons)]
    omega_list = [omega_initial for _ in range(n_electrons)]

    relaxation_cosine = np.cos(1)

    time = 0.0
    while average_spin_z(spin_list, n_electrons) >= relaxation_cosine:
        for i in range(n_electrons):
            spin = spin_list[i]

            omega = omega_full(omega_new(omega_list[i], omega_tau, time_delta), external_field)

            if flag == 0:
                spin = spin_rotation(spin, omega, time_delta)
                spin_list[i] = spin

                if abs((la.norm(spin) - spin_length)) > 0.00001 * spin_length:
                    print('Position deviation is too big!')
                    return None
                omega_list[i] = omega
            else:
                spin_list[i] = spin_mixed_modulation(spin, omega, time_delta)
                if abs((la.norm(spin) - spin_length)) > 0.00001 * spin_length:
                    print('Position deviation is too big!')
                    return None
                omega_list[i] = omega
        time += time_delta
        print(average_spin_z(spin_list, n_electrons))
        # print(time, " ", average_spin_z(condition_list))

    return time


print(relaxation(0.3, [0, 0, 0], 0.001, 1000))
print(relaxation(0.3, [0, 0, 0], 0.001, 1000, 1))
