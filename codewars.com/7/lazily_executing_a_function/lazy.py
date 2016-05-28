#!/usr/bin/env python3

def modding(a, b):
    return a % b

def make_lazy(*args):
    f, args = args[0], args[1:]
    return lambda args: f(*args)

if __name__ == "__main__":
    l = make_lazy(modding, 4, 4)
    import pdb
    pdb.set_trace()
