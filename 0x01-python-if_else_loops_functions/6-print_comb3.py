#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i, 10):
        if (k != i):
            print("{}{}".format(i, k), end=", " if i != 8 else "\n")
