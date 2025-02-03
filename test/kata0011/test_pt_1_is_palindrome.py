from src.kata0011.pt_1_is_palindrome import is_palindrome

def test_is_palindrome_returns_True_for_palindrome_of_even_length():
    assert is_palindrome(1221)
    assert is_palindrome(6745225476)
    assert is_palindrome(22)
    assert is_palindrome(90488409)

def test_is_palindrome_returns_True_for_palindrome_of_odd_length():
    assert is_palindrome(34543)
    assert is_palindrome(1)
    assert is_palindrome(9274729)
    assert is_palindrome(1234567890987654321)

def test_is_palindrome_returns_False_for_non_palindrome():
    assert is_palindrome(257) is False
    assert is_palindrome(9949) is False
    assert is_palindrome(2789422) is False
    assert is_palindrome(10) is False