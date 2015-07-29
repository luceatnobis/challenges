#!/usr/bin/env python3

import os
from signal import signal

from pyprimes import isprime

def stuff(a, b):
    print(prime_counter)

signal(10, stuff)

def xnacchi(x):
    counter = 0
    stem = []

    while True:
        if counter < x:
            stem.append(1)
            counter += 1
            yield 1
        else:
            new = sum(stem)
            stem.append(new)
            stem.pop(0)
            yield new

i = 0
prime_counter = 0
if __name__ == "__main__":
    x = 25
    mod = 1000 ** 2
    terms = 1000 ** 2
    g = xnacchi(x)
    sequence = list()

    for i in range(terms):
        n = next(g)
        modded = n % mod
        if not isprime(modded):
            continue
        prime_counter += 1
    print(prime_counter)
