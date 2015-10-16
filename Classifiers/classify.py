__author__ = 'Logsiny'


def read_file(filename):
    with open(filename, 'r') as f:
        data = [line.split() for line in f]
    return data

print read_file('mushroom.test')

