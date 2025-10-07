def my_pow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    res = my_pow(x, n//2)

    if n % 2:
        return res * res * x
    else:
        return res * res
