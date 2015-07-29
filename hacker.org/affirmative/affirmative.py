#!/usr/bin/env/ python

import sys
from string import uppercase
from colorama import Fore

def main():
	file = open("what", "r")
	try:
		for line in file:
			line.rstrip("\n")
			for word in line.split(" "):
				word.rstrip("\n")
				char = chr(int(word, 16))
				if char.isupper():
					sys.stdout.write(Fore.RED + char + Fore.WHITE)
				else:
					sys.stdout.write(chr(int(word,16)))
	except ValueError:
		print word,
main()
