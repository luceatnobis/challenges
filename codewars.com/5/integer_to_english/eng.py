#!/usr/bin/env python3

import pdb

def int_to_english(n):
    # solution: 'twenty five billion one hundred sixty one million forty five thousand six hundred fifty six'
    one = [
        "one", "two", "three", "four", "five",  "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    ]
    tens = [
        "twen", "thir", "four", "fif"
    ]   
    chunks = map(int, format(n, ",").split(","))
    t_pot = divmod(len(str(n)), 3)

    l_join = lambda x: " ".join(map(str, x))

    for c in chunks:
        c_collection = []
        h, r = divmod(c, 100)
        if h != 0:
            c_collection.append(l_join([one[h], "hundred"]))
        t, r2 = divmod(r, 10)
        if t != 0:
            if t >= 2:  # 20-100
                # pdb.set_trace()
                t2 = "%sty" % tens[t-2] if t < 6 else "%sty" % one[t-1]
                t2 = t2.replace("tt", "t")
                print(n, t2)
                pass
            elif 15 < t:  # 1-15
                pass
        break


if __name__ == "__main__":
    for l in range(1, 9):
        int_to_english(121 + 10*l)
    # int_to_english(25161045656)
    # int_to_english(161045656)
