#!/usr/bin/env python

from string import printable

def main():
	f = open("string", "r")
	hexString = ""
	for i in f:
		hexString = i.strip()

	hexString = list(str.decode(hexString,"hex"))	
	key = [0,0,0,0]
	combinations = {}

	for slot in range(len(key)):
		combinations[str(slot)] = []
		for key[slot] in range(256):
			string = ""
			for i in range(len(hexString))[slot::4]:
				string += chr(ord(hexString[i]) ^ key[slot])
				#print i, hexString[i], key[i % len(key)]

			if all(char in printable for char in string):
				combinations[str(slot)].append(key[slot])
				#print key[0]
	
	decrypted = ""
	for i in range(len(hexString)):
		testKey	= [211, 30, 44, 239]
		decrypted += chr(ord(hexString[i]) ^ testKey[i%len(testKey)])
	print decrypted
		

	"""
	for one in combinations["2"]:
		string = ""
		for i in range(len(hexString))[2::4]:
			string += chr(ord(hexString[i]) ^ one)
		print one,string
	
	for one in combinations["0"]:
		for two in combinations["1"]:
			for three in combinations["2"]:
				for four in combinations["3"]:
					decrypted = ""
					testKey	= [one, two, three, four]
					print testKey
					for i in range(len(hexString)):
						#print i, hexString[i], testKey[i%len(testKey)]
						decrypted += chr(ord(hexString[i]) ^ testKey[i%len(testKey)])
					print decrypted
	"""
main()
