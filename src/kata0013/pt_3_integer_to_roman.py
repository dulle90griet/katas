""" Convert a decimal integer to Roman numerals. """

def int_to_roman(num: int) -> str:
    rom = ""

    n = num // 1000
    num = num % 1000
    rom += "M" * n

    n = num // 100
    num = num % 100
    if n == 9:
        rom += "CM"
    elif n >= 5:
        rom += "D" + "C" * (n - 5)
    elif n == 4:
        rom += "CD"
    else:
        rom += "C" * n
    
    n = num // 10
    num = num % 10
    if n == 9:
        rom += "XC"
    elif n >= 5:
        rom += "L" + "X" * (n - 5)
    elif n == 4:
        rom += "XL"
    else:
        rom += "X" * n
    
    n = num
    if n == 9:
        rom += "IX"
    elif n >= 5:
        rom += "V" + "I" * (n - 5)
    elif n == 4:
        rom += "IV"
    else:
        rom += "I" * n

    return rom