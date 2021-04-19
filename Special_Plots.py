import matplotlib.pyplot as plt
import numpy as np
from File_Operations import FileOperations
plt.figure(figsize=(19, 9.5))


def relaxation_plot():
    file = FileOperations('Time_5000_117_from0,04to1,2.txt')
    _, x, y = file.reading()
    x1, x2, y1, y2 = [], [], [], []

    for i in range(len(x)):
        if x[i] < 1:
            x1.append(x[i])
            y1.append(y[i])
        if x[i] > 1:
            x2.append(x[i])
            y2.append(y[i])

    plt.plot(x1, y1, 'r', linewidth=2)
    plt.plot(x2, y2, 'r', linewidth=2)
    plt.plot(x, y, 'ro', markersize=8)
    plt.xlim(0, 1.23)
    plt.ylim(0, 42)

    plt.title('Spin relaxation time dependence on the external magnetic field', fontsize=26)
    plt.xlabel('Time between collisions ( 1/Ω )', fontsize=20)
    plt.ylabel('Spin relaxation time ( 1/Ω )', fontsize=20)

    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.savefig(r'image_files\relaxation_plot.png')
    plt.show()


def relaxation_log_log_plot():
    file = FileOperations('Time_5000_117_from0,04to1,2.txt')
    _, x, y = file.reading()
    x = [np.log(i) for i in x]
    y = [np.log(i) for i in y]
    for i in range(len(x)):
        print(x[i], y[i])

    x1, x2, y1, y2 = [], [], [], []

    for i in range(len(x)):
        if x[i] < 0:
            x1.append(x[i])
            y1.append(y[i])
        if x[i] > 0:
            x2.append(x[i])
            y2.append(y[i])

    plt.plot(x1, y1, 'r', linewidth=2)
    plt.plot(x2, y2, 'r', linewidth=2)
    plt.plot(x, y, 'ro', markersize=8)
    plt.xlim(-3.3, 0.3)
    plt.ylim(0, 4)

    plt.title('Spin relaxation time dependence on the external magnetic field', fontsize=26)
    plt.xlabel('Logarithm of time between collisions', fontsize=20)
    plt.ylabel('Logarithm of spin relaxation time', fontsize=20)

    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.savefig(r'image_files\relaxation_log_log_plot.png')
    plt.show()


def external_field_plot():
    file2 = FileOperations('Time_5000_117_from0,04to1,2.txt')

    file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
    _, x1, y1 = file.reading()
    plt.plot(x1, y1, 'y')

    file = FileOperations('Field_0,2_2000_16_from1,0to16,0.txt')
    _, x2, y2 = file.reading()
    plt.plot(x2, y2, 'r')

    file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
    _, x3, y3 = file.reading()
    plt.plot(x3, y3, 'b')

    file = FileOperations('Field_0,4_2000_16_from1,0to16,0.txt')
    _, x4, y4 = file.reading()
    plt.plot(x4, y4, 'g')

    plt.xlim(0, 17)
    plt.ylim(0, 80)

    plt.title('Spin relaxation time dependence on the external magnetic field', fontsize=26)
    plt.xlabel('Time between collisions ( 1/ω )', fontsize=20)
    plt.ylabel('Spin relaxation time ( 1/ω )', fontsize=20)

    plt.legend(['0.1', '0.2', '0.3', '0.4'], title='ωτ =', fontsize=20, title_fontsize=20, loc='upper left')

    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.plot(x1, y1, 'yo')
    plt.plot(x2, y2, 'ro')
    plt.plot(x3, y3, 'bo')
    plt.plot(x4, y4, 'go')

    plt.savefig(r'image_files\external_fields_plot.png')
    plt.show()


def external_field_factor_plot():
    file2 = FileOperations('Time_5000_117_from0,04to1,2.txt')

    file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
    _, x1, y1 = file.reading()
    y_0 = file2.searching(0.1)
    x1 = [i**2 for i in x1]
    y1 = [(i/y_0)**2 for i in y1]
    plt.plot(x1, y1, 'y')

    file = FileOperations('Field_0,2_2000_16_from1,0to16,0.txt')
    _, x2, y2 = file.reading()
    y_0 = file2.searching(0.2)
    x2 = [i**2 for i in x2]
    y2 = [(i/y_0)**2 for i in y2]
    plt.plot(x2, y2, 'r')

    file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
    _, x3, y3 = file.reading()
    y_0 = file2.searching(0.3)
    x3 = [i**2 for i in x3]
    y3 = [(i/y_0)**2 for i in y3]
    plt.plot(x3, y3, 'b')

    file = FileOperations('Field_0,4_2000_16_from1,0to16,0.txt')
    _, x4, y4 = file.reading()
    y_0 = file2.searching(0.4)
    x4 = [i**2 for i in x4]
    y4 = [(i/y_0)**2 for i in y4]
    plt.plot(x4, y4, 'g')

    plt.xlim(0, 270)
    plt.ylim(0, 150)

    plt.title('Spin relaxation time dependence on the external magnetic field', fontsize=26)
    plt.xlabel('(Ωτ)^2', fontsize=20)
    plt.ylabel('Squared ratio of relaxation times', fontsize=20)

    plt.legend(['0.1', '0.2', '0.3', '0.4'], title='ωτ =', fontsize=20, title_fontsize=20, loc='upper left')

    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.plot(x1, y1, 'yo')
    plt.plot(x2, y2, 'ro')
    plt.plot(x3, y3, 'bo')
    plt.plot(x4, y4, 'go')

    plt.savefig(r'image_files\external_field_factor_plot.png')
    plt.show()


def external_field_log_plot():
    file2 = FileOperations('Time_5000_117_from0,04to1,2.txt')

    file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
    _, x1, y1 = file.reading()
    y_0 = file2.searching(0.1)
    x1 = [i ** 2 for i in x1]
    y1 = [np.log(i/y_0) for i in y1]
    plt.plot(x1, y1, 'y')

    file = FileOperations('Field_0,2_2000_16_from1,0to16,0.txt')
    _, x2, y2 = file.reading()
    y_0 = file2.searching(0.2)
    x2 = [i**2 for i in x2]
    y2 = [np.log(i/y_0) for i in y2]
    plt.plot(x2, y2, 'r')

    file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
    _, x3, y3 = file.reading()
    y_0 = file2.searching(0.3)
    x3 = [i**2 for i in x3]
    y3 = [np.log(i/y_0) for i in y3]
    plt.plot(x3, y3, 'b')

    file = FileOperations('Field_0,4_2000_16_from1,0to16,0.txt')
    _, x4, y4 = file.reading()
    y_0 = file2.searching(0.4)
    x4 = [i**2 for i in x4]
    y4 = [np.log(i/y_0) for i in y4]
    plt.plot(x4, y4, 'g')

    plt.xlim(0, 260)
    plt.ylim(0, 7)

    plt.title('Spin relaxation time dependence on the external magnetic field', fontsize=26)
    plt.xlabel('(Ωτ)^2', fontsize=20)
    plt.ylabel('Logarithm of ratio of relaxation times', fontsize=20)

    plt.legend(['0.1', '0.2', '0.3', '0.4'], title='ωτ =', fontsize=20, title_fontsize=20, loc='upper left')

    plt.tick_params(axis='both', which='major', labelsize=18)

    plt.plot(x1, y1, 'yo')
    plt.plot(x2, y2, 'ro')
    plt.plot(x3, y3, 'bo')
    plt.plot(x4, y4, 'go')

    plt.savefig(r'image_files\external_field_log_plot.png')
    plt.show()

'''
file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x1, y1 = file.reading()
file = FileOperations('Field_spec50_0,3_2000_16_from1,0to16,0.txt')
_, x2, y2 = file.reading()
plt.plot(x1, y1, 'ro')
x2 = [i for i in x2]
plt.plot(x2, y2, 'bo')
'''
'''
file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x1, y1 = file.reading()
file = FileOperations('Field_spec200_0,3_2000_16_from1,0to16,0.txt')
_, x2, y2 = file.reading()
file = FileOperations('Field_spec50_0,3_2000_16_from1,0to16,0.txt')
_, x3, y3 = file.reading()
x = [np.log(i) for i in x1]
y1 = [np.log(i) for i in y1]
y2 = [np.log(i) for i in y2]
y3 = [np.log(i) for i in y3]

plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'bo')
plt.plot(x3, y3, 'go')


plt.show()
'''


file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x1, y1 = file.reading()
file = FileOperations('2_Field_0,3_2000_17_from0,0to16,0.txt')
_, x2, y2 = file.reading()

plt.plot(x1, y1, 'ro')
plt.plot(x2, y2, 'bo')

plt.show()

