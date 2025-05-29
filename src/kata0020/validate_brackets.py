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
                # If `s` can only contain brackets, `c` must be a closing bracket`
                # And if the stack is empty, that bracket can't have been opened
                return False
    
    return not stack