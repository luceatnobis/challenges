#!/usr/bin/env python3

triangle = []
counter = 0


def add_line():
    global counter, triangle
    present_rows = len(triangle)
    if present_rows == 0:
        triangle.append([0])
        counter += 1
        print(triangle)
    else:
        triangle.append([counter])
        counter += 1
        r = len(triangle)


def calculate_sum(n):
    global triangle
    x, y = None, None
    # lets calculate coords
    for i, row in enumerate(triangle):
        if n not in row:
            continue
        x = i
        y = row.index(n)

def main():
    while counter < 3:
        add_line()
    
    print(triangle)
    # calculate_sum(18)


if __name__ == "__main__":
    main()
