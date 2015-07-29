#!/usr/bin/env python

def main():
	for i in range(1,10):
		for j in range(1,10):
			for k in range(1,10):
				for l in range(1,10):
					if i * j * k * l == 3240:
						print i,j,k,l				

def divisorGen(n):
	possFac = []
	for fac in range(1,n/2+1):
		if n % fac == 0:
			possFac.append(fac)
	return possFac

main()
