#!/usr/bin/env python

import Image

def main():
	img = Image.open("flag.ico").convert("RGB")
	xDim, yDim = img.size
	ram = img.load()
	
	for y in range(yDim):
		for x in range(xDim):
			print x,y,ram[x,y]

main()
