#!/usr/bin/env python

def main():
	max, sum = 1000, 0

	for i in range(max):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	print sum

main()
