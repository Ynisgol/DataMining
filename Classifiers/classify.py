#!/usr/bin/python

from C45 import *
import sys

__author__ = 'Meng Shi'


def read_file(filename):
    with open(filename, 'r') as fp:
        data = [line.split() for line in fp]
    return data

dataset = read_file(sys.argv[1])

testset = read_file(sys.argv[2])
control = [row[0] for row in testset]
for row in testset:
    row[0] = 0

c = C45()
c.train(dataset)
result = c.test(testset)

with open(sys.argv[3], 'w+') as f:
    sys.stdout = f
    for element in result:
        print element
    count = 0
    for i in range(len(result)):
        if result[i] == control[i]:
            count += 1
    print "Accuracy: " + str(count / (len(result) * 1.0) * 100) + '%'
sys.stdout = sys.__stdout__
