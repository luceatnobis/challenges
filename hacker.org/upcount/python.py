#!/usr/bin/env python
import pdb

def calc(depth):
    if depth == 0: return 1
    cc = calc(depth - 1)
    # return cc + (depth % 7) + ((((cc ^ depth) % 4) == 0) ? 1 : 0)

def ncalc(depth):
    if depth == 0: return 1
    cc = ncalc(depth - 1)
    m = 1 if (cc ^ depth) % 4 == 0 else 0
    # print("%s %s %s %s" % (depth, m, cc, (cc + (depth % 7) + m)))
    return cc + (depth % 7) + m

def iterative(depth):
    # essentially what we do is, we turn the recursive function
    # into an iterative one so the stackframes dont blow up
    cc = 1
    for i in range(0, depth+1):
        m = 1 if (cc ^ i) % 4 == 0 else 0
        # print("%s %s %s %s" % (i, m, cc, (cc + (i% 7) + m)))
        cc = cc + (i % 7) + m
    return cc

def main():
    """
    print(ncalc(150))
    print(iterative(150))
    """
    # print(ncalc(11589))
    print(iterative(11589))

main()
