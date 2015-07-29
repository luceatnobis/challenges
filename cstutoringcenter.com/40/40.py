#!/usr/bin/env python3


def mod_triangle():
    yield [1]
    yield [1, 1]
    line = [1, 2, 1]
    yield line
        
    while True:
        pnl_u = [sum([v, line[i+1]]) for (i, v) in enumerate(line[:-1])]
        new_line = [1] + [x % 100 for x in pnl_u] + [1]

        yield new_line
        line = new_line

def main():
    total_row_sum = 0
    mod_gen = iter(mod_triangle())
    for i in range(25000):
        total_row_sum += sum(next(mod_gen))
    print(total_row_sum)

if __name__ == "__main__":
    main()
