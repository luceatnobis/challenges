#!/usr/bin/env python

from operator import mul

def main():
	x = 6008514751D
	factorlist = []
	loop = 2
	while loop <= x:
		if x % loop == 0:
			x /= loop
			factorlist.append(loop)
		else:
			loop += 1
	print factorlist

main()
