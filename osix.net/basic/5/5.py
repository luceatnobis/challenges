#/usr/bin/env python

def main():

	result = []
	final = []
	key = [ord(x) for x in "secret"] # key list

	with open("data.bin", "rb") as f:
		data = f.read()
	
	for i, byte in enumerate(data):
		byte = ord(byte)
		xor_byte = byte ^ key[i % len(key)]
		result.append(xor_byte)

	for byte in result:
		if byte == 23:
			byte = 0
		elif byte == 0:
			byte = 23
		elif byte == 78:
			byte = 66
		elif byte == 66:
			byte = 78
		elif byte == 36:
			byte = 144
		elif byte == 144:
			byte = 36
		final.append(byte)

	final = [chr(x) for x in final]

	with open("solution.jpg", "wb") as f:
		f.write("".join(final))
		
main()
