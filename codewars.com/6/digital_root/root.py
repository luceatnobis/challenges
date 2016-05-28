#!/usr/bin/env python3

def digital_root(n):
    s = sum(map(int, list(str(n))))
    return s if s < 10 else digital_root(s)

if __name__ == "__main__":
    print(digital_root(24))
