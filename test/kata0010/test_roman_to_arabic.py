from src.kata0010.roman_to_arabic import roman_to_arabic

def test_r_to_a_returns_int():
    romans = ["I", "V", "X", "L", "C", "D", "M"]
    outputs = map(roman_to_arabic, romans)
    for output in outputs:
        assert type(output) is int

def test_r_to_a_returns_correct_value_for_whole_numerals():
    assert roman_to_arabic("I") == 1
    assert roman_to_arabic("XVI") == 16
    assert roman_to_arabic("MDCLI") == 1651
    assert roman_to_arabic("MMMM") == 4000
    assert roman_to_arabic("XXX") == 30

def test_r_to_a_returns_correct_value_for_subtractive_numerals():
    assert roman_to_arabic("IV") == 4
    assert roman_to_arabic("IX") == 9
    assert roman_to_arabic("XL") == 40
    assert roman_to_arabic("XC") == 90
    assert roman_to_arabic("CD") == 400
    assert roman_to_arabic("CM") == 900

    assert roman_to_arabic("XIV") == 14
    assert roman_to_arabic("MCDXCIX") == 1499
    assert roman_to_arabic("CMXLIV") == 944