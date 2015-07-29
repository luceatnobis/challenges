#!/usr/bin/env python

def main():
	products = []	
	for i in range(100,1000):
		for j in range(100, 1000):
			product = i * j
			if int(str(product)[::-1]) == product:
				products.append(i*j)
	products.sort()
	print products[-1]

main()
