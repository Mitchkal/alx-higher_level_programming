#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    return (length, sentence[0] if sentence and length > 0 else None)
