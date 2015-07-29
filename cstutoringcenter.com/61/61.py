#!/usr/bin/env python

import sets
import pyprimes
import operator

def odd_generator():
	n = 1
	while True:

		yield n
		n += 2

def fib_generator():
	a, b = 1, 0
	yield 1

	while True:
		a, b = a + b, a
		yield a

def prime_generator():
	return pyprimes.nprimes(2000)
	

def main():

	odd_gen = odd_generator()
	odd_set = sets.Set()

	fib_gen = fib_generator()
	fib_set = sets.Set()

	prime_gen = prime_generator()
	prime_set = sets.Set()

	for i in range(2000):

		odd_set.add(odd_gen.next())
		fib_set.add(fib_gen.next())
		prime_set.add(prime_gen.next())
	
	intersection = odd_set & fib_set & prime_set
	print reduce(operator.add, intersection)

main()
