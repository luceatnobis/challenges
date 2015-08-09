#!/usr/bin/env python3
# https://www.hackthis.co.uk/levels/coding/1

import re
import sys

import requests

def main():
    if len(sys.argv) < 3:
        print("Usage: %s <username> <password> <additional data>",
                file=sys.stderr)
        return 1

    chall_url = "https://www.hackthis.co.uk/levels/coding/1"

    sess = requests.Session()
    user_info = {
        'username': sys.argv[1],
        'password': sys.argv[2],
    }
    resp = sess.post("https://www.hackthis.co.uk/?login", data=user_info)
    if user_info['username'] not in resp.content.decode():
        print("Login was unsuccessful, check login details.", file=sys.stderr)
        return 1
    
    content = sess.get(chall_url).content.decode()
    words = re.search("(?<=<textarea>)[^<]+", content).group(0).split(", ")
    s_words = sorted(words)

    print(words)
    print(", ".join(s_words))
    sess.post(chall_url, data={'answer': ", ".join(s_words)})
    
if __name__ == "__main__":
    main()
