import matplotlib.pyplot as plt
import numpy as np
from File_Operations import FileOperations


default_file_names = {
    'T': 'Time_Plot.txt',
    'F': 'Field_Plot.txt',
    'FF': 'Field_Plot.txt',
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
    file_name = 'Field_from1,0to16,0.txt'

file = FileOperations(file_name)
inf, x, y = file.reading()

# creating plot
plt.figure(figsize=(19, 9.5))

y_0 = 0
y_theory = []

if plot_type == 'T':
    plt.title("Среднее время релаксации от времени между столкновениями")
    plt.xlabel("Время между столкновениями ( 1/(cек^2*Omega) )")
    plt.ylabel("Время релаксации ( 1/(cек^2*Omega) )")

elif plot_type == 'F':
    omega_tau = float(inf[1])
    file = FileOperations('Time_from0,04to1,2_5000.txt')
    y_0 = file.searching(omega_tau)
    y_theory = [y_0 * (1 + (i * omega_tau) ** 2) for i in x]
    plt.plot(x, y_theory, 'bo')
    plt.title("Среднее время релаксации от внешнего поля при Omega*Tau = " + str(omega_tau))
    plt.xlabel("Отношение внешнего поля к случайному")
    plt.ylabel("Время релаксации ( 1/(cек^2*Omega) )")

elif plot_type == 'FF':
    omega_tau = float(inf[1])
    file = FileOperations('Time_from0,04to1,2_5000.txt')
    y_0 = file.searching(omega_tau)
    y_theory = [y_0 * (1 + (i * omega_tau) ** 2) for i in x]

    fun_y = lambda a: (a[1] - y_0) / (a[0] ** 2)
    y = list(map(fun_y, zip(x, y)))
    y_theory = list(map(fun_y, zip(x, y_theory)))

    plt.plot(x, y_theory, 'bo')
    print(x)
    print(y_theory)
    plt.title("Фактор магнитного поля при Omega*Tau = " + str(omega_tau))
    plt.xlabel("Отношение внешнего поля к случайному")
    plt.ylabel("Время релаксации ( 1/(cек^2*Omega) )")

elif plot_type == 'S':
    # this code is unique for most runs, so it'd be ugly
    omega_tau = float(inf[1])
    file = FileOperations('Time_from0,04to1,2_5000.txt')
    y_0 = file.searching(omega_tau)
    y_theory = [y_0 * (1 + (i * omega_tau) ** 2) for i in x]

    x = [i for i in x]

    for i in range(len(y)):
        if y[i] <= 0:
            x.pop(i)
            y.pop(i)

    fun_y = lambda i: np.log(i - y_0)
    y = list(map(fun_y, y))
    y_theory = list(map(fun_y, y_theory))

    plt.plot(x, y_theory, 'bo')
    # plt.title("Логирифм среднего времени релаксации от логарифма времени между столкновениями")
    # plt.xlabel("Логарифм времени между столкновениями")
    # plt.ylabel("Логирифм среднего времени релаксации")

else:
    plt.title("Wrong Input")
    x, y = [0], [0]


print(y_0)
print(x)
print(y)

plt.xlim(min(0, 1.05 * min(x)), 1.05 * max(x))
plt.ylim(min(0, 1.05 * min(y)), 1.05 * max(y + y_theory))

plt.plot(x, y, 'ro')

# for example: Field_from0,04to1,2_5000.txt --> FieldFactor_from0,04to1,2_5000.png
image_name = str(plot_type) + '_' + '_'.join((''.join(file_name.split('.')[:1]) + '.png').split('_')[1:])

plt.savefig('image_files' + '\\' + image_name)
plt.show()
