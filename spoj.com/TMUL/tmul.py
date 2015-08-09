#!/usr/bin/env python

import sys

lines = [x.rstrip() for x in sys.stdin.readlines()]

for l in lines[1:]:
    x, y = [int(x) for x in l.split(" ")]
    print(x * y)
