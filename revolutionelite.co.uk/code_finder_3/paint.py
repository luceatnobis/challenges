#!/usr/bin/env python3

import pdb
from PIL import Image

def main():
    with open("output") as f:
        c = [x for x in f.read().replace("\n", "").split(" ") if x]
    t = [[int(y) for y in c[i:i+2]] for i in range(0, len(c)-1, 2)]
    # pdb.set_trace()

    img = Image.new("RGB", (100, 100))
    ram = img.load()
    for y in range(100):
        for x in range(100):
            ram[y, x] = (0, 0, 0)

    for y, x in t:
        ram[y, x] = (255, 255, 255)
    img.save("output.png")

if __name__ == "__main__":
    main()
