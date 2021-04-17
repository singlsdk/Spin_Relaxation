import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from Modulation import spin_precession_modulation
from File_Operations import FileOperations

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([-1.2, 1.2])
ax.set_ylim3d([-1.2, 1.2])
ax.set_zlim3d([-1.2, 1.2])

line, = ax.plot([], [], [], lw=2)

u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="skyblue")

ax.scatter(0, 0, 0)

num = 100
relaxation_circle = np.linspace(0, 2*np.pi, num)
relaxation_circle_y = [-np.cos(1)] * num
ax.plot(np.sin(1)*np.sin(relaxation_circle), relaxation_circle_y, np.sin(1)*np.cos(relaxation_circle), color='r')
# because relaxation angle is 1


def init():
    line.set_data_3d([], [], [])
    return line,


x_data, y_data, z_data = [], [], []


omega_tau = 0.4
outside_omega_value = 10

outside_omega = [0, - outside_omega_value, 0]  # spin_position_initial = [0, spin_length, 0]
spin_position_list = spin_precession_modulation(omega_tau, outside_omega, frames_number=10000)

inf = str(omega_tau) + ' ' + ' '.join([str(i) for i in outside_omega])

file = FileOperations('Bloch_' + (str(omega_tau) + ' ' +
                                  str(outside_omega_value)).replace('.', ',').replace(' ', '_') + '.txt')
file.writing_bloch(inf, spin_position_list)

if outside_omega_value == 0:
    multiplier = 0
else:
    multiplier = 1.1 / outside_omega_value

ax.quiver(0, 0, 0, outside_omega[0]*multiplier,
          outside_omega[1]*multiplier, outside_omega[2]*multiplier, color='g')


def animate(i):
    spin_position = spin_position_list[i]
    x_data.append(spin_position[0])
    y_data.append(spin_position[1])
    z_data.append(spin_position[2])
    line.set_data_3d(x_data, y_data, z_data)

    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(spin_position_list), interval=10, blit=True)

# anim.save('Spin_Relaxation_Bloch_Sphere_Animation.gif')
plt.show()

'''
file = FileOperations('Bloch_0,4_10.txt')
inf, spin_position_list = file.reading_bloch()
inf = inf.split()

print(inf)
outside_omega = [float(inf[i]) for i in range(1, 4)]
outside_omega_value = la.norm(outside_omega)
'''