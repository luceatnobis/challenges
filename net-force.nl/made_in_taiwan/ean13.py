#!/usr/bin/env python

import Image

def read():
	img = Image.open("ean13.gif").convert("RGB")
	xDim, yDim = img.size
	ram = img.load()

	string = ""

	#for x in range(xDim):
	for x in range(xDim):
		if ram[x,0][0] < 150:
			string += "1"
		else:
			string += "0"
	string = string[3:len(string)-3].replace("01010", "")
	print len(string)

def main():
	read()

main()
