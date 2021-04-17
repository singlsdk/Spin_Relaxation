import matplotlib.pyplot as plt
import numpy as np
from File_Operations import FileOperations

file2 = FileOperations('Time_5000_117_from0,04to1,2.txt')

file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.1)
x = [np.log(i) for i in x]
y = [np.log(abs(i-y_0)) for i in y]
plt.plot(x, y, 'y')
print(max(y))

file = FileOperations('Field_0,2_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.2)
x = [np.log(i) for i in x]
y = [np.log(abs(i-y_0)) for i in y]
plt.plot(x, y, 'r')
print(max(y))

file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.3)
x = [np.log(i) for i in x]
y = [np.log(abs(i-y_0)) for i in y]
plt.plot(x, y, 'b')
print(max(y))

file = FileOperations('Field_0,4_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.4)
x = [np.log(i) for i in x]
y = [np.log(abs(i-y_0)) for i in y]
plt.plot(x, y, 'g')
print(max(y))
'''
file = FileOperations('Field_0,5_2000_11_from1,0to11,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.5)
y = [i - y_0 for i in y]
plt.plot(x, y, 'y')
print(max(y))
'''
plt.xlim(0, 3)
plt.ylim(-10, 10)

plt.savefig(r'image_files\external_fields_log.png')
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
