#!/usr/bin/python3

import socket
from struct import unpack, pack

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("vortex.labs.overthewire.org", 5842))

	bytes = []
	
	anus = sock.recv(1024)
	summ, = unpack("<I", anus)

	anus = sock.recv(1024)
	for i in range(0,12,4):
		n, = unpack("<I", anus[i:i+4])
		summ += n

	wat = pack('<Q', summ)
	
	sock.send(pack("<Q",summ))
	for i in range(3):
		print(sock.recv(4096))

main()
