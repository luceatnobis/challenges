#!/usr/bin/env python3
import re

def ipv4_address(num):
    return bool(re.match("(\d){1,3}\.(\d){1,3}\.(\d){1,3}\.(\d){1,3}", num))
    

if __name__ == "__main__":
    print(ipv4_address("192.168.1.2"))
    print(ipv4_address("192.168.1"))
