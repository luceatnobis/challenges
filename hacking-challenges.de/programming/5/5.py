#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from base64 import encodestring as b64
import hashlib

def main():
	with open("what") as f:
		#line = f.read().split("\n")
		line = str.decode(f.read(), "utf-8").split("\n")

	"""
	for w in line:
		print w, "".join([hex(ord(c))[2:] for c in w.upper()])
	"""
	hashes = []

	for word in [x for x in line if x]:
		#if word != u"Zusammenschluß": continue
		len_original = len(word)
		print "Length of word:", len_original

		first_word = "".join( [(c + str(len_original)) for c in word ])
		print "First step:", first_word

		second_word = first_word[::-1]
		print "Second step:", second_word	

		third_word = second_word.upper()
		print "Third step:", third_word

		fourth_word = "".join([hex(ord(c))[2:] for c in third_word])
		print "Fourth step:", fourth_word 

		fifth_word = b64(fourth_word).replace("\n", "")
		print "Fifth step: \"" +  fifth_word + "\""
	
		sixth_word = fifth_word.lower()
		print "Sixth step:", sixth_word

		seventh_word = sixth_word.replace("=", "")
		print "Seventh step:", seventh_word

		eigth_word = hashlib.md5(seventh_word).hexdigest()
		print "Eighth step:", eigth_word

		hashes.append(eigth_word)

	print hashlib.md5("".join(hashes)).hexdigest()
	#print hashes
main()
