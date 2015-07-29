#!/usr/bin/env python

def main():
	base, exp = 2, 1000
	res = pow(base, exp)
	digits = [int(x) for x in list(str(res))]
	print sum(digits)

main()
