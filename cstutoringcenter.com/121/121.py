#!/usr/bin/env python

def main():
	fileArray = []
	f = open("p120.txt")
	for line in f:
		line.rstrip()
		fileArray.append(line.split())
	f.close()
	for columnIndex in range(len(fileArray))[:len(fileArray)-4]: # getting the column index
		subList = []
		for i in range(4):
			subList.append(fileArray[columnIndex+i])
		for rowIndex in range(4):
			

main()
