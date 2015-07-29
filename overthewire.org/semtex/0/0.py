#!/usr/bin/env python

import socket

def main():
	incoming, filtered = "", ""
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("141.138.199.118", 24000))

	try:
		while True:
			new = s.recv(4096)
			incoming += new
			if not new:
				break
	finally:
		s.close()
	
	for i in range(len(incoming)):
		if i % 2 == 0:
			filtered += incoming[i]
	
	print filtered
main()
