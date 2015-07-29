#!/usr/bin/env python

def part_1():

	new_content = []

	with open("huge_ch", "rb") as f:
		huge_ch = f.read()

	for byte in huge_ch:
		if 0x30 > byte:
			byte += 1
		elif byte < 0x2A:
			byte += 2

		new_content.append(byte)

	blabla = [new_content[x] for x in range(len(new_content)) if not x % 2 == 0 ]
	with open("part1.dat", "wb") as f:
		f.write("".join(blabla))

def part_2():

	and_list = []

	with open("part1.dat", "rb") as f:
		part1_dat = f.read()

	with open("hugex0r.bin", "rb") as f:
		hugex0r_bin = f.read()

	for i, (p, h) in enumerate(zip(part1_dat, hugex0r_bin)):
		and_list.append( ord(p) & ord(h) )

	and_list = [chr(x) for x in and_list]

	with open("part2.dat", "wb") as f:
		f.write("".join(and_list))

def part_3():

	with open("part") # this is stupid

part_3()
