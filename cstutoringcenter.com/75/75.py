#!/usr/bin/env python3


from math import sqrt, floor


def construct_wythoff(n):
    phi = (1+sqrt(5))/2  # golden ratio
    for x in range(1, n + 2):  # including 0 and upper bound
        yield floor(x * phi)
    raise StopIteration


def construct_fibonnaci_sequence(seq, l):
    x, y = seq
    for i in range(l + 1):
        a = x + y
        yield a
        x, y = y, a


def main():
    structure_length = 15
    wythroff_row = list(construct_wythoff(structure_length))

    # construct begin sequences
    fib_sequences = [
        (x, wythroff_row[x]) for x in range(0, structure_length + 1)]

    # fill rows
    columns = []
    for seq in fib_sequences:
        columns.append(list(
            construct_fibonnaci_sequence(seq, structure_length)))

    print(columns[15][15])

if __name__ == "__main__":
    main()
