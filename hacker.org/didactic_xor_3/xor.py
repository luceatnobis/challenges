#!/usr/bin/env python

import sys

def main():
	
	txt = "31cf55aa0c91fb6fcb33f34793fe00c72ebc4c88fd57dc6ba71e71b759d83588"

	txt = [int(txt[i:i+2],16) for i in range(0, len(txt), 2)]

	for b in range(256):
		key = b
		for x in range(256):
			sol = ""
			for num in txt:
				sol = sol + chr(num ^ key)
				key = (key + x) % 256
			if "the" in sol:
				print sol
				sys.exit()
main()
