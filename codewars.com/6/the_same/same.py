#!/usr/bin/env python


def comp(a1, a2):
    if None in (a1, a2):
        return False
    elif not a1 or not a2:
        return True

    for n in a1:
        n2 = n**2
        i = a2.count(n2)
        if not i:
            return False
        a2.remove(n2)
    return True

if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print comp(a1, a2)

    a1 = [121, 144, 19, 161, 19, 144, 19, 11]  
    a2 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

    print comp(a1, a2)
