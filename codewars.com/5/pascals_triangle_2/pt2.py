#!/usr/bin/env python
import pdb

def pascal(num):
    t = [[1]]
    if num == 1:
        return t

    for c, r in enumerate(t, 2):
        n = [r[0]]
        for i, v in enumerate(r[1:], 1):
            n.append(r[i-1] + r[i])
        n.append(1)
        t.append(n)
        if c == num:
            break
    return t

if __name__ == "__main__":
    print(pascal(1))
    print(pascal(2))
    print(pascal(3))
