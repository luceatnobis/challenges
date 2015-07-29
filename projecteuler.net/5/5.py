#!/usr/bin/env python

poss = range(11,21)

def main():
	div = 20

	while True:
		if check(div):
			print div
			break
		div += 1

def check(x):
	for p in poss:
		if x % p != 0:
			return False
		
	return True

main()
