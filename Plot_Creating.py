import matplotlib.pyplot as plt
import numpy as np
from File_Operations import FileOperations


def time_theor():
    _y_theor = []
    for _i in x:
        if _i <= 1:
            _y_theor.append(1/_i)
        else:
            _y_theor.append(1.0)
    return _y_theor


def field_theor():
    print(type(y_0), type(omega_tau))
    _y_theor = [y_0 * (1 + (_i * omega_tau) ** 2) for _i in x]
    return _y_theor


default_file_names = {
    'T': 'Time_Plot.txt',
    'F': 'Field_Plot.txt',
    'FF': 'Field_Plot.txt',
    'LL': 'Time_Plot.txt',
    'S': 'Field_Plot.txt'
}

print("Print plot type:", end=' ')
plot_type = input()

print("Default (print 0) or customizable (print 1) file_name:", end=' ')
input_type = input()

if input_type == '0':
    file_name = default_file_names[plot_type]

elif input_type == '1':
    print("Print file name:", end=' ')
    file_name = input()

else:
    # most useful file for few next plots; write anything instead 0 and 1 to call it
    file_name = 'Field_0,2_2000_16_from1,0to16,0.txt'

print("Print 1 for theoretical plot:", end=' ')
theor_existence = input()
if theor_existence == '1':
    theor_existence = '_theor_'
else:
    theor_existence = '_'


file = FileOperations(file_name)
inf, x, y = file.reading()

# creating plot
plt.figure(figsize=(19, 9.5))
default_label_size = 20
default_title_size = 26

y_0 = 0
y_theor = []

if plot_type == 'T':
    y_theor = time_theor()
    plt.title('Spin relaxation time dependence on time between collisions', fontsize=default_title_size)
    plt.xlabel('Time between collisions ( 1/Ω )', fontsize=default_label_size)
    plt.ylabel('Spin relaxation time ( 1/Ω )', fontsize=default_label_size)

elif plot_type == 'F':
    omega_tau = float(inf[1])
    file = FileOperations('Time_5000_117_from0,04to1,2.txt')
    y_0 = file.searching(omega_tau)
    y_theor = field_theor()
    plt.title('Spin relaxation time dependence on the external magnetic field , Ωτ = ' + str(omega_tau),
              fontsize=default_title_size)
    plt.xlabel('Time between collisions ( 1/Ω )', fontsize=default_label_size)
    plt.ylabel('Spin relaxation time ( 1/Ω )', fontsize=default_label_size)

elif plot_type == 'FF':
    omega_tau = float(inf[1])
    file = FileOperations('Time_5000_117_from0,04to1,2.txt')
    y_0 = file.searching(omega_tau)
    y_theor = field_theor()

    def fun_y(a): return (a[1] - y_0) / (a[0] ** 2)
    y = list(map(fun_y, zip(x, y)))
    y_theor = list(map(fun_y, zip(x, y_theor)))

    plt.title("Фактор магнитного поля при Omega*Tau = " + str(omega_tau))
    plt.xlabel("Отношение внешнего поля к случайному")
    plt.ylabel("Магнитный фактор релаксации ( 1/Omega^2 )")

elif plot_type == 'LL':

    y_theor = time_theor()

    for i in range(len(y)):
        if y[i] <= 0:
            y = 1

    def fun_y(j): return np.log(j - y_0)
    y = list(map(fun_y, y))
    y_theor = list(map(fun_y, y_theor))

    x = list(map(np.log, x))

    # plt.title("Логирифм среднего времени релаксации от логарифма времени между столкновениями")
    # plt.xlabel("Логарифм времени между столкновениями")
    # plt.ylabel("Логирифм среднего времени релаксации")

elif plot_type == 'S':
    # this code is unique for most runs, so it'd be ugly
    omega_tau = float(inf[1])
    file = FileOperations('Time_5000_117_from0,04to1,2.txt')
    y_0 = file.searching(omega_tau)
    y_theor = field_theor()

    x = [i**2 for i in x]
    y = [i / y_0 for i in y]

    for i in range(len(y)):
        if y[i] <= 0:
            x[i] = 1
            y[i] = 1
            y_theor[i] = 0

    def fun_y(j): return np.log(j)
    y = list(map(fun_y, y))
    y_theor = list(map(fun_y, y_theor))
    # plt.title("Логирифм среднего времени релаксации от логарифма времени между столкновениями")
    # plt.xlabel("Логарифм времени между столкновениями")
    # plt.ylabel("Логирифм среднего времени релаксации")

else:
    plt.title("Wrong Input")
    x, y = [0], [0]


print(y_0)
print(x)
print(y)

if theor_existence == '_theor_':
    plt.plot(x, y_theor, 'bo')
    print(y_theor)
else:
    y_theor = []

plt.tick_params(axis='both', which='major', labelsize=18)
plt.xlim(min(0, 1.05 * min(x)), 1.05 * max(x))
plt.ylim(min(0, 1.05 * min(y)), 1.05 * max(y + y_theor))

plt.plot(x, y, 'ro', markersize=7)

# for example: Field_from0,04to1,2_5000.txt --> FieldFactor_from0,04to1,2_5000.png
image_name = str(plot_type) + theor_existence + '_'.join((''.join(file_name.split('.')[:1]) + '.png').split('_')[1:])

plt.savefig('image_files' + '\\' + image_name)
plt.show()
