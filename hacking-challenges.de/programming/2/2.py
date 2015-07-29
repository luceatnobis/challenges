#!/usr/bin/env python

def main():
	string =  open("2.txt", "r").read()
	#string = "12345678901234567890123456789098765432100"
	absIndex, result = 0,0

	while True:
		try:
			for i in range(30):
				result += int(string[absIndex])
				absIndex += 1
			for i in range(10):
				result -= int(string[absIndex])
				absIndex += 1
		except IndexError:
			break
	print result

main()
