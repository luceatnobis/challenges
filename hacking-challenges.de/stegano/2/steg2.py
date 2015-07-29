#!/usr/bin/env python

import Image

def main():
	img = Image.open("stegano_2.jpg").convert("RGB")
	xDim, yDim = img.size
	ram = img.load()

	for y in range(yDim):
		for x in range(xDim):
			if ram[x,y] != (0,0,0):
				ram[x,y] = (0,0,255)
	img.show()

main()
