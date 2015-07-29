#!/usr/bin/env python

def main():
	f = open("colours")
	sum = 0
	for line in f:
		line = line.rstrip("\n")
		print line
		i = int(line, 16)
		sum += i

	print sum

main()
