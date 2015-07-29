#!/usr/bin/env python

import Image

def main():
	img = Image.open("tryout2.php.png").convert("RGB")
	xDim, yDim = img.size

	ram = img.load()
	for y in range(yDim):
		for x in range(xDim):
			#print ram[x,y]
			if ram[x,y] != (0, 200, 255):
				print "happened"
				ram[x,y] = (0,0,0)

	img.save("output.png")

main()
