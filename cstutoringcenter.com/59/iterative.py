#!/usr/bin/env python3


min_weight = 0xFFFFFFFF
weights = list()


class Node:

    def __init__(self, value):
        self.value = value
        self.nodes = list()

    def add_node(self, node):
        self.nodes.append(node)

    def process_value(self, chain=[0]):
        global min_weight, weights
        if not self.nodes:
            chain.append(self.value)
            weight_on_branch = sum(chain)
            if weight_on_branch < min_weight:
                min_weight = weight_on_branch
        else:
            for node in self.nodes:
                node.process_value(chain + [self.value])

    def __repr__(self):
        return str(self.value)


def main():
    t_name = "triangle"
    grid = list()
    triangle = open(t_name).readlines()

    for i, row in enumerate(triangle):
        nrs = [int(x) for x in (row.rstrip().split(" "))]
        grid.append([Node(x) for x in nrs])

    for i, row in enumerate(grid[:-1]):
        for j, node in enumerate(row):
            node.add_node(grid[i+1][j])
            node.add_node(grid[i+1][j+1])
    root = grid[0][0]
    root.process_value()

    print(min_weight)

main()
