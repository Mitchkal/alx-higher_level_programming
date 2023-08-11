#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sums = 0
    for i in range(1, length):
        sums += int(sys.argv[i])
    print("{}".format(sums))
