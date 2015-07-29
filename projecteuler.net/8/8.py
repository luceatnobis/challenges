#!/usr/bin/env python3

import functools

def adjacent_chunks(big):
    step = 13

    for i, item in enumerate(big):
        stop = step + i
        if stop > len(big):
            raise StopIteration

        yield [int(x) for x in big[i:stop]]


def main():
    max_result = 0

    with open("big_number") as f:
        big_number = str(int(f.read().rstrip()))

    for chunk in adjacent_chunks(big_number):
        temp_res = functools.reduce(lambda x, y: x * y, chunk)

        if temp_res > max_result:
            max_result = temp_res

    print(max_result)

main()
