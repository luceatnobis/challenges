#!/usr/bin/env python

import Image

def main():
	img = Image.open("rankkix.gif").convert("RGB")
	ram = img.load()

	x_dim, y_dim = img.size

	for y in range(y_dim):
		for x in range(x_dim):
			if ram[x,y] != (255,255,255):
				ram[x,y] = (0,0,0)

	img.save("fgt.gif")

main()
