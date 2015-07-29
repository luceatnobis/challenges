#!/usr/bin/env python

import Image
import sys

def main():
	try:
		img = Image.open("stegano1.bmp")
	except(IOError):
		print "File couldn't be opened.",
		sys.exit()


	xDim, yDim = img.size
	imgLoad = img.load()
	colours = []

	wat = ""
	for x in range(xDim):
			if imgLoad[x, 0] == (0,255,0):
				wat += ("1")
			else:
				wat += ("0")
	gah = [wat[i:i+8] for i in range(0, len(wat), 8)]
	print gah

main()

