#!/usr/bin/env python3

import os
import sys

def main():
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        : = open(sys.argv[1])
    else:
        f = sys.stdin

    lines = [x.rstrip() for x in f.readlines()]
    number_testcases = int(lines.pop(0))
    for i in range(number_testcases):
        process_case(lines)


def process_case(lines):
    cities = list()
    n_cities = int(lines.pop(0))
    distance = [[sys.maxsize for x in range(n_cities)] for x in range(n_cities)]

    for i in range(n_cities):
        cities.append(lines.pop(0))
        connections = int(lines.pop(0))
        for j in range(connections):
            k, w = [int(x) for x in lines.pop(0).split(" ")]
            k -= 1
            distance[i][k] = w

    for k in range(n_cities):
        for i in range(n_cities):
            if i == k:
                continue
            for j in range(n_cities):
                if j == k:
                    continue
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    tests = int(lines.pop(0))
    for i in range(tests):
        a, b = [cities.index(x) for x in lines.pop(0).split(" ")]

    lines.pop(0)

if __name__ == "__main__":
    main()
