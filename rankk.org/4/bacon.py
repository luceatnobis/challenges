#!/usr/bin/env python
from string import ascii_lowercase as lo, ascii_uppercase as up

def main():
	uppercase, lowercase = "a", "b"
	letters = { "aaaaa" : "a", "aaaab" : "b", "aaaba" : "c", "aaabb" : "d", "aabaa" : "e",
				"aabab" : "f", "aabba" : "g", "aabbb" : "h", "abaaa" : "j", "abaaa" : "i",
				"abaab" : "k", "ababa" : "l", "ababb" : "m", "abbaa" : "n", "abbab" : "o",
				"abbba" : "p", "abbbb" : "q", "baaaa" : "r", "baaab" : "s", "baaba" : "t",
				"baabb" : "u", "baabb" : "v", "babaa" : "w", "babab" : "x", "babba" : "y",
				"babbb" : "z"
			}
	with open("message") as f:
		message = [x for x in f.read() if x in up or x in lo]

	new_list = []
	for char in message:
		if char in up:
			new_list.append(uppercase)
		else:
			new_list.append(lowercase)

	print "".join(new_list)
	for set in range(new_list:
		print set[

main()
