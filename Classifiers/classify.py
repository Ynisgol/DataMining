from C45 import *
# import sys

__author__ = 'Logsiny'


def read_file(filename):
    with open(filename, 'r') as f:
        data = [line.split() for line in f]
    return data

# dataset = read_file('mushroom.test')
datase1 = [[1, 1, 3],
           [1, 1, 3],
           [2, 1, 4],
           [2, 1, 4],
           [3, 1, 4],
           [3, 1, 4],
           [3, 1, 4],
           [3, 1, 4],
           [1, 2, 3],
           [1, 2, 3],
           [2, 2, 4],
           [2, 2, 4]]

datase2 = [[1, 3, 1],
           [1, 3, 1],
           [2, 4, 1],
           [2, 4, 1],
           [3, 4, 1],
           [3, 4, 1],
           [3, 4, 1],
           [3, 4, 1],
           [1, 3, 2],
           [1, 3, 2],
           [2, 4, 2],
           [2, 4, 2]]
# print gain_ratio(dataset, 1)  # 8 / 12 * 1.5 + 4 / 12 * 1 = 1.3333

dataset3 = [[1, 'm', 'a'],
            [1, 'm', 'a'],
            [1, 'n', 'c'],
            [1, 'n', 'c'],
            [3, 'm', 'b'],
            [3, 'm', 'b'],
            [3, 'n', 'd'],
            [3, 'n', 'd']]

# b = C45.Node(0, 'a')

dataset = read_file('mushroom.test')
"""
with open('mushroom3col.test', 'w+') as f:
    sys.stdout = f
    for row in dataset:
        if row[5] == 'n':
            print row[0], row[5], row[19]
sys.stdout = sys.__stdout__
"""
c = C45()
# c.preprocess(dataset)
c.dtree = c.train(dataset)
testset = read_file('mushroom.training')
print c
control = [row[0] for row in testset]
for row in testset:
    row[0] = 0
result = c.test(testset)

print result
print control

count = 0
for i in range(len(result)):
    if result[i] == control[i]:
        count += 1
print "Accuracy: " + str(count / (len(result) * 1.0))
