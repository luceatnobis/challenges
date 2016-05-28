#!/usr/bin/env python3

import math

def chunks(line, n=2):
    for i in range(0, len(line), n):
        yield line[i:i+n]

def main():
    plain = list()
    l = [x.rstrip() for x in open("data").readlines()]
    globals().update({k: int(v, 16) for (k, v) in [y.split(" = ") for y in l]})

    """
    <dude12312414> So I'll go back to that: a = b (mod N) means a = b +
    N * k for some integer k.
    """
    
    N = 143
    e = 23
    c = 2

    

if __name__ == "__main__":
    main()
