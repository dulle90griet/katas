def multiply_strings(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
         "7": 7, "8": 8, "9": 9, 0: "0", 1: "1", 2: "2", 3: "3",
         4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

    res = [0] * (len(num1) + len(num2))
    for j, c2 in enumerate(reversed(num2)):
        for i, c1 in enumerate(reversed(num1)):
            d1 = m[c1]
            d2 = m[c2]
            res[i + j] += d1 * d2
            res[i + j + 1] += res[i + j] // 10
            res[i + j] %= 10
    
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return "".join(m[c] for c in res)[::-1]
