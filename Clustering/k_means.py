#!/usr/bin/python
import sys
import math

__author__ = 'Logsiny'


def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        data += [row.split(',') for row in f]
    return data


def clean_data(data):
    """
    This is only used for bezdekIris.data to remove the column that specifies the class.
    :param data: the plain dataset read from file
    :return: cleaned data
    """
    new_data = [row[:-1] for row in data]
    return [[float(col) for col in row] for row in new_data]


def print_data(data):
    print '['
    for row in data:
        print '', row, ','
    print ']'


def get_distance(p1, p2):
    """
    Get the Euclidean distance between two points.
    :param p1: point one
    :param p2: point two
    :return:
    """
    # TODO: if len(p1) != len(p2) raise exception
    return sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))) ** 0.5


def get_mean(l):
    """
    Get the center of the cluster.
    :param l: a list of points (at least one)
    :return: the center of the points
    """
    count = len(l) * 1.0
    return [sum(e) / count for e in zip(*l)]


def k_means(database_file, k=0, output_file=''):
    data = read_file(database_file)
    # print_data(data)
    print_data(clean_data(data))
    print get_distance([6, 2], [3, 6])
    print get_mean([[6, 2], [3, 6], [1, 2]])

if __name__ == '__main__':
    k_means('bezdekIris.data')
