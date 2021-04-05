import matplotlib.pyplot as plt
from File_Operations import FileOperations


file2 = FileOperations('Time_5000_117_from0,04to1,2.txt')

file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.1)
y = [i - y_0 for i in y]
plt.plot(x, y, 'y')

file = FileOperations('Field_0,2_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.2)
y = [i - y_0 for i in y]
plt.plot(x, y, 'r')

file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.3)
y = [i - y_0 for i in y]
plt.plot(x, y, 'b')

file = FileOperations('Field_0,4_2000_16_from1,0to16,0.txt')
_, x, y = file.reading()
y_0 = file2.searching(0.4)
y = [i - y_0 for i in y]
plt.plot(x, y, 'g')

plt.xlim(0, 17)
plt.ylim(0, 100)


'''
file = FileOperations('Field_0,3_2000_16_from1,0to16,0.txt')
_, x1, y1 = file.reading()
file = FileOperations('Field_0,3_2000_17_from-16,0to0,0.txt')
_, x2, y2 = file.reading()
plt.plot(x1, y1, 'ro')
x2 = [abs(i) for i in x2]
plt.plot(x2, y2, 'bo')


file = FileOperations('Field_0,1_2000_16_from1,0to16,0.txt')
_, x1, y1 = file.reading()
file = FileOperations('Field_0,1_2000_17_from-16,0to0,0.txt')
_, x2, y2 = file.reading()
plt.plot(x1, y1, 'ro')
x2 = [abs(i) for i in x2]
plt.plot(x2, y2, 'bo')
'''

plt.show()
