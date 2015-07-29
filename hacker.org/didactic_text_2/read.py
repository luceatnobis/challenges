#!/usr/bin/env python

from string import lowercase 

def main():
	f = open('numbers', 'r')
	for line in f:
		line.rstrip()
		print lowercase[int(line)],
main()
