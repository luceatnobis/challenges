#!/usr/bin/env python

from string import ascii_lowercase as al

def main():
	text, new_text, key = "", "", "vjwqwc"

	with open("krypton4") as f:
		text = f.read().lower().rstrip("\n")

	for i, c in enumerate(text):
		index_of_key = al.index(key[i % len(key)])
	
		new_text += al[(index_of_key + al.index(c)) % 26]

	print new_text

main()
