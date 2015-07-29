#!/usr/bin/env python

def main():
	lines = []
	f = open("../keypass")
	for l in f:
		l = l.rstrip("\n").lower()
		lines.append(l)
	
	f.close()
	c, p = lines
	f = open("../krypton4")
	cipherText = f.read().rstrip()
	
	for i in range(len(cipherText)):
		char = cipherText[i].lower()
		if char not in c: continue

		iCrypt= c.index(char)
		print p[iCrypt],
main()
