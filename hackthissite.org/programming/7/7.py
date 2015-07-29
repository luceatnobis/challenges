#!/usr/bin/env python

import Image
import sys

def main():
	try:
		img = Image.open("BMP.png").convert("RGB")
	except IOError:
		print "Datei wurde nicht gefunden."
		sys.exit()

	ram = img.load()
	xDim, yDim = img.size

	for y in range(yDim):
		print ram[0, y]

main()
