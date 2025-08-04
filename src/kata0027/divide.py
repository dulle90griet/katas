def divide(self, dividend: int, divisor: int) -> int:
    if dividend == divisor:
        return 1

    is_positive = (dividend < 0) == (divisor < 0)

    int_max = 2 ** 31
    if is_positive:
        int_max -= 1
        
    a, b = abs(dividend), abs(divisor)
    quotient = 0

    while a >= b:
        places = 0

        while a >= b << (places + 1):
            places += 1

        a -= b << places
        quotient += 1 << places
    
    quotient = min(quotient, int_max)
    
    return quotient if is_positive else -quotient
