#!/usr/bin/env python3

import socks

def main():

    a = socks.socksocket()
    a.set_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9051)

    a.connect(("wtfismyip.com", 80))
    a.send(b"GET /text HTTP/1.0\r\nHost: wtfismyip.com\r\n\r\n")

if __name__ == "__main__":
    main()
