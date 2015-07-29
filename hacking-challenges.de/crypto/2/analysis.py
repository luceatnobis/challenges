#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	freqs = {}

	with open("text") as f:
		line = f.read().rstrip()

	line = str.decode(line, "utf-8")

	for char in line:
		if freqs.has_key(char):
			freqs[char] += 1
		else:
			freqs[char]  = 1

	for key, value in sorted(freqs.iteritems(), key=lambda (key, value): (value, key), reverse=True):
		print key, value


main()
