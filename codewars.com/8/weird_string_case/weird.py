#!/usr/bin/env python

def to_weird_case(arg):
    return " ".join(map( lambda z: "".join(y.upper() if x % 2 == 0 else y.lower() for (x, y) in enumerate(z)), arg.split(" ")))

if __name__ == "__main__":
    print(to_weird_case("This"))
