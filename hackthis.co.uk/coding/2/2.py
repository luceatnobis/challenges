#!/usr/bin/env python3
# https://www.hackthis.co.uk/levels/coding/2

import re
import sys

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
    words = re.search("(?<=<textarea>)[^<]+", content).group(0).split(", ")

    # sess.post(chall_url, data={'answer': ", ".join(s_words)})

def decrypt(ct):
    printable_chars = 95

    sequence = ct.split(",")
    decrypted = list()
    for x in sequence:
        if x.isspace():
            decrypted.append(x)
            continue
        what = chr(x)
        
    
if __name__ == "__main__":
    main()
