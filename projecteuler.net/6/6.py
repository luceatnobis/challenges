#!/usr/bin/env python

def main():
	limit = 100
	squareSum = sum([x**2 for x in range(limit+1)])
	squaredSum = sum(range(limit+1)) ** 2

	print squaredSum - squareSum

main()
