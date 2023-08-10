#!/usr/bin/python3
for asciit in range(ord('a'), ord('z')+1):
    if asciit != ord('q') and asciit != ord('e'):
        print("{}".format(chr(asciit)), end="")
