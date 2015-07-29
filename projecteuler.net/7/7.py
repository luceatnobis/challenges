#!/usr/bin/env python

from operator import mul

def main():
	products = []
	num = open("string", "r").read()

	for i in range(len(num)-5):
		digits = map(int, list(num[i:i+5]))
		products.append(reduce(mul, digits))

	products.sort()
	print products[-1]
main()
