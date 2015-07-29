#!/usr/bin/env python

import Image
import sys

def main():
	try:
		img = Image.open("stegano3.bmp")
	except(IOError):
		print "File couldn't be opened.",
		sys.exit()

	colCounter = 0
	colourList = []

	xDim, yDim = img.size
	imgLoad = img.load()

	for y in range(yDim):
		for x in range(xDim):
			colourList.append(imgLoad[x,y])
	print set(colourList)
	

main()
