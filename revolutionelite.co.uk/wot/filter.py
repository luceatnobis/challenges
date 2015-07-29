#!/usr/bin/python

def main():
	f = open("list", "r")
	n = open("newList", "w")
	
	for line in f:
		line = line.rstrip('\n')
		if len(line) == 4:
			n.write(line + "\n")
			
main()
