#!/usr/bin/env python

def main():
	secret_num = 7
	char_list = [71, 72, 77, 25, 79, 62, 75, 82, 25, 76, 62, 60, 78, 75, 62]

	for char in char_list:
		print chr(char + secret_num),

main()
