#!/usr/bin/env python3

def likes(names):
    n = len(names)
    who = ""
    l = "like"

    if n == 0:
        who = "no one"
        l = "%ss" % l
    elif n == 1:
        who = "%s" % names[0]
        l = "%ss" % l
    elif n == 2:
        who = " and ".join(names)
    elif n == 3:
        who = "{}, {} and {}".format(*names)
    else:
        who = "{}, {} and %s others".format(*names[:2]) % (n - 2)

    return "%s %s this" % (who, l)

if __name__ == "__main__":
    print(likes([]))
    print(likes(["Paul"]))
    print(likes(["Paul", "Mary"]))
    print(likes(["Paul", "Mary", "John"]))
    print(likes(["Paul", "Mary", "John", "Ringo"]))
