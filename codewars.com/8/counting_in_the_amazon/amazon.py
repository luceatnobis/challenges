#!/usr/bin/env python2.7

def count_arara(n):
    t = divmod(n, 2)
    return ("adak " * t[0] + ("anane" if t[1] else "")).strip()

if __name__ == "__main__":
    print count_arara(2) == "adak"
