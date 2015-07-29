#!/usr/bin/env python

import sys

def main():
	string = "84 104 101 32 115 101 99 114 101 116 32 119 111 114 100 32 121 111 117 39 114 101 32 115 101 97 114 99 104 105 110 103 32 102 111 114 32 105 115 32 115 101 99 114 101 116"

	for i in string.rsplit(' '):
		num = int(i)
		sys.stdout.write(chr(num))

	sys.stdout.write('\n')
main()
