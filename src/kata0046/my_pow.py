def my_pow(x: float, n: int) -> float:
    if n < 0:
        n = -n
        x = 1 / x

    res = 1
    while n > 0:
        if n & 1:   # equivalent to n % 2
            res *= x
        x *= x
        n >>= 1     # equivalent to n //= 2

    return res
