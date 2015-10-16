from collections import defaultdict, deque
import math

__author__ = 'Logsiny'


class C45:
    class Node:
        def __init__(self, attr_index=None, classification=None):
            if attr_index is None:
                self.attr_index = -1
            else:
                self.attr_index = attr_index
            self.children = defaultdict(C45.Node)
            self.classification = classification

        def __str__(self):
            return '[' + str(self.attr_index) + ', ' + str(self.classification) + ']'

    def __init__(self):
        self.dtree = C45.Node()
        self.attr_values = []

    def preprocess(self, data):
        line_length = len(data[0])
        self.attr_values = [{} for _ in range(line_length)]
        for row in data:
            for i in range(line_length):
                if row[i] not in self.attr_values[i]:
                    self.attr_values[i][row[i]] = 1
                else:
                    self.attr_values[i][row[i]] += 1

    def train(self, data):
        if data:
            ent = entropy(data)
            if ent == 0:  # all samples belong to the same class
                return C45.Node(0, data[0][0])  # what if len(data[0]) == 0
            else:
                gain_ratios = [gain_ratio(data, i, ent) for i in range(1, len(data[0]))] or [0]
                max_ratio = max(gain_ratios)
                if max_ratio == 0:
                    expected_key, expected_value = C45.get_expect(data)
                    return C45.Node(0, expected_key)
                else:
                    max_index = gain_ratios.index(max_ratio) + 1
                    curr = C45.Node(max_index)
                    sub_data = defaultdict(list)
                    for row in data:
                        sub_data[row[max_index]] += [row[:max_index] + row[max_index + 1:]]
                    for value in self.attr_values[max_index]:
                        if value in sub_data:
                            curr.children[value] = self.train(sub_data[value])
                    return curr
        return

    def __str__(self):
        ret = ""
        q = deque()
        q.append(self.dtree)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                ret += curr.__str__() + ', '
                for child in curr.children:
                    q.append(curr.children[child])
            ret += '\n'
        return ret

    @staticmethod
    def get_expect(data):
        max_key = None
        max_value = 0
        if data:
            counts = defaultdict(int)
            for row in data:
                counts[row[0]] += 1
                if not max_key or max_value < counts[row[0]]:
                    max_key = row[0]
                    max_value = counts[row[0]]
        return max_key, max_value


def entropy(data):
    length = len(data)
    counts = defaultdict(int)
    for row in data:
        counts[row[0]] += 1  # what if row[0] doesn't exist? no really possible. row[0] is class bit.
    probs = [counts[cls] / (length * 1.0) for cls in counts]
    info = - sum(prob * math.log(prob, 2) for prob in probs)
    return info


def gain_ratio(data, index, entropy_data=None):
    length = len(data)
    info = entropy_data or entropy(data)
    if index >= length:
        return 0
    groups = defaultdict(list)
    for row in data:
        groups[row[index]] += [row]
    info_attr = sum(len(group) / (length * 1.0) * entropy(group) for group in groups.values())
    if info - info_attr == 0:
        return 0
    split = - sum(len(group) / (length * 1.0) * math.log((len(group) / (length * 1.0)), 2) for group in groups.values())
    return (info - info_attr) / split