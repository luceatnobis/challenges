#!/usr/bin/env python

import re

def get_ic(plaintext):

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
	
	print total_char_count, tsum
	print ic

def main():
	#get_ic("pnfuthapyjzrplmhvuwzyvytrtiuxudghvmmhkgtmkmkwgivlmljqiivnlveiimjydatmclydufiumavkdeuayvqhqgpyjwdevullpt")
	#print len("pnfuthapyjzrplmhvuwzyvytrtiuxudghvmmhkgtmkmkwgivlmljqiivnlveiimjydatmclydufiumavkdeuayvqhqgpyjwdevullpt")
	get_ic("juww tdru mdh zpiu fdwiut gzkf fhqfgkghgkdr skazuc prt gzu jdct gzpg mdh ruut vdc gzu prfjuc kf pwazpqug")

main()
