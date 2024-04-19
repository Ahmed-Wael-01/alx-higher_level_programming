#!/usr/bin/python3
"""indent a paragraph"""


def text_indentation(text):
    """prints a paragraph after putting 2 new lines after each . ? :"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
