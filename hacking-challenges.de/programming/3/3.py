#!/usr/bin/env python

import hashlib


def main():
	content = open("2.txt", "r").read()
	#content = "01234561234"
	what = list(content)
	what.sort()
	hashString = "".join(what)
	md5 = hashlib.md5(hashString).hexdigest()
	print md5

main()
