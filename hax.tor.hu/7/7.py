#!/usr/bin/env python

def main():
	chars = []
	f = open("pairs", "r")

	for line in f:
		first, second = line.rstrip("\n").split(" ")
		first = int(first, 16)
		second = int(second, 16)
	
		first = first ^ 0xA5
		second = second ^ 0xA5

		fBin = bin(first)[2:]
		pfBin = (8- len(fBin)) * "0" + fBin
		
		sBin = pfBin[4:] + pfBin[:4]
		print chr(int(sBin,2)),
		
main()
