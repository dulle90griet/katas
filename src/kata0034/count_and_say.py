memo = {}

def count_and_say(n: int) -> str:
    s = "1"

    for m in range(n - 1):
        if m in memo:
            s = memo[m]
            continue

        temp, count, prev = "", 0 , s[0]
        for char in s:
            if char == prev:
                count += 1
            else:
                temp += f"{count}{prev}"
                prev, count = char, 1
        temp += f"{count}{prev}"
        s = memo[m] = temp

    return s

