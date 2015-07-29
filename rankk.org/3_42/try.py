#!/usr/bin/env python

def solve(string):

	chars = [string[i:i+2] for i in range(0,len(string), 2)]
	new_chars = []

	for index, char in enumerate(chars):
		added = (len(string)/2) - index
		new_char = int(char, 16) - added

		if new_char % 2 != 0:
			new_char -= 2
		new_chars.append(new_char)

	return "".join(chr(x) for x in new_chars)

print solve("739B9D9895939EA45447A1969B43868C843F89913F3B718B7B7E8D8A347E87318477752D816E6F7B6F6B267E7575662F")
