#!/usr/bin/env python

def ipToInt32(ip):
    return int("".join([bin(x)[2:].zfill(8) for x in map(int, ip.split("."))]), 2)

if __name__ == "__main__":
    print ipToInt32("128.32.10.1")
