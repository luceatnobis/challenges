#!/usr/bin/env python3

import sys
import time
import socket

host = "vuln2015.icec.tf"
port = 9000

sock = socket.socket()
sock.connect((host, port))

answers = list()

while True:
    input_collection = list()
    num_collection = list()
    assignment = ""
    while True:
        leave = False
        recv = sock.recv(16384).decode()
        input_collection.append(recv)
        if "the numbers" in recv:
            break
    nums, assignment = "".join(input_collection).split("\n")
    i = [int(x) for x in nums.split(" ") if x]

    verb = assignment.split(" ")[2]
    if verb == "maximum":
        answer = max(i)
    elif verb == "minimum":
        answer = min(i)
    elif verb == "average":
        answer = sum(i) / len(i)
    elif verb == "sum":
        answer = sum(i)
    else:
        print(assignment)
        sys.exit()

    answers.append(answer)
    sock.send(("%s\n" % answer).encode())
