def longest_valid_parentheses(s: str) -> int:
    stack = []
    result = 0

    i = 0
    for j, ch in enumerate(s):
        if ch == "(":
            stack.append(j)
        else:
            if not stack:
                i = j + 1
                continue
            if len(stack) == 1:
                cur_len = max(result, j - i + 1)
            else:
                cur_len = max(result, j - stack[-2])
            stack.pop()

            if cur_len > result:
                result = cur_len

    return result
