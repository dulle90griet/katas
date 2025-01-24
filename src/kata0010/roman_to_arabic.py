# first attempt - O(n) complexity; beats 80%
def roman_to_arabic(s: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    out = 0

    for i in range(len(s) - 1):
        if values[s[i]] < values[s[i+1]]:
            out -= values[s[i]]
        else:
            out += values[s[i]]
    out += values[s[-1]]
    
    return out

