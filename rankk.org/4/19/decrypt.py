#!/usr/bin/env python

def main():

	cracked_nums = []
	#crypted = "970105" # "123"
	crypted = "827400716220761113112780188862593389002185976803643291005369"
	chunked = [ int(crypted[i:i+2]) for i in range(0, len(crypted),2) ]

	for index, crypt_num in enumerate(chunked):
		for number in range(0,100):
			if (number * 7 - ((index + 1) * 3)) % 100 == crypt_num:
				cracked_nums.append(number)
				continue

	test = map(str,cracked_nums)
	print "".join([ c.zfill(2) for c in test ])

main()
