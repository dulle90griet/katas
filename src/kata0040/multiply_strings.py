def multiply_strings(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    int_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9
    }

    res = []
    for j in range(len(num2)):
        carry = 0
        cur = "0" * j

        for i in range(len(num1)-1, -1, -1):
            d_1 = int_map[num1[i]]
            d_2 = int_map[num2[len(num2) - 1 - j]]

            val = d_1 * d_2 + carry
            cur = f"{val % 10}{cur}"
            carry = val // 10

        if carry > 0:
            cur = f"{carry}{cur}"

        res.append(cur)

    max_len = max(len(r) for r in res)
    
    ans, carry, i = "", 0, 0
    for i in range(max_len):
        cur = carry
        for r in res:
            if i < len(r):
                cur += int_map[r[-(i+1)]]

        ans = f"{cur % 10}{ans}"
        carry = cur // 10     

    if carry > 0:
        ans = f"{carry}{ans}"

    return ans
