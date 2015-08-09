#!/usr/bin/env python3
# dict sorting script

import os
import sys

if len(sys.argv) != 2:
    print("No dict found, exiting.", file=sys.stderr)
elif not os.path.exists(sys.argv[1]):
    print("Dict %s not found, exiting." % sys.argv[1], file=sys.stderr)

l = [x.rstrip() for x in open(sys.argv[1]).readlines()]
d = dict(x.split(":") for x in l)

for k, v in sorted(d.items(), key=lambda x: x[1]):
    print("%s:%s" % (k, v))
