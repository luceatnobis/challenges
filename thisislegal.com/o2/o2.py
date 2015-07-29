#!/usr/bin/env python

from string import ascii_lowercase as al

def main():
	reverse_key = []
	key = "enc"
	string = "rwfwcvttw ufriifyg dws jjbhwooqm ezu iwsh".replace(" ","")
	new_string = ""

	for i, char in enumerate(string):
		key_char = key[ i % len(key) ]
		key_char_index = al.index( key_char ) + 1
		char_index = al.index( char) + 1

		new_index = char_index - key_char_index
		reverse_key.append(al[new_index-1])

	print "".join(reverse_key)

main()
