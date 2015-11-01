#!/usr/bin/python
import random

__author__ = 'Logsiny'


class KMeans:
    def __init__(self, data):
        self.clusters = []
        self.points = [KMeans.Point(row, None) for row in data]

    def get_initial_centers(self, k):
        lines = random.sample(range(len(self.points)), k)
        for line in lines:
            self.clusters += [KMeans.Cluster(self.points[line])]
        return

    def __str__(self):
        s = ""
        line_count = 1
        for point in self.points:
            s += str(line_count) + ': ' + str(point) + '\n'
            line_count += 1
        return s

    @staticmethod
    def get_distance(p1, p2):
        """
        Get the Euclidean distance between two points.
        :type p1: KMeans.Point
        :type p2: KMeans.Point
        :rtype: float
        """
        # TODO: if len(p1) != len(p2) raise exception
        return sum((p1.attributes[i] - p2.attributes[i]) ** 2 for i in range(len(p1.attributes))) ** 0.5

    def clustering(self):
        count = 0
        for point in self.points:
            if self.clustering_point(point):
                count += 1
        for cluster in self.clusters:
            cluster.get_center()
        return count

    def clustering_point(self, point):
        """
        Clustering one point
        :param point: KMeans.Point
        :return: True - changed cluster; False - didn't change
        """
        min_dist = None
        min_cluster = None
        for cluster in self.clusters:
            dist = KMeans.get_distance(point, cluster.center)
            if not min_dist or dist < min_dist:
                min_dist = dist
                min_cluster = cluster
        min_cluster.points += [point]
        old_cluster = point.cluster
        point.cluster = min_cluster
        return old_cluster != min_cluster

    class Cluster:
        index = 0

        def __init__(self, center, points=None):
            self.index = KMeans.Cluster.index
            KMeans.Cluster.index += 1
            self.center = center  # center point
            self.points = points or []  # point list

        def __str__(self):
            return str(self.index)

        def get_center(self):
            self.center = KMeans.Point(self.get_mean([point.attributes for point in self.points]), self)

        @staticmethod
        def get_mean(l):
            """
            Get the center of the cluster.
            :param l: a list of points (at least one)
            :return: the center of the points
            """
            count = len(l) * 1.0
            return [sum(e) / count for e in zip(*l)]

    class Point:
        def __init__(self, attributes, cluster):
            self.attributes = attributes
            self.cluster = cluster

        def __str__(self):
            return str(self.attributes) + ', ' + str(self.cluster)


def read_file(filename):
    data = []
    with open(filename, 'r') as f:
        data += [row.split(',') for row in f]
    return data


def clean_data(data):
    new_data = [row[:-1] for row in data]
    return [[float(col) for col in row] for row in new_data]


def ground_truth(data):
    return [row[-1] for row in data]


def print_data(data):
    print '['
    for row in data:
        print '', row, ','
    print ']'


def k_means(database_file, k=3, output_file=''):
    raw_data = read_file(database_file)
    data = clean_data(raw_data)
    classifier = KMeans(data)
    classifier.get_initial_centers(k)
    count_points_changed_cluster = classifier.clustering()
    while count_points_changed_cluster > 0:
        count_points_changed_cluster = classifier.clustering()
    print classifier

    count = {}
    truth = ground_truth(raw_data)
    for i in range(len(classifier.points)):
        idx = classifier.points[i].cluster.index
        clu = truth[i]
        if (idx, clu) in count:
            count[(idx, clu)] += 1
        else:
            count[(idx, clu)] = 1
    for (idx, clu) in count:
        print idx, clu, count[(idx, clu)]


if __name__ == '__main__':
    k_means('bezdekIris.data')
    # a = KMeans.Cluster(None)
    # b = KMeans.Cluster(None)
    # print a.index, b.index
