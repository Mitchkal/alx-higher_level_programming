#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    import sys
    output = 0
    input_vars = len(argv) - 1
    if input_vars != 3:
        print("Usage: {} {} {} {}".format(argv[0], '<a>', '<operator>', '<b>'),
              end='\n')
        sys.exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            output += add(a, b)
            print("{} + {} = {}".format(a, b, output))
            sys.exit(0)
        elif argv[2] == '-':
            output += sub(a, b)
            print("{} - {} = {}".format(a, b, output))
            sys.exit(0)
        elif argv[2] == '*':
            output += mul(a, b)
            print("{} * {} = {}".format(a, b, output))
            sys.exit(0)
        elif argv[2] == '/':
            output += div(a, b)
            print("{} / {} = {}".format(a, b, output))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /",
                  end="\n")
            sys.exit(1)
