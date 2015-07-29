#!/usr/bin/env python

def main():
	line = open("5").read()
	frequency = {} # char : 0...

	for char in line:
		if char in frequency:
			frequency[char] += 1
		else:
			frequency[char] = 1

	for key, value in sorted(frequency.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s" % (key, value)

	
main()
