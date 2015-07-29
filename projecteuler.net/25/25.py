#!/usr/bin/env python

def main():
	counter, a, b = 1, 0, 1
	while True:
		a, b = a + b, a
		if len(str(a)) >= 1000: print counter, a; break
		counter += 1

main()
