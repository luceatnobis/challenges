#!/usr/bin/env python

def main():

	expected = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,
	0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,
	0.02360,0.00150,0.01974,0.00074];

	string = "VURZJUGRGGUGVGJQKEOAGUGKKQVWQP"
	sum1, totcount = 0, 0
	counts = [0] * 26

	for i, char in enumerate(string):
		counts[ord(string[i]) - 0x41]+= 1
		totcount += 1
	
	for i in range(26):
		sum1 += pow(( counts[i] - totcount * expected[i]), 2) / (totcount * expected[i])
	print sum1
main()
