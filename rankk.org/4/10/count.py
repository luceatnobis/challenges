#!/usr/bin/env python

def main():

	letters = {}

	with open("count-and-wonder") as f:
		lines = f.read().replace("\r\n", "")

	for char in lines:
		if char in letters:
			letters[char] += 1
		else:
			letters[char] = 1

	print letters

	for key, value in sorted(letters.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print key, value

main()
