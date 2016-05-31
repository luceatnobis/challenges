#!/usr/bin/env python3

# https://www.youtube.com/watch?v=BTVt1OKp7v0
# http://puzzling.stackexchange.com/q/546
# http://math.stackexchange.com/q/1192961

from io import BytesIO

import re
import sys
import requests

from PIL import Image

colour_to_letter = {
    (0xFF, 0x00, 0x00): 'R', (0x00, 0x00, 0x00): 'B', (0xFF, 0xFF, 0xFF): 'W'
}


def main():
    base_url = "https://www.sabrefilms.co.uk/revolutionelite/"
    result_url = base_url + "mmres.php"  # ?result=1
    raw_chall_url = base_url + "mastermind.php"
    login_url = base_url + "login.php"
    if len(sys.argv) != 3:
        print("Usage: %s <username> <password>" % sys.argv[0])
        return

    auth = {'username': sys.argv[1], 'password': sys.argv[2]}

    colours = "ROYGBW"

    session = requests.Session()
    session.post(login_url, data=auth)  # logs in
    c = session.get(raw_chall_url).content.decode()
    if "Log Out" not in c:
        print("Username or password invalid; exiting")
        return

    conseq = lambda x: re.search("won games: (\d)", x).group(1)

    for game in range(1, 6):
        round_nr = 1
        guess = 'RROO'
        solutions = list(gen(4, list(colours)))
        print("Starting game", game)
        session.get(raw_chall_url, params={'start': '1'})

        while True:
            session.get(raw_chall_url, params={'solution': guess})
            res_resp = session.get(
                result_url, params={'result': str(round_nr)}
            )
            result_raw = res_resp.content
            feedback = retrieve_guess(result_raw)

            solutions = [x for x in solutions if evaluate(guess, x, feedback)]
            if len(solutions) == 0:
                break
            guess = solutions.pop(0)
            round_nr += 1
        c = session.get(raw_chall_url).content.decode()
        print("Solved", conseq(c), "of 5")


def retrieve_guess(content):
    img = Image.open(BytesIO(content))
    ram = img.load()

    return "".join(
        colour_to_letter[ram[25 + (i * 50), 40]] for i in range(4)
    )


def evaluate(guess, code, result):
    return result == mastermind_feedback(guess, code)


def mastermind_feedback(guess, code):
    code, guess = list(code), list(guess)
    red, black, white = 0, 0, 0
    for i, g in enumerate(guess):
        if g not in code:
            black += 1
            guess[i] = 0
        elif g == code[i]:
            red += 1
            code[i] = 0
            guess[i] = 0

    for i, g in enumerate(guess):
        if g == 0 or g not in code:
            continue
        white += 1
        code[code.index(g)] = 0
    return ('R' * red + 'W' * white + 'B' * black).ljust(4, 'B')


def gen(n=0, elements=[], already=[]):
    if n == 0:
        yield "".join(already)
    else:
        for e in elements:
            for r in gen(n - 1, elements, already + [e]):
                yield r

if __name__ == "__main__":
    main()
