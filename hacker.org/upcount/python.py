#!/usr/bin/env python

def calc(depth):
	if depth == 0:
		return 1
	cc = calc(depth - 1)
	what = cc + (depth % 7)
	if ((cc ^ depth) % 4) == 0:
		return cc +1
	else: return cc


def main():
	print calc(50)

main()
