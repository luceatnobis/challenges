#!/usr/bin/env python3

import re
import pdb
import sys
import requests

def main():
    if len(sys.argv[1:]) < 2:
        print("Usage: %s <username> <password>" % sys.argv[0], file=sys.stderr)
        sys.exit(1)

    base_url = "http://bright-shadows.net"
    login_url = "%s/login.php" % base_url
    challenge_url = base_url + "/challenges/programming/dit_dit_dah/tryout.php"
    solution_url = (
        base_url + "/challenges/programming/dit_dit_dah/solution.php"
    )
    params = {
        'retry': 'no',
        'submitted': '1',
        'edit_username': sys.argv[1],
        'edit_password': sys.argv[2],
    }
    session = requests.Session()
    resp = session.post(login_url, data=params)

    catalog = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }
    
    solution = ""
    raw = session.get(challenge_url).content.decode()
    morse_raw = re.search("(?<=')([^']+)", raw).group(0)

    prep = morse_raw.replace("1", ".").replace("0", "-").split("2")
    for l in prep:
        if l not in prep:
            exit(1)
        solution += catalog[l]
    resp = session.get(solution_url, params={'solution': solution})
    print(resp.content.decode())

if __name__ == "__main__":
    main()
