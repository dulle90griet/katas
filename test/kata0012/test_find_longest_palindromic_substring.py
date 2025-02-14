from src.kata0012.find_longest_palindromic_substring import find_longest_palindrome


def test_returns_single_char_if_no_palindromes():
    assert find_longest_palindrome("a") == "a"

    result = find_longest_palindrome("abc")
    assert len(result) == 1
    assert result in "abc"

    result = find_longest_palindrome("defgaljdnki")
    assert len(result) == 1
    assert result in "defgaljdnki"


def test_returns_whole_string_if_string_is_palindromic():
    assert find_longest_palindrome("ababa") == "ababa"
    assert find_longest_palindrome("defilopolifed") == "defilopolifed"
    assert find_longest_palindrome("bb") == "bb"
    assert find_longest_palindrome("greggerg") == "greggerg"


def test_returns_longest_palindrome_from_middle_of_string():
    result = find_longest_palindrome("abcbedlamirrorrimaldebalonmosq")
    assert result == "bedlamirrorrimaldeb"

    result = find_longest_palindrome("aaaagegaadecimallamicedgfgonto")
    assert result == "decimallamiced"


def test_returns_longest_palindrome_from_end_of_string():
    result = find_longest_palindrome("ababacdegitalatiged")
    assert result == "degitalatiged"

    result = find_longest_palindrome("undertheseaamammallammam")
    assert result == "mammallammam"


def test_returns_longest_palindrome_from_beginning_of_string():
    result = find_longest_palindrome("racecarorracebike")
    assert result == "racecar"

    result = find_longest_palindrome("poordanisinadroopmappatella")
    assert result == "poordanisinadroop"
