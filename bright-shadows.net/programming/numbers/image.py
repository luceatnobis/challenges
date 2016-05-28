#!/usr/bin/env python

import os
import pdb
import Image

from glob import glob

def main():
    """
    files = glob("*png")
    for f in files:
        highlight(f)
    """
    highlight(

def process(fname):
    # output_name = "%s_output.png" % os.path.splitext(fname)[0]
    img = Image.open(fname).convert("RGB")
    xDim, yDim = img.size

    background = (0, 200, 255)
    font = (0, 0, 0)

    ram = img.load()
    
    for y in range(yDim):
        for x in range(xDim):
            if ram[x,y] == background:
                continue
            ram[x,y] = font

    # img.save(output_name)
    

if __name__ == "__main__":
    main()
