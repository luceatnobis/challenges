#!/usr/bin/env python3

def main():

    tree = []
    filename = "triangle_test"
    # filename = "triangle"
    for l in open(filename).readlines():
        tree.append([int(x) for x in l.rstrip().split(" ")])


    l = tree[0]
    for r in tree[1:]:
        nl = [l[0]+r[0]]
        for i in range(1,len(r)-1):
            nl.append(
                max(l[i-1], l[i]) + r[i]
                )
        nl.append(l[-1]+r[-1])
        print(nl)
        l = nl


if __name__ == "__main__":
    main()
