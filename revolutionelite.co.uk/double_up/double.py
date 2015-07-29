#!/usr/bin/env python

def digit_root(num):

	root = sum([int(x) for x in str(num)])
	if root > 9: return digit_root(root)
	else: return root

def main():

	x = 0
	y = 0
	double_num = 1	

	""" # this is supposed to calculate x...very inefficient. 23 secs
	while True:
		double_num *= 2
		x += 1
		if len(str(double_num)) == 10000:
			print x
			print double_num
			break
	"""

	with open("info", "r") as f: # loading it from a file for testing purposes
		content = [x.rstrip('\n') for x in f.readlines()]

	x = content[0]
	double_num = content[1]

	for bad_i, char in enumerate(double_num):
		comp_i = digit_root(bad_i + 1)
		if comp_i == int(char):
			y += 1
	
	print int(x) * y
main()
