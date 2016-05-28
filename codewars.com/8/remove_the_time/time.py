#!/usr/bin/env python3

def shorten_to_date(arg):
    return arg.split(",")[0]

if __name__ == "__main__":
    print(shorten_to_date("Monday February 2, 8pm"))
