#!/usr/bin/env python

import imp
ic = imp.load_source("ic", "../4/second/second.py").ic

from string import ascii_lowercase

def build_sequence(number_of_sequences, line): # int, str

	subLists = [ [] for x in range(number_of_sequences) ] 

	for i, char in enumerate(line):
		subLists[i % number_of_sequences] += char

	return  [ "".join(x) for x in subLists ]

def calc_avg_IC(suspectedKeylen, line):
	icSum = 0
	subLists = build_sequence(suspectedKeylen, line)

	for l in subLists:
		joined = "".join(l)
		icSum += ic(joined)
	
	avgIC = icSum / suspectedKeylen
	return avgIC

def rot(string):
	caesard = {}	

	capitals = [i for i, char in enumerate(string) if char.isupper()]

	for rot in range(26):
		lower, modified = string.lower(), ""
		newString = []
		for char in lower:
			newString.append(ascii_lowercase[((ascii_lowercase.index(char) + rot) % len(ascii_lowercase))])

		for i in capitals:
			char = ascii_lowercase.index(newString[i])
			newString[i] = ascii_lowercase[char].upper()
		caesard["".join(newString)] = str(26-rot)
	return caesard

def calc_chi(orgString):
	totalCount, sum1, sum2 = 0, 0, 0
	cleaned_string = [x.lower() for x in orgString if x.lower() in ascii_lowercase]

	counts = [0] * 26
	expected = [0.08167,0.0492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,
				0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,
				0.02360,0.00150,0.01974,0.00074];

	for c in cleaned_string:
		counts[ord(c) - 97] += 1
		totalCount += 1
	
	for i in range(26):
		sum1 = sum1 + pow((counts[i] - totalCount * expected[i]), 2) / (totalCount * expected[i])
	
	return sum1

def main():
	freq, chi = {}, {}

	with open("found1") as f:
		lines = f.read().replace("\n", "")

	for i in range(1,20):
		avgIC = calc_avg_IC(i, lines)
		freq[str(i)] = avgIC

	"""
	for key, value in sorted(freq.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s" % (key, value)
	"""

	suspected_keylength = 9
	decryption_key = [""] * suspected_keylength
	ideal_mapping = [ ["", ""] ] * suspected_keylength
	
	sequenced = build_sequence(suspected_keylength, lines)
	for i, sequence in enumerate(sequenced):
		key, lowest_chi = 0, 0
		chi_to_sequence = {}
		rotated_sequences = rot(sequence)
		for rotated_sequence in rotated_sequences:
			chi_to_sequence[str(calc_chi(rotated_sequence))] = rotated_sequence

		lowest_chi = [key for key, value in sorted(chi_to_sequence.iteritems(), key=lambda (k,v): float(k))][0]
		ideal_mapping[i] = [sequenced[i], chi_to_sequence[str(lowest_chi)]]

	for original, rotation in ideal_mapping:
		print original, rotation
		print ord(original[0]), ord(rotation[0])

main()
