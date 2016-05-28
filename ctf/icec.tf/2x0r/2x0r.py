#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string
import argparse
import codecs

"""
My über secure encryption script!
"""

def xor(text, key1, key2):
    key1 = key1 * (len(text)//len(key1) + 1)
    key2 = key2 * (len(text)//len(key2) + 1)

    res = ""
    for i in range(len(text)):
        res += chr(ord(text[i]) ^ ord(key1[i]) ^ ord(key2[i]))
    return res

def encrypt(input_data, password1, password2):
    return xor(input_data, password1, password2)

def decrypt(input_data, password1, password2):
    # This is XOR encryption, so decryption is just the same
    return xor(input_data, password1, password2)

def brute(input_data):
    from string import ascii_lowercase as al, ascii_uppercase as au
    allowed = al + au + "!.: "
    brute_bytes = 6
    byte = [[] for x in range(brute_bytes)]
    for index in range(brute_bytes):
        for key in range(1, 256):
            p = ord(input_data[index]) ^ key
            if chr(p) not in allowed:
                continue
            byte[index].append(p)
    for a in byte[0]:
        for b in byte[1]:
            for c in byte[2]:
                custom_xor(input_data, [a, b, c])

    return "hi"

def custom_xor(input_data, key):
    key = key * (len(input_data)//len(key) + 1)

    res = ""
    for i, val in enumerate(input_data):
        res += chr(ord(val) ^ key[i])

def main():
    parser = argparse.ArgumentParser("My über secure encryption script!")

    parser.add_argument("action", choices=["encrypt", "decrypt", "brute"])
    parser.add_argument("file", help="The input file")
    parser.add_argument("outfile", help="The output file")
    parser.add_argument("password1", help="The first encryption password")
    parser.add_argument("password2", help="The second encryption password")

    opts = parser.parse_args()

    with codecs.open(opts.file, 'r', "utf-8") as in_file:
        input_data = in_file.read()
    result_data = ""

    if opts.action == "encrypt":
        result_data = encrypt(input_data, opts.password1, opts.password2)
    elif opts.action == "decrypt":
        result_data = decrypt(input_data, opts.password1, opts.password2)
    elif opts.action == "brute":
        result_data = brute(input_data)

    with codecs.open(opts.outfile, 'w', "utf-8") as out_file:
        out_file.write(result_data)

main()
