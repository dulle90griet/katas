def validate_brackets(self, s: str) -> bool:
    # create a structure of list nodes
    # in each node, index 0 is a pointer to the parent node
    # index 1 is the bracket type
    # indexes 2+ are pointers to child nodes
    # the top-level node has parent None

    cur_node = [None, None]
    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for c in s:
        if c in brackets.values():
            # opening bracket encountered
            new_node = [cur_node, c]
            cur_node.append(new_node)
            cur_node = new_node
        else:
            # closing bracket encountered
            if brackets[c] != cur_node[1]:
                # bracket doesn't match currently open type - return false
                return False
            else:
                # bracket matches
                if cur_node[0]:
                    # return to the parent level ...
                    cur_node = cur_node[0]
                    # ... and pop this node to close it
                    cur_node.pop()

    # if all nodes are closed, return true
    if cur_node[0] is None:
        return True
    return False