def longest_valid_parentheses(s: str) -> int:
    stack = []
    result = 0

    i = 0
    for j in range(len(s)):
        if s[j] == "(":
            stack.append(j)
        else:
            if not stack:
                i = j + 1
                continue
            if len(stack) == 1:
                result = max(result, j - i + 1)
            else:
                result = max(result, j - stack[-2])
            stack.pop()

    return result
