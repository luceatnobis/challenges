#!/usr/bin/env python

from pyprimes import isprime
from operator import mul

def main():
	#primes = [x for x in range(3, 501) if isprime(x)]
	firstGroup = sum([x for x in range(3, 101) if isprime(x)])
	secondGroup = 0

	for i in range(100, 201):
		digits = [int(x) for x in str(i) if isprime(i)]
		if digits: secondGroup += reduce(mul, digits)

	thirdGroup = sum([((x * secondGroup) - firstGroup) for x in range(200, 301) if isprime(x)])
	fourthGroup = sum([thirdGroup - (x ** 2) for x in range(300, 401) if isprime(x)])
	fifthGroup = sum([sum([int(x) for x in str(x)]) for x in range(400, 501) if isprime(x)])
	print firstGroup,
	print secondGroup,
	print thirdGroup,
	print fourthGroup,
	print fifthGroup,

main()
