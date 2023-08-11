#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)

    if length == 1:
        print("{} {}".format('0', 'arguments.'))
    elif length == 2:
        print("{} {}".format('1', 'argument:'), end="\n")
        print("{} {}".format('1:', sys.argv[1]), end="\n")
    elif length > 2:
        print("{} {}".format(length - 1, 'arguments:'), end="\n")
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]), end="\n" if i != length else
                  "")
