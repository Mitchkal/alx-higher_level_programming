#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0 or n > 0:
        return (str[:n] + str[1 + n:])
    else:
        return (str)
