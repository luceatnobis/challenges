#!/usr/bin/env python3
# https://www.hackthis.co.uk/levels/coding/2
# Its hard to overestimate what an incredible waste of time this challenge was.

import re
import sys
from itertools import count

import requests

def main():
    if len(sys.argv) < 3:
        print("Usage: %s <username> <password> <additional data>",
                file=sys.stderr)
        return 1

    chall_url = "https://www.hackthis.co.uk/levels/coding/2"

    sess = requests.Session()
    user_info = {
        'username': sys.argv[1],
        'password': sys.argv[2],
    }
    resp = sess.post("https://www.hackthis.co.uk/?login", data=user_info)
    if user_info['username'] not in resp.content.decode():
        print("Login was unsuccessful, check login details.", file=sys.stderr)
        return 1
    
    content = sess.get(chall_url).content.decode()
    words = re.search("(?<=<textarea>)[^<]+", content).group(0)
    result = "".join(decrypt(words))
    sess.post(chall_url, data={'answer': result})

def encrypt(pt):
    ct = list()
    number_printable = 94
    forward = {chr(k): v for (k, v) in zip(range(33, 127), count(start=1))}
    backward = {v: k for (k, v) in forward.items()}

    for p in pt:
        if p not in forward:
            ct.append(p)
            continue
        a = forward[p]
        b = number_printable - a
        c = backward[b]
        d = ord(c)
        ct.append(str(d))
        # print(p, a, b, c, d)

    return ",".join(ct)

def decrypt(ct):
    plain = list()
    number_printable = 94
    forward = {chr(k): v for (k, v) in zip(range(33, 127), count(start=1))}
    backward = {v: k for (k, v) in forward.items()}

    for ci in ct.split(","):
        try:
            # b is the character of that ascii value
            b = chr(int(ci))
        except ValueError:
            plain.append(ci)
            continue
        # c is the position of this character in the forward dict
        c = forward[b]
        # d is the number_printable - c 
        d = number_printable - c
        # e is the original ascii value of d
        e = backward[d]
        plain.append(e)
        # print(ci, b, c, d, e)

    return plain
    
if __name__ == "__main__":
    main()
