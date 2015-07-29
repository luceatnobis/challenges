#!/usr/bin/env python

def main():

	d = {}

	with open("data") as f:
		content = f.readlines()

	[x.rstrip("\n") for x in content]

	for line in content:
		if line not in d:
			d[line] = 1
		else:
			d[line] += 1

	for v, k in sorted(d.iteritems()):
		if k == 1: print v, k

main()
