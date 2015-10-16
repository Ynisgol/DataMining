from C45 import *
# import sys

__author__ = 'Logsiny'


def read_file(filename):
    with open(filename, 'r') as f:
        data = [line.split() for line in f]
    return data

dataset = read_file('mushroom.training')

c = C45()
c.train(dataset)
testset = read_file('mushroom.test')
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
