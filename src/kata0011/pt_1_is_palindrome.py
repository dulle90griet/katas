""" Write a function that returns `True` if an integer is a palindrome, or `False` if it isn't. """

def is_palindrome(num: int) -> bool:
    # string solution
    return str(num) == str(num)[::-1]