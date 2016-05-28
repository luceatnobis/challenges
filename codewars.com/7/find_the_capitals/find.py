#!/usr/bin/env python3

def capitals(n):
    return list(c for c, i in enumerate(n) if i.isupper())

if __name__ == "__main__":
    print(capitals("CodEWaRs"))
