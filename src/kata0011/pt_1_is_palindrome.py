""" Write a function that returns `True` if an integer is a palindrome, or `False` if it isn't. """

def is_palindrome(num: int) -> bool:
    # # string solution
    # return str(num) == str(num)[::-1]

    # stringless solution
    if num < 0: return False

    if num != 0 and num % 10 == 0:
        return False

    reversed_rear = 0
    while num > reversed_rear:
        reversed_rear = (reversed_rear * 10) + (num % 10)
        num //= 10
    
    return num == reversed_rear or num == reversed_rear // 10