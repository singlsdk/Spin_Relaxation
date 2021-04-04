import matplotlib.pyplot as plt
from File_Operations import FileOperations

file = FileOperations('Field_0,1_2000_from1,0to16,0.txt')
_, x, y = file.reading()
plt.plot(x, y, 'yo')

file = FileOperations('Field_0,2_2000_from1,0to16,0.txt')
_, x, y = file.reading()
plt.plot(x, y, 'ro')

file = FileOperations('Field_0,3_2000_from1,0to16,0.txt')
_, x, y = file.reading()
plt.plot(x, y, 'bo')

file = FileOperations('Field_0,4_2000_from1,0to16,0.txt')
_, x, y = file.reading()
plt.plot(x, y, 'go')

plt.xlim(0, 14)
plt.ylim(0, 100)

plt.show()
