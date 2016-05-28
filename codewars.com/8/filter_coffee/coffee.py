#!/usr/bin/env python2.7

def search(budget, prices):
    return ",".join(map(str, sorted([x for x in prices if budget >= x])))

print(search(3, [6, 1, 2, 9, 2]))
print(search(14, [7, 3, 23, 9, 14, 20, 7]))
