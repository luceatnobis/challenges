#!/usr/bin/env python2.7

import json

from operator import add
from functools import reduce
from collections import Counter


def naughty_or_nice(data):
    # its a mess
    res = reduce(add, (Counter(x.values()) for x in data.values()))
    flipped = {v: k + "!" for k, v in res.iteritems()}

    if len(flipped.keys()) == 1:
        return u"Nice!"
    return flipped[max(flipped.keys())]

if __name__ == "__main__":
    with open("json.js") as f:
        data = json.load(f)
    print naughty_or_nice(data)
