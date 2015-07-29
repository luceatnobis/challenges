#!/usr/bin/env python

from operator import add

def main():
	with open("numbers") as f:
		numbers = [int(x) for x in f.read().split("\n") if x]

	print str(reduce(add, numbers))[:10]

main()
