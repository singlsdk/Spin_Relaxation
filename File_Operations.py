import os.path

# TODO: maybe use map (idk how for this file structure)

"""
file structure:

inf(number of modulations and others)   0
x0 y0                                   1
x1 y1                                   2
x2 y2                                   3
...                                     ...

"""


def file_name_creating(inf, x_axis):

    # Example:
    # inf = 'Field 0.3 2000' ; x_axis = [1.0, 2.0, ..., 16.0]  --> 'Field_0,3_2000_16_from1,0to16,0.txt'
    file_name = inf.replace(' ', '_') + '_from' + str(min(x_axis)) + 'to' + str(max(x_axis))
    file_name = file_name.replace('.', ',') + '.txt'

    # file_location = 'text_files' + '\\'
    file_location = FileOperations.file_location
    file_path = file_location + file_name
    if os.path.exists(file_path) == 1:
        print('File exists!')
        return 'Error'

    print(file_name)
    return file_name


class FileOperations:

    file_location = 'text_files' + '\\'

    def __init__(self, file_name):
        self.file_path = FileOperations.file_location + file_name

    def reading(self):
        with open(self.file_path, 'r') as file:
            xy = [line.split() for line in file]
            # xy = [[inf], [x0, y0], [x1, y1], [x2, y2], ...]
            inf = xy[0]
            xy = xy[1:]  # xy = [[x0, y0], [x1, y1], [x2, y2], ...]
            x = [float(i[0]) for i in xy]
            y = [float(i[1]) for i in xy]

        print(inf)
        print(x)
        print(y)

        return inf, x, y

    def searching(self, x_value):
        # for value in x found value in y
        with open(self.file_path, 'r') as file:
            k = 0
            for line in file:
                if k != 0:
                    xy = line.split()
                    if abs(float(xy[0]) - x_value) < 0.0001 * x_value:
                        return float(xy[1])
                k = 1

        print('No required value in x axis')
        return None

    def writing(self, inf, x, y):

        length = len(x)
        if length != len(y):
            print('Wrong Input')
            return None

        # 'w' to delete old file
        with open(self.file_path, 'w') as file:
            file.write(inf + '\n')

        # 'a' to make new line in existing file
        with open(self.file_path, 'a') as file:
            for i in range(length):
                file.write(str(x[i]) + ' ' + str(y[i]) + '\n')

    def reading_bloch(self):
        lst = []
        with open(self.file_path, 'r') as file:
            k = 0
            inf = file.readline()

            for line in file:
                # if k == 0:
                #    inf = line.split()
                #    k = 1
                # else:
                lst.append(line.split())
        print(inf)
        print(lst)

        return inf, lst

    def writing_bloch(self, inf, lst):

        # 'w' to delete old file
        with open(self.file_path, 'w') as file:
            file.write(inf + '\n')

        # 'a' to make new line in existing file
        with open(self.file_path, 'a') as file:
            for i in lst:
                file.write(' '.join([str(j) for j in i]) + '\n')


'''
# location of all text files
file_location = 


def file_reading(file_name):
    with open(file_location + file_name, 'r') as file:
        xy = [line.split() for line in file]
        for line in file:
            xy.append(line.split())
        # xy = [[inf], [x0, y0], [x1, y1], [x2, y2], ...]
        inf = xy[0]
        xy = xy[1:]  # xy = [[x0, y0], [x1, y1], [x2, y2], ...]
        x = [float(i[0]) for i in xy]
        y = [float(i[1]) for i in xy]

    print(inf)
    print(x)
    print(y)

    return inf, x, y


def file_searching(file_name, x_value):
    # for value in x found value in y
    with open(file_location + file_name, 'r') as file:
        k = 0
        for line in file:
            if k != 0:
                xy = line.split()
                if abs(float(xy[0]) - x_value) < 0.0001 * x_value:
                    return float(xy[1])
            k = 1

    print('No required value in x axis')
    return None


def file_writing(file_name, inf, x, y):

    file_path = file_location + file_name

    length = len(x)
    if length != len(y):
        print('Wrong Input')
        return None

    # 'w' to delete old file
    with open(file_location + file_name, 'w') as file:
        file.write(inf + '\n')

    # 'a' to make new line in existing file
    with open(file_name, 'a') as file:
        for i in range(length):
            file.write(str(x[i]) + ' ' + str(y[i]) + '\n')


print(file_reading('Field_Plot.txt'))
'''
