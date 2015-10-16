from C45 import *

__author__ = 'Logsiny'


def read_file(filename):
    with open(filename, 'r') as f:
        data = [line.split() for line in f]
    return data

# dataset = read_file('mushroom.test')
dataset = [[1, 1],
           [1, 1],
           [2, 1],
           [2, 1],
           [3, 1],
           [3, 1],
           [3, 1],
           [3, 1],
           [1, 2],
           [1, 2],
           [2, 2],
           [2, 2]]
# print gain_ratio(dataset, 1)  # 8 / 12 * 1.5 + 4 / 12 * 1 = 1.3333

b = C45.Node(0, 'a')
dataset = read_file('mushroom.training')
c = C45()
c.preprocess(dataset)
c.dtree = c.train(dataset)
print c
