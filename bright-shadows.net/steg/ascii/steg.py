#!/usr/bin/env python

import Image

def main():
	img = Image.open("stegano5.png")
	xDim, yDim = img.size

	ram = img.load()

	for x in range(yDim)[::16]:
		for y in range(xDim)[::16]:
			for char in ram[x,y]:
				print chr(char),
		print

main()
