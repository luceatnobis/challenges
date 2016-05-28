#!/usr/bin/env python3

import pdb

c = []
grid = []

"""
y2 = (y + lines + star[s][i][0]) % lines;
x2 = (x + llen + star[s][i][1]) % llen;
"""

star = [
    # y, x                long-short
    [-2, -1], [-2, 1],  # up-left, up-right
    [2, -1], [2, 1],    # right-up, right-down
    [2, 1], [2, -1],    # down-right, down-left
    [-2, 1], [-2, -1],  # left-down, left-up
]

Y, X = 6, 6

def knight(y, x, n):
    if n == 0:
        pdb.set_trace()
        # print(c)
    else:
        # b, grid[y][x] = grid[y][x], 0xFF
        c.append(grid[y][x])
        grid[y][x] = 0xFF
        for s in star:
            y2 = (y + Y + s[0]) % Y
            x2 = (x + X + s[1]) % X

            if grid[y2][x2] == 0xFF:
                continue
            if n - 1 > 0:
                knight(y2, x2, n - 1)
                print(c)
        grid[y][x] = c.pop()
        # b = grid[y][x]

def main():
    with open("grid") as f:
        for l in f:
            grid.append([int(x) for x in l.rstrip()])

    knight(5, 1, 4)
    # pdb.set_trace()
    pass

if __name__ == "__main__":
    main()
