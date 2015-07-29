#!/usr/bin/env python

from string import ascii_lowercase as al

def main():
	
	i, j = 10, 0
	
	while True:
		if (i + j) % 26 == al.index("s"):
			print i, j
			break

		j += 1

main()
