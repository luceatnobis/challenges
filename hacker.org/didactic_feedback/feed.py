#!/usr/bin/env python

def main():
	string = str.decode("751a6f1d3d5c3241365321016c05620a7e5e34413246660461412e5a2e412c49254a24","hex")
	print string
	for a in range(256):
		k = a
		for i in range(len(string)):
			c = ord(string[i]) ^ k
			print chr(c),
			k = c
		print 	
			
main()
