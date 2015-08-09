#!/usr/bin/env python3
# https://www.hackthis.co.uk/levels/captcha/1
# Jess totally helped me in me boneheaded moments
# In fact, without Jess this code would not work.

import re
import sys
import io
import hashlib

from itertools import groupby
from operator import itemgetter

import requests
from PIL import Image


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: %s <username> <password> <additional data>" % sys.argv[0],
            file=sys.stderr
        )
        return 1

    chall_url = "https://www.hackthis.co.uk/levels/captcha/1"
    captcha_url = "https://www.hackthis.co.uk/levels/extras/captcha1.php"

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
    img = Image.open(io.BytesIO(sess.get(captcha_url).content))

    result = captcha(img)
    sess.post(chall_url, data={'answer': "".join(result[::-1])})


def captcha(img):

    BG = (30, 30, 30)
    chars = list()
    font_cols = list()

    ram = img.load()

    xDim, yDim = img.size
    for x in range(xDim):
        for y in range(yDim):
            ctup = ram[x, y]
            if ctup[1] < 55 or ctup[0] > 10 or ctup[2] > 10:
                ram[x, y] = BG

    lines = [x.rstrip() for x in open("dict").readlines()]
    hashes = dict(l.split(':') for l in lines)

    xDim, yDim = img.size
    # finding all the columns which have letters in them
    for x in range(xDim):
        for y in range(yDim):
            if ram[x, y] == BG:
                continue
            font_cols.append(x)
            break

    # we group the columns. see http://stackoverflow.com/q/3149440/3716299
    for k, g in groupby(enumerate(font_cols), lambda x: x[0]-x[1]):
        char = list()
        l = list(map(itemgetter(1), g))
        y_upper, y_lower = None, None
        for y in range(yDim):
            for x in range(l[0], l[-1]+1):
                # getting the upper y coordinate
                if ram[x, y] != BG and not y_upper:
                    y_upper = y
                # getting the upper y coordinate
                if ram[x, yDim - y - 1] != BG and not y_lower:
                    y_lower = yDim - y - 1

        for y in range(y_upper, y_lower + 1):
            for x in range(l[0], l[-1] + 1):
                char.append(b"1") if ram[x, y] == BG else char.append(b"0")

        chars.append(hashes[hashlib.md5(b"".join(char)).hexdigest()])
        """
        try:
            chars.append(hashes[hashlib.md5(b"".join(char)).hexdigest()])
        except KeyError:
            new_items = [b" " if x == b"1" else b"0" for x in char]
            print(b"".join(new_items).decode())
            print(hashlib.md5(b"".join(char)).hexdigest())

        # iterating over exact smiley coords
        for y in range(y_upper, y_lower + 1):
            for x in range(l[0], l[-1] + 1):
                print("1",end='') if ram[x, y] == BG else print("0",end='')
            print()
        print()
        """
    return chars

if __name__ == "__main__":
    main()
