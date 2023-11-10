#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sums = 0
    num = 0
    for x in reversed(roman_string):
        num = roman[x]
        total += num if total < num * 5 else -num
    return total
