#!/usr/bin/env python

import sys
import string 

def main():
	alphabet = dict()
	crypt = "21 0 7 15 20 0 9 20 0 9 8 1 20 5 13 1 20 8 19"
	counter = 0
	
	for i in string.ascii_lowercase[::-1]:
		alphabet[counter] = i
		counter += 1

	for i in crypt.rsplit(' '):
		num = int(i)
		sys.stdout.write(alphabet[num])

	sys.stdout.write('\n')

main()
