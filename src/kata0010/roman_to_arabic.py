# first attempt - O(n) complexity; beats 80%
# def roman_to_arabic(s: str) -> int:
#     values = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000
#     }

#     out = 0

#     for i in range(len(s) - 1):
#         if values[s[i]] < values[s[i+1]]:
#             out -= values[s[i]]
#         else:
#             out += values[s[i]]
#     out += values[s[-1]]
    
#     return out

# second attempt - O(n) complexity; beats 100%
# Note that in fact this is SLOWER than the previous solution if
# `for i in range(len(s))` is used - the speed improvement is 
# derived almost entirely from use of `for char in s`.
# Memory usage is slightly increased.

def roman_to_arabic(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number