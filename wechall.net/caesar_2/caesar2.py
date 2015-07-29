#!/usr/bin/env python

def main():
	freqs = {}

	with open("stuff3") as f:
		line = f.read().rstrip("\n").replace(" ","")
	original = str.decode(line, "hex")

	for i in original:
		if i in freqs:
			freqs[i] += 1
		else:
			freqs[i] = 1

	#for key, value in sorted(freqs.iteritems(), key=lambda(k,v): v, reverse=True):
	#	print str.encode(key, "hex"), value
	
	for add in range(128):
		new_string = ""
		for i, char in enumerate(original):
			new_string += chr((ord(char) + add) % 128)
		raw_input("Please press enter")
		print add, new_string

main()
