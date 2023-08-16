#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    if roman_string == "":
        return (0)
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    convert = 0
    for i, k in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[k]:
            convert += dic[i]
        else:
            convert -= dic[i]
    convert += dic[roman_string[-1]]
    return convert
