#!/usr/bin/env python

import Image

def main():
	image = Image.open("file.jpg").convert("RGB")
	xDim, yDim = image.size
	ram = image.load()
	for y in range(416,418):
		for x in range(0, xDim):
			print ram[x,y]

main()
