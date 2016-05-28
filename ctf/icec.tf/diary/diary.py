#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import string
import argparse
import codecs

"""
My diary encryption script
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        # multiply by a prime for security
        key ^= ((2 * ord(ch)**2 + 3*ord(ch) + 7) & 0xff)

    return xor(input_data, key)

def decrypt(input_data, password):
    # This is XOR encryption, so decryption is just the same
    return encrypt(input_data, password)

def brute(input_data, password):
    s = string.ascii_lowercase + string.ascii_uppercase + " "
    for b in range(0, 256):
        d = xor(input_data, b)
        try:
            u = unicode(d)
        except UnicodeDecodeError:
            continue
        if filter(lambda x: x in s, u[:15]) == u[:15]:
            return u

def main():
    parser = argparse.ArgumentParser("Diary Encryption Script(DES) v3.14")

    parser.add_argument("action", choices=["encrypt", "decrypt", "brute"])
    parser.add_argument("file", help="The input file")
    parser.add_argument("outfile", help="The output file")
    parser.add_argument("password", help="The encryption password")

    opts = parser.parse_args()

    with codecs.open(opts.file, 'rb', "utf-8") as in_file:
        input_data = in_file.read()
    result_data = ""

    if opts.action == "encrypt":
        result_data = encrypt(input_data, opts.password)
    elif opts.action == "decrypt":
        result_data = decrypt(input_data, opts.password)
    elif opts.action == "brute":
        result_data = brute(input_data, opts.password)

    with codecs.open(opts.outfile, 'w', "utf-8") as out_file:
        out_file.write(result_data)

if __name__ == "__main__":
    main()
