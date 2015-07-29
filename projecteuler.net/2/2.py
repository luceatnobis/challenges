#!/usr/bin/env python

def main():
	a, b = 1, 1
	numbers = []

	while True:
		print a
		a, b = a+b, a
		if a >= 4 * 1000 * 1000: break
		if a % 2 == 0: numbers.append(a)

	print sum(numbers)		
	
main()
