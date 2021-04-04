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
    omega_random_initial = [0, 0, 1]
    omega = [x + y for x, y in zip(omega_random_initial, omega_outside)]  # vector sum

    frame_number = 0

    while cosine_similarity(spin_position, spin_position_initial) > cosine_of_angle_of_relaxation:

        # every time_delta_accuracy round of cycle omega changes, so it changes every omega*tau
        if frame_number % (time_delta_accuracy + 1) == time_delta_accuracy:
            omega = omega_full(omega_outside)

        frame_number += 1

        spin_position = spin_position_mixed_modulation(spin_position, omega, time_delta)
        spin_position_list.append(spin_position)

        if abs((la.norm(spin_position) - spin_length)) > 0.0001 * spin_length:
            print('Position deviation is too big!')
            return None

    time_of_relaxation = time_delta * (frame_number - 1)

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
'''
class SpinRelaxation:

    # condition of relaxation
    angle_of_relaxation = 1
    cosine_of_angle_of_relaxation = np.cos(angle_of_relaxation)

    # step of time in modulation
    time_delta_accuracy = 100

    # initialization of spin
    spin_length = 1
    spin_position_initial = [0, spin_length, 0]
    spin_position = spin_position_initial
    spin_position_list = [spin_position]

    omega_outside = [0, 0, 0]

    def __init__(self, omega_tau, omega_outside=(0, 0, 0), angle_of_relaxation=1, time_delta_accuracy=100):
        self.omega_tau = omega_tau

        self.time_delta_accuracy = time_delta_accuracy
        
        self.omega_outside = omega_outside
        self.time_delta = omega_tau / self.time_delta_accuracy
        
        self.angle_of_relaxation = angle_of_relaxation

    def spin_relaxation_modulation(self):
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
        omega_random_initial = [0, 0, 1]
        omega = [x + y for x, y in zip(omega_random_initial, omega_outside)]  # vector sum

        frame_number = 0

        while cosine_similarity(spin_position, spin_position_initial) > cosine_of_angle_of_relaxation:

            # every time_delta_accuracy round of cycle omega changes, so it changes every omega*tau
            if frame_number % (time_delta_accuracy + 1) == time_delta_accuracy:
                omega = omega_full(omega_outside)

            frame_number += 1

            spin_position = spin_position_mixed_modulation(spin_position, omega, time_delta)
            spin_position_list.append(spin_position)

            if abs((la.norm(spin_position) - spin_length)) > 0.0001 * spin_length:
                print('Position deviation is too big!')
                return None

        time_of_relaxation = time_delta * (frame_number - 1)

        return time_of_relaxation
'''
