#!/usr/bin/python3
def uppercase(str):
    if len(str) == 0:
        print("error")
        return
    j = 0
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="\n" if j == len(str) - 1 else "")
        j = j + 1
