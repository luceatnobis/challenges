#!/usr/bin/env python3
# https://www.hackthis.co.uk/levels/captcha/3
# Jess totally helped me in me boneheaded moments

import re
import sys
import io
import hashlib

from itertools import groupby
from operator import itemgetter

import requests
from PIL import Image


def main():
    """
    if len(sys.argv) < 3:
        print(
            "Usage: %s <username> <password> <additional data>" % sys.argv[0],
            file=sys.stderr
        )
        return 1

    chall_url = "https://www.hackthis.co.uk/levels/captcha/3"
    captcha_url = "https://www.hackthis.co.uk/levels/extras/captcha3.php"

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
    sess.post(chall_url, data={'answer': "".join(result)})
    """

    captcha("hi")

def captcha(img):

    img = Image.open(sys.argv[1])

    BG = (30, 30, 30)
    smileys = list()
    font_cols = list()

    ram = img.load()

    lines = [x.rstrip() for x in open("dict").readlines()]
    hashes = dict(l.split('#') for l in lines)

    xDim, yDim = img.size
    # finding all the columns which have smiley in them
    for x in range(xDim):
        for y in range(yDim):
            if ram[x, y] == BG:
                continue
            font_cols.append(x)
            break

    c = 0
    collection = list()
    # we group the columns. see http://stackoverflow.com/q/3149440/3716299
    for k, g in groupby(enumerate(font_cols), lambda x: x[0]-x[1]):
        smiley = list()
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
                smiley.append(" ") if ram[x, y] == BG else smiley.append("1")
        collection.append("".join(smiley))

        # print(l[0], l[-1], y_upper, y_lower, l[-1] - l[0], y_lower - y_upper)
        c = img.crop(box=(l[0], y_upper, l[-1], y_lower))
        c.save("coolface.png")
        """
        for s_n, s in enumerate(collection):
            for i, foo in enumerate(collection):
                if s_n == i:
                    continue
        """


    """
        # iterating over exact smiley coords
        for y in range(y_upper, y_lower + 1):
            for x in range(l[0], l[-1] + 1):
                smiley.append(b"0") if ram[x, y] == BG else smiley.append(b"1")
        smileys.append(hashes[hashlib.md5(b"".join(smiley)).hexdigest()])
        """

    return smileys

if __name__ == "__main__":
    main()
