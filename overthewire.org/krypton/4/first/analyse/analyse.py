#!/usr/bin/env python

def main():
	crypt = open("found1").read().rstrip("\n").replace(" ","")
	keyLen = 6

	identical = ["",] * keyLen

	for i in range(len(crypt)):
		mod = i % keyLen # for modulo classes
		identical[mod] += crypt[i]
	
	for i in range(keyLen):
		f = open(str(i), "w")
		f.write(identical[i])
		f.close()

main()
