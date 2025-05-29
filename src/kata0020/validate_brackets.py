def validate_brackets(self, s: str) -> bool:
    stack = []
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for c in s:
        if c in ["(", "{", "["]:
            stack.append(c)
        else:
            if not stack or brackets[c] != stack.pop():
                return False
    
    return not stack