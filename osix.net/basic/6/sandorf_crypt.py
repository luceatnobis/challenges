#!/usr/bin/env python

def pad_to_n(base, length):
	if base == length: return 0
	return (length - base % length)

def crypt(original_message):

	matrix = [
		[27, 00, 18, 01, 28, 02],
		[19, 29,  9, 30, 03, 10],
		[31, 20, 04, 11, 21, 32],
		[12, 05, 33, 22, 06, 13],
		[34, 23, 14, 35, 15, 07],
		[24, 16, 25,  8, 26, 17],
	]

	original_message = "abcdefghijklmnopqrstuvwxyz0123456789"
	app_rev = (original_message + ("#" * pad_to_n(len(original_message), 36)))[::-1]

	trans_string = [''] * 36

	counter = 0
	for sublist in matrix:
		for item in (sublist):
			trans_string[item] = app_rev[counter]
			counter += 1
	return "".join(trans_string)

def decrypt(original_message):

	chunks = []
	matrix = [1,3,5,10,14,19,22,29,33,8,11,15,18,23,26,28,31,35,2,6,13,16,21,25,30,32,34,0,4,7,9,12,17,20,24,27]

	for i in range(0, len(original_message), 36):
		block = original_message[i:i+36]
		string = ""
		for x in matrix:
			string += block[x]
		chunks.append(string)

	return "".join(chunks)[::-1]



def main():

	with open("crypt0.bin") as f:
		content = f.read()

	#print "".join([ decrypt(content[x:x+36]) for x in range(1, len(content), 36) ])
	print decrypt(content)
	

main()
