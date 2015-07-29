#!/usr/bin/env python

from string import ascii_uppercase as alphabet

def main():
	shifts = [21, 10, 23, 17, 23, 3]
	lShifts = len(shifts)

	crypt = open("../found1").read().rstrip("\n")
	
	for i in range(len(crypt)):
		shift2Use = i % lShifts
		try:
			indexInAlp = alphabet.index(crypt[i])
		except ValueError:
			continue
		#print indexInAlp, indexInAlp + shifts[shift2Use] % 26
		newIndex = (indexInAlp + shifts[shift2Use]) % 26
		print alphabet[newIndex],
main()
