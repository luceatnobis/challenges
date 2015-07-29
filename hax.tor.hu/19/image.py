#!/usr/bin/env python

import Image

def main():
	s = 0
	cols = []
	img = Image.open("colors.jpg")
	xDim, yDim = img.size

	ram = img.load()
	for y in range(yDim):
		for x in range(xDim):
			col = ram[x,y]
			cols.append(col)
			#if col == (254, 0, 0) or col == (0, 176, 0) or col == (0, 176, 0):
			#	ram[x,y] = (0,0,0)
			#print col
	cols = set(cols)
	print cols
	for i in cols:
		print [hex(x) for x in i]
			
main()
