def count_and_say(n: int) -> str:
    s = "1"

    for _ in range(n - 1):
        temp, count, prev = "", 0 , s[0]
        for char in s:
            if char == prev:
                count += 1
            else:
                temp += f"{count}{prev}"
                prev, count = char, 1
        temp += f"{count}{prev}"
        s = temp

    return s
