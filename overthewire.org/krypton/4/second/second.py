#!/usr/bin/env python

from string import ascii_uppercase as al

def ic(cipherText):
    f, fi = {}, 0

    for c in cipherText:
        try:
            f[c] += 1
        except:
            f[c] = 1

    for k, v in f.iteritems():
        fi += v * (v-1)

    ic = fi / float( len(cipherText) * (len(cipherText) - 1) )
    return ic

def main():
	crypt = "".join(c for c in open("found2").read() if c in al)
	cLen = len(crypt)

	for i in range(2,3):
		sequences = ["",] * i
		for j in range(cLen)[i::i]:
			print i,j, crypt[j-1]

if __name__ == "__main__":
	main()
