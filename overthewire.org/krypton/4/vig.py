#!/usr/bin/env python

import re
import sys

from string import ascii_uppercase

expected = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,
			0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,
			0.02360,0.00150,0.01974,0.00074];

def main():

	max_sequence = 15
	period_length = -1
	final_key = []

	with open("../5/found1", "r") as f:
		hint = f.read().replace(" ", "").rstrip("\n")

	avg_ic_collection = {}

	for sequence in range(1, max_sequence):
		
		sequence_list = generate_sequence(hint, sequence)
		sequence_ic = [0] * sequence

		for i in range(sequence):
			sequence_ic[i] = ic( sequence_list[i] )

		avg_ic_collection[sequence] = sum(sequence_ic) / len(sequence_ic)

	for k, v in sorted(avg_ic_collection.iteritems(), key=lambda(k, v): (v), reverse=True):
		print "%s:\t %.13f" % (k, v)

	while period_length == -1:
		try:
			period_length = int(raw_input("Enter a period length: "))
			#input_str = int(raw_input("Enter a period length: "))
			#period_length = avg_ic_collection[input_str]
		except (ValueError): pass
		except (KeyboardInterrupt): sys.exit()

	sequences = generate_sequence(hint, period_length)
	
	for s in sequences:
		caesard = caesar_complete(s)		
		chi_squared = [chi_square(x) for x in caesard]
		final_key.append(chr(chi_squared.index(min(chi_squared)) + 0x41))

	print "The calculated key is \"%s\"; would you like to make changes to that key?" % ("".join(final_key))

	next_one = False
	key_choice = raw_input(">")
	if key_choice.upper() in ["Y", "YES"]: next_one = True

	if next_one:
		while True:
			final_key = raw_input("Please enter the new key: ").upper()
			if not final_key.isalpha() or len(final_key) != period_length: continue
			final_key = list(final_key)
			break

	decrypt_vigenere(hint, final_key)

def decrypt_vigenere(ciphertext, key):

	ciphertext = [ord(x) for x in ciphertext]
	key = [ord(x) for x in key]

	plaintext = []
	keylen = len(key)

	for i, char in enumerate(ciphertext):
		c = char - 0x41
		p = ( 26 - key[i % keylen] - 0x41) % 26
		c = (c + p) % 26
		plaintext.append( chr(c + 0x41) )
	
	print "".join(plaintext)

def caesar_complete(text):

	sequences = []

	if type(text) != "list":
		text = list(text)

	for shift in range(26):
		shift = 26 - shift
		sequences.append(caesar(text, shift))

	return sequences

def caesar(text, shift):

	sequence = []

	for i, char in enumerate(text):
		c = ord(char) - 0x41
		c  = (c + shift) % 26
		sequence.append(chr(c + 0x41))

	return "".join(sequence)

def generate_sequence(base, sequence):

	sequence_list = []

	for i in range(sequence):
		sequence_list.append( [] )

	base = base.upper()
	base = re.sub("[^A-Z]", "", base)

	for i,char in enumerate(base):
		if char not in ascii_uppercase: continue

	for i, char in enumerate(base):
		sequence_list[ i % sequence ].append(char)

	for i in range(sequence):
		sequence_list[i] = "".join(sequence_list[i])

	return sequence_list

def chi_square(sequence):

	totcount, sum1 = 0, 0.0
	counts = [0] * 26

	for i,char in enumerate(sequence):
		counts[ord(char) - 0x41] += 1;
		totcount += 1;

	for i in range(26):
		sum1 = sum1 + pow((counts[i] - totcount*expected[i]),2)/(totcount*expected[i]);

	return sum1	

def ic(plaintext):

	plaintext = plaintext.lower()
	plaintext = re.sub(r"[^a-z]", "", plaintext)

	counts = [0] * 26;
	total_char_count = 0;

	for i in range(26):
		 counts[i] = 0 # initialise

	for i, char in enumerate(plaintext):
		counts[ord(char) - 97] += 1 # count each char's occurence
		total_char_count += 1 # counts total length

	"""
	for i in range(len(counts)):
		print chr(i + 0x61) + ": " + str(counts[i])
	"""

	tsum = 0;

	for i in range(26):
		tsum = tsum + counts[i] * (counts[i]-1)

	ic = float(tsum) / (total_char_count*(total_char_count-1))
	return ic


main()
