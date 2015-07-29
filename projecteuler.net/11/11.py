#!/usr/bin/env python

from operator import mul
from functools import reduce


class BoundaryOverFlow(Exception):

    def __str__(self):
        return "BoundaryOverFlow detected"


class Table:

    def __init__(self, table_str):
        maximum = 0
        self.adj = 4
        self.grid = self._huge_into_lists(table_str)

        self.x_len = len(self.grid[0])
        self.y_len = len(self.grid)

        self.chain_funcs = list(getattr(self, x) for x in dir(self) if
                                x.startswith("_chain"))

        pair = (0, 0)

        for pair in self._return_coordinate_pair(self.x_len, self.y_len):
            list_of_chains = self._apply_chains(pair)
            local_max = max(reduce(mul, c) for c in list_of_chains)

            maximum = local_max if maximum < local_max else maximum

        print(maximum)

    def _apply_chains(self, pair):
        """
        Return a list of tuples with the returned chains
        """
        chains = []
        for func in self.chain_funcs:
            try:
                chains.append(func(pair))
            except BoundaryOverFlow:
                continue

        return chains

    def _return_coordinate_pair(self, x_stop, y_stop, x_start=0, y_start=0):
        for y in self._return_coordinate(y_start, y_stop):
            for x in self._return_coordinate(x_start, x_stop):
                yield(y, x)

    def _return_coordinate(self, start, stop):
        for i in range(start, stop):
            yield i

    def _huge_into_lists(self, table_str):
        final_grid = []
        lines = table_str.split("\n")

        for x in (x.split(" ") for x in lines if x):
            final_grid.append([int(y) for y in x])

        return final_grid

    def _chain_north(self, pair):
        """
        Return the chain that goes north
        """
        y, x = pair

        if y - self.adj < 0:
            raise BoundaryOverFlow
        return tuple(self.grid[y-z][x] for z in range(self.adj))

    def _chain_east(self, pair):
        """
        Return the east chain
        """
        y, x = pair

        if x - self.adj < 0:
            raise BoundaryOverFlow
        return tuple(self.grid[y][x-z] for z in range(self.adj))

    def _chain_south(self, pair):
        """
        Return the south chain
        """
        y, x = pair

        if y + self.adj > self.y_len:
            raise BoundaryOverFlow
        return tuple(self.grid[y+z][x] for z in range(self.adj))

    def _chain_west(self, pair):
        """
        Return the west chain
        """
        y, x = pair

        if x + self.adj > self.x_len:
            raise BoundaryOverFlow
        return tuple(self.grid[y][x+z] for z in range(self.adj))

    def _chain_north_east(self, pair):
        """
        Return the north east chain
        """
        y, x = pair

        if y - self.adj < 0 and x - self.adj < 0:
            raise BoundaryOverFlow
        return tuple(self.grid[y-z][x-z] for z in range(self.adj))

    def _chain_north_west(self, pair):
        y, x = pair

        if y - self.adj < 0 or x + self.adj > self.x_len:
            raise BoundaryOverFlow
        return tuple(self.grid[y-z][x+z] for z in range(self.adj))

    def _chain_south_east(self, pair):
        x, y = pair

        if y + self.adj > self.y_len or x - self.adj < 0:
            raise BoundaryOverFlow
        return tuple(self.grid[y+z][x-z] for z in range(self.adj))

    def _chain_south_west(self, pair):
        y, x = pair

        if y + self.adj > self.y_len or x + self.adj > self.x_len:
            raise BoundaryOverFlow

        try:
            return tuple(self.grid[y+z][x+z] for z in range(self.adj))
        except:
            print(y, x)
            print(y + self.adj, x+self.adj)
            raise


def main():
    with open("table") as f:
        table_str = f.read()

    Table(table_str)

main()
