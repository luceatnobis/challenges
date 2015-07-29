#!/usr/bin/env python

import Image

def main():
	img_original = Image.open("original.jpg").convert("RGB")
	img_rankk = Image.open("rankk.jpg").convert("RGB")

	ram_original = img_original.load()
	ram_rankk = img_rankk.load()

	xDim, yDim = img_original.size
	img_difference = Image.new("RGB", (xDim, yDim), "#FFFFFF")
	ram_difference = img_difference.load()

	for y in range(yDim):
		for x in range(xDim):
			if ram_original[x,y] != ram_rankk[x,y]:
				ram_difference[x,y] = ram_rankk[x,y]
	
	img_difference.save("difference.jpg")
main()
