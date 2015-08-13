#!/usr/bin/env python3

import string

alpha = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghij"
)

def makehash(s, mult):
    h = 0
    for i, val in enumerate(s):
        h = h * mult + alpha.index(s[i]) + 1
    return h
