#!/usr/bin/env python
import binascii

def main():
	key = "CARNIVORE"
	i = 0
	byte = open("bin").read().split("\n")
	byte.pop()
	
	"""
	for i in byte:
		print chr(int(i, 2)),
	
	"""
	seq = byte[-10:-1]
	for i in range(len(seq)):
		print chr(int(seq[i], 2) ^ ord(key[i]))
main()
