""" Implement a function to convert a string to a 32-bit signed integer.

Ignore any leading whitespace.

Determine the sign by checking if the next character is `-` or `+`. Assume positivity if neither features.

Skip any leading zeros, then read the integer until a non-digit character is encountered or the end of the string is reached. If no digits are read, the value is 0.

Make sure the integer is rounded within the 32-bit signed integer range, from `- 2 ** 31` to `2 ** 31 - 1`. """

import re

def a_to_i(s: str) -> int:
    _, sign, num = re.match(r"(\s*)([-+]?)0*(\d*)", s).groups()
    sign = -1 if sign and sign[0] == "-" else 1
    num = int(num) * sign if num else 0

    if num < -(2 ** 31):
        num = -(2 ** 31)
    elif num > (2 ** 31) - 1:
        num = (2 ** 31) - 1

    return num
