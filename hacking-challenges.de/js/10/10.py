#!/usr/bin/env python

def main():
	a = 64
	b = 0
	c = 60
	while True:
		if (a * b * c) / 120 == 53728:
			break
		b += 1
	print b

main()
