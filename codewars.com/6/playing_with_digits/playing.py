#!/usr/bin/env python

def dig_pow(n, p):
    from itertools import count as c
    s = sum([pow(int(i), m) for i, m in zip(str(n), c(p))]) / float(n)
    return s if s.is_integer() else -1

if __name__ == "__main__":
    print(dig_pow(46288, 3))
    print(dig_pow(46283, 3))
