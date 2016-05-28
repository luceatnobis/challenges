#!/usr/bin/env python3

def f4(x): return x.split()
def f5(xs): return [x[::-1].title() for x in xs]
def f6(xs): return "_".join(xs)

def chained(f):
    pass

if __name__ == "__main__":
    print(chained([f4,f5,f6])("lorem ipsum dolor"))
