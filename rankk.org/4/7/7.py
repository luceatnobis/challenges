#!/usr/bin/env python

import Image

def main(): 
	string = ""
	img = Image.open("amulet.bmp").convert("RGB")
	xDim, yDim = img.size

	ram = img.load()
	for y in range(yDim):
		for x in range(xDim):
			for c in ram[x,y]:
				string += chr(c)

	print string
	print len(string)

main()
