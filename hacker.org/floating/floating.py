#!/usr/bin/env python

from struct import unpack, pack

def main():
	what = 10000010000100010100001011000000
	a = pack("@f", what)
	print unpack("@f", a)
	
main()
