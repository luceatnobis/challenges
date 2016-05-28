#!/usr/bin/env python3

def isValidWalk(walk):
    p = 0+0j
    for d in walk:
        p += {'w': 1+0j, 'e': -1+0j, 's': 0-1j, 'n': 0+1j}[d]
    return len(walk) == 10 and not bool(p)

if __name__ == "__main__":
    print(isValidWalk(['n', 'w', 'e', 's']))
