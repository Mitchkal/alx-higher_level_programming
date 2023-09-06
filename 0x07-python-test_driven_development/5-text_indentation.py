#!/sr/bin/python3
"""
module 5-text_indentation
 prints a text with 2 new lines
 after each of these characters:
 ., ? and :
 """


def text_indentation(text):
    """indents text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ":?.":
        text = text.replace(char, char + "\n\n")

    strings = [line.strip(' ') for line in text.split('\n')]
    final = "\n".join(strings)

    print(final, end="")
