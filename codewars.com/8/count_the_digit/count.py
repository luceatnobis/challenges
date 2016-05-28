#!/usr/bin/env python2.7
# count the digit

import pdb

def nb_dig(n ,d):
    d = str(d)
    counter = 0
    for k in xrange(0, n+1):
        counter += str(k**2).count(d)
    return counter


if __name__ == "__main__":
    print nb_dig(5750, 0)
    print nb_dig(11011, 2)
    print nb_dig(10, 1)
