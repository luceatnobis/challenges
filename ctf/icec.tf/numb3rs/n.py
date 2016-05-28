#!/usr/bin/env python3

from string import ascii_lowercase as a

def chunks(line, n=2):
    for i in range(0, len(line), n):
        yield line[i:i+n]


c = "05110006_00111507000104190802_08130308020418".replace("_", "")
print("".join((a[int(x)] for x in chunks(c))))
