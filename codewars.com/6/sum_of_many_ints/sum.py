#!/usr/bin/env python3

def f(n, m):
    s = 0
    for i in range(1, n):
        s += i % m
    return s

if __name__ == "__main__":
    print(f(15, 10))
