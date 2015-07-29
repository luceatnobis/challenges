#!/usr/bin/env python

def main():
	lines = {}
	f = open("lines", "r")
	
	for line in f:
		line = line.rstrip("\n")
		if line in lines:
			lines[line] += 1
		else:
			lines[line] = 1

	for key in lines:
		if lines[key] == 1:
			print key

main()
