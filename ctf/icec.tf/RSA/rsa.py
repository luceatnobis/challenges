#!/usr/bin/env python3

def chunks(line, n=2):
    for i in range(0, len(line), n):
        yield line[i:i+n]

def main():
    plain = list()
    l = [x.rstrip() for x in open("data").readlines()]
    globals().update({k: int(v, 16) for (k, v) in [y.split(" = ") for y in l]})

    ciphertext = c.to_bytes(128, "big")
    decrypted = pow(c, d, N)
    for h in chunks(hex(decrypted)[2:]):
        plain.append(int(h, 16))
    print("".join(chr(x) for x in plain))

if __name__ == "__main__":
    main()
