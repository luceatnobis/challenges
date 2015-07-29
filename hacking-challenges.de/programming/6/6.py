#!/usr/bin/env python

def main():
	counter = 0

	for num in range(101, 1000):
		print num
		querSumme = sum([int(x) for x in str(num)])
		
		while True:
			num = num / float(querSumme)	
			if 1 > num: break
			counter += 1
	print counter

main()
