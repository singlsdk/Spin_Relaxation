import numpy as np
from numpy import linalg as la


def random_unit_vector():

    # Code from: https://stackoverflow.com/questions/5408276/
    # sampling-uniformly-distributed-random-points-inside-a-spherical-volume

    phi = np.random.uniform(0, np.pi * 2)
    cos_theta = np.random.uniform(-1, 1)

    theta = np.arccos(cos_theta)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = cos_theta

    # x^2 + y^2 + z^2

    return x, y, z


def omega_full(omega_outside):
    omega = [x + y for x, y in zip(random_unit_vector(), omega_outside)]  # vector sum
    return omega


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (la.norm(vec1) * la.norm(vec2))


def spin_position_mixed_modulation(spin_position, omega, time_delta):
    # counting next coordinate of spin

    omega_delta = [x * time_delta / 2 for x in omega]
    matrix_of_coefficients = np.array([[1, omega_delta[2], -omega_delta[1]],
                                       [-omega_delta[2], 1, omega_delta[0]],
                                       [omega_delta[1], -omega_delta[0], 1]])

    negate_off_diagonal = np.identity(3) * 2 - np.ones(3)
    matrix_of_results = np.dot(matrix_of_coefficients * negate_off_diagonal, spin_position)

    spin_position = la.solve(matrix_of_coefficients, matrix_of_results)
    return spin_position


def spin_position_rotation(spin_position, omega, time_between_collisions):
    omega_value = la.norm(omega)
    omega_unit = [i / omega_value for i in omega]
    x, y, z = omega_unit[0], omega_unit[1], omega_unit[2]
    a = time_between_collisions * omega_value
    cos, sin = np.cos(a), np.sin(a)

    matrix_of_rotation = [
        [cos + (1 - cos) * pow(x, 2), (1 - cos) * x * y - sin * z, (1 - cos) * x * z + sin * y],
        [(1 - cos) * y * x + sin * z, cos + (1 - cos) * pow(y, 2), (1 - cos) * y * z - sin * x],
        [(1 - cos) * x * z - sin * y, (1 - cos) * z * y + sin * x, cos + (1 - cos) * pow(z, 2)]
    ]

    return np.dot(spin_position, matrix_of_rotation)


def spin_relaxation_modulation(omega_tau, omega_outside=(0, 0, 0)):
    # condition of relaxation
    angle_of_relaxation = 1
    cosine_of_angle_of_relaxation = np.cos(angle_of_relaxation)

    # step of time in modulation
    time_delta_accuracy = 100
    time_delta = omega_tau / time_delta_accuracy

    # initialization of spin
    spin_length = 1
    spin_position_initial = [0, spin_length, 0]
    spin_position = spin_position_initial
    spin_position_list = [spin_position]

    # initial spin position is perpendicular to random omega at first moment
    # TODO: omega_random_initial = [0, 0, 1]
    omega_random_initial = random_unit_vector()
    omega = [x + y for x, y in zip(omega_random_initial, omega_outside)]  # vector sum
    omega_list = [omega]

    frame_number = 0

    while cosine_similarity(spin_position, spin_position_initial) > cosine_of_angle_of_relaxation:

        # every time_delta_accuracy round of cycle omega changes, so it changes every omega*tau
        if frame_number % (time_delta_accuracy + 1) == time_delta_accuracy:
            omega = omega_full(omega_outside)

        omega_list.append(omega)

        frame_number += 1

        spin_position = spin_position_mixed_modulation(spin_position, omega, time_delta)
        spin_position_list.append(spin_position)

        if abs((la.norm(spin_position) - spin_length)) > 0.00001 * spin_length:
            print('Position deviation is too big!')
            return None

    time_of_relaxation = time_delta * (frame_number - 1)

    return time_of_relaxation


def spin_relaxation_modulation_2(omega_tau, omega_outside=(0, 0, 0), angle_of_relaxation=1,
                                 omega_initial='random'):
    # condition of relaxation
    cosine_of_angle_of_relaxation = np.cos(angle_of_relaxation)

    # initialization of spin
    spin_length = 1
    spin_position_initial = [0, 0, spin_length]
    spin_position = spin_position_initial
    spin_position_list = [spin_position]

    # initial spin position is perpendicular to random omega at first moment
    if omega_initial == 'random':
        omega_random_initial = random_unit_vector()
    if omega_initial == 'perpendicular':
        omega_random_initial = [0, 1, 0]
    else:
        print('Wrong omega initial')
        return None

    omega = [x + y for x, y in zip(omega_random_initial, omega_outside)]  # vector sum
    omega_list = [omega]

    frame_number = 0

    while cosine_similarity(spin_position, spin_position_initial) > cosine_of_angle_of_relaxation:

        # every round of cycle omega changes, so it changes every omega*tau
        if frame_number != 0:
            omega = omega_full(omega_outside)
            omega_list.append(omega)

        frame_number += 1

        spin_position = spin_position_rotation(spin_position, omega, omega_tau)
        spin_position_list.append(spin_position)

        if abs((la.norm(spin_position) - spin_length)) > 0.00001 * spin_length:
            print('Position deviation is too big!')
            return None

    time_of_relaxation = omega_tau * (frame_number - 1)

    spin_position = spin_position_list[-2]

    # accuracy of calibration
    time_accuracy = 100
    # trying until first time out
    for i in range(time_accuracy):
        delta = omega_tau*i/time_accuracy
        spin_position_new = spin_position_rotation(spin_position, omega, delta)
        if cosine_similarity(spin_position_new, spin_position_initial) <= cosine_of_angle_of_relaxation:
            time_of_relaxation += delta
            break

    return time_of_relaxation


def spin_average_relaxation_time(omega_tau, n_modulations, omega_outside=(0, 0, 0)):
    time_list = []
    for i in range(n_modulations):
        if i % 10 == 0:
            print(i)

        time = spin_relaxation_modulation(omega_tau, omega_outside)
        time_list.append(time)

    average_time = sum(time_list) / n_modulations

    print(omega_tau)
    print(omega_outside)
    print(average_time)

    return average_time


def spin_average_relaxation_time_2(omega_tau, n_modulations, omega_outside=(0, 0, 0),
                                   angle_of_relaxation=1, omega_initial='random'):
    time_list = []
    for i in range(n_modulations):
        if i % 1000 == 0:
            print(i)

        time = spin_relaxation_modulation_2(omega_tau, omega_outside, angle_of_relaxation, omega_initial)
        time_list.append(time)

    average_time = sum(time_list) / n_modulations

    print(omega_tau)
    print(omega_outside)
    print(average_time)

    return average_time


def spin_precession_modulation(omega_tau, omega_outside=(0, 0, 0), frames_number=1000):
    # TODO: make help functions for spin_precession_modulation and spin_relaxation_modulation;
    #  problem is too big number of arguments

    # step of time in modulation
    time_delta_accuracy = 100
    time_delta = omega_tau / time_delta_accuracy

    # initialization of spin
    spin_length = 1
    spin_position_initial = [0, - spin_length, 0]
    spin_position = spin_position_initial
    spin_position_list = [spin_position]

    # initial spin position is perpendicular to random omega at first moment
    omega_random_initial = [0, 0, 1]
    omega = [x + y for x, y in zip(omega_random_initial, omega_outside)]  # vector sum

    for frame_number in range(frames_number):

        # every time_delta_accuracy round of cycle omega changes, so it changes every omega*tau
        if frame_number % (time_delta_accuracy + 1) == time_delta_accuracy:
            omega = omega_full(omega_outside)

        spin_position = spin_position_mixed_modulation(spin_position, omega, time_delta)
        spin_position_list.append(spin_position)

        if abs((la.norm(spin_position) - spin_length)) > 0.0001 * spin_length:
            print('Position deviation is too big!')
            return None

    return spin_position_list


# TODO: Make class (a bit later............)

def average_spin_z(modulation_list):
    spin_z_sum = 0
    for spin_position in modulation_list:
        spin_z_sum += spin_position[0][2]
    return spin_z_sum / len(modulation_list)


class SpinRelaxation:

    def __init__(self, omega_tau, omega_outside=(0, 0, 0), angle_of_relaxation=1, omega_initial='random',
                 time_accuracy=100):

        self.omega_outside = omega_outside
        self.omega_tau = omega_tau
        self.omega_initial = omega_initial
        self.spin_length = 1
        # accuracy of calibration
        self.time_accuracy = time_accuracy

        # condition of relaxation
        self.cosine_of_angle_of_relaxation = np.cos(angle_of_relaxation)

        # initialization of spin
        self.spin_position_initial = [0, 0, self.spin_length]

        # initial spin position is perpendicular to random omega at first moment
        if self.omega_initial == 'random':
            self.omega_random_initial = random_unit_vector()
        elif self.omega_initial == 'perpendicular':
            self.omega_random_initial = [0, 1, 0]
        else:
            print('Wrong omega initial')
            self.omega_random_initial = ['Wrong omega initial']

    def spin_relaxation_modulation_c(self):
        # initialization of spin
        if self.omega_initial == 'random':
            omega_random_initial = random_unit_vector()
        else:
            omega_random_initial = self.omega_random_initial

        spin_position = self.spin_position_initial
        spin_position_list = [spin_position]

        omega = [x + y for x, y in zip(omega_random_initial, self.omega_outside)]  # vector sum
        omega_list = [omega]

        frame_number = 0

        while cosine_similarity(spin_position, self.spin_position_initial) >= self.cosine_of_angle_of_relaxation:

            # every round of cycle omega changes, so it changes every omega*tau
            if frame_number != 0:
                omega = omega_full(self.omega_outside)
                omega_list.append(omega)

            frame_number += 1

            spin_position = spin_position_rotation(spin_position, omega, self.omega_tau)
            spin_position_list.append(spin_position)

            if abs((la.norm(spin_position) - self.spin_length)) > 0.00001 * self.spin_length:
                print('Position deviation is too big!')
                return None

        time_of_relaxation = self.omega_tau * (frame_number - 1)

        spin_position = spin_position_list[-2]

        # trying until first time out
        for i in range(self.time_accuracy):
            delta = self.omega_tau * i / self.time_accuracy
            spin_position_new = spin_position_rotation(spin_position, omega, delta)
            if cosine_similarity(spin_position_new, self.spin_position_initial) <= self.cosine_of_angle_of_relaxation:
                time_of_relaxation += delta
                break

        return time_of_relaxation

    def spin_relaxation_modulation_ensemble(self, n_modulations):
        modulation_list = []
        for _ in range(n_modulations):
            if self.omega_initial == 'random':
                omega_random_initial = random_unit_vector()
            else:
                omega_random_initial = self.omega_random_initial
            omega = [x + y for x, y in zip(omega_random_initial, self.omega_outside)]  # vector sum
            modulation_list.append([self.spin_position_initial, omega])

        frame_number = 0

        spin_z = average_spin_z(modulation_list)

        while spin_z >= self.cosine_of_angle_of_relaxation:
            # print(frame_number)
            for i in range(len(modulation_list)):
                m = modulation_list[i]

                # every round of cycle omega changes, so it changes every omega*tau
                omega = m[1]
                if frame_number != 0:
                    omega = omega_full(self.omega_outside)

                spin_position = spin_position_rotation(m[0], omega, self.omega_tau)
                modulation_list[i] = [spin_position, omega]

            frame_number += 1
            spin_z = average_spin_z(modulation_list)

        time_of_relaxation = self.omega_tau * (frame_number - 1)
        print(time_of_relaxation)

        '''
        spin_position = spin_position_list[-2]

        # trying until first time out
        for i in range(self.time_accuracy):
            delta = self.omega_tau * i / self.time_accuracy
            spin_position_new = spin_position_rotation(spin_position, omega, delta)
            if cosine_similarity(spin_position_new, self.spin_position_initial) <= self.cosine_of_angle_of_relaxation:
                time_of_relaxation += delta
                break
        '''
        return time_of_relaxation

    def spin_average_relaxation_time_c(self, n_modulations):
        time_list = []
        for i in range(n_modulations):
            if i % 1000 == 0:
                print(i)

            time_of_relaxation = self.spin_relaxation_modulation_c()
            time_list.append(time_of_relaxation)

        average_time = sum(time_list) / n_modulations

        print(self.omega_tau)
        print(self.omega_outside)
        print(average_time)

        return average_time
