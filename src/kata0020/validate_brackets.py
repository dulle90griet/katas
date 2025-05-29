def validate_brackets(self, s: str) -> bool:
    # create a structure of list nodes
    # in each node, index 0 is a pointer to the parent node
    # index 1 is the bracket type
    # indexes 2+ are pointers to child nodes
    # the top-level node has parent None

    cur_node = [None, None]
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