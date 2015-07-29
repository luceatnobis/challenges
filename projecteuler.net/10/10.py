#!/usr/bin/env python

from pyprimes import isprime

def main():
	nums = [x for x in range(2,1000 * 1000 * 2)[1::2]if isprime(x)]
	print sum(nums)

main()
