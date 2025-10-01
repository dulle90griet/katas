def pow(x: float, n: int) -> float:
    if n < 0:
        n = abs(n)
        x = 1 / x
    res = 1
    for _ in range(n):
        res *= x
    return res